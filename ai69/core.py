import os
import venv
import requests
import subprocess
import re
import platform

class APIError(Exception):
    pass

class Ai69:
    def __init__(self):
        self.key = os.getenv('OPENAI_API_KEY')
        self.venv_path = os.path.join(os.path.dirname(__file__), 'venv')
        self._create_venv()

    def set_key(self, k):
        self.key = k
        if not self.key:
            raise ValueError("API key not provided")

    def __getattr__(self, name):
        def func(*args):
            if not self.key:
                raise APIError("API key not set")
            
            prmpt = self._gen_prmpt(name, args)
            msg = [{"role": "user", "content": prmpt}]
            resp = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"},
                json={"messages": msg, "model": "gpt-3.5-turbo-1106", "max_tokens": 512}
            )

            if resp.status_code != 200:
                raise APIError("Invalid API key or server error encountered")

            code = resp.json()['choices'][0]['message']['content'].strip()
            # # exec(code, globals())
            # # return locals()[name](*args)

            # lvars = {}
            # exec(code, globals(), lvars)
            # genf = lvars.get(name)

            # if not callable(genf):
            #     raise RuntimeError(f"Function '{name}' could not be generated.")

            # return genf(*args)
            try:return eval(self._exec(code, name, args))
            except Exception as e:return self._exec(code, name, args)
        return func

    def _gen_prmpt(self, name, args):
        return (
            f"# give a python function with exact {name} function name. --import-all-dependensies --no-explanation --only-code --output-complete-function --include-function-header\n" +
            f"use : {name}(args)\n\n"
            "\n".join(f"# type of arg{i+1}: {type(arg).__name__}" for i, arg in enumerate(args)) +
            f"\ndef {name}({', '.join(f'arg{i+1}' for i in range(len(args)))}):\n    "
        )


    def _create_venv(self):
        if not os.path.exists(self.venv_path):
            venv.create(self.venv_path, with_pip=True)
    
    def _extract_deps(self, code):
        imports = re.findall(r'^import (\S+)|^from (\S+) import', code, re.MULTILINE)
        deps = [match[0] or match[1] for match in imports]
        return set(deps)

    def _install_deps(self, deps):
        if platform.system() == "Windows":pip_path = os.path.join(self.venv_path, 'Scripts', 'pip')
        else:pip_path = os.path.join(self.venv_path, 'bin', 'pip')

        for dep in deps:
            var = subprocess.run([pip_path, "install", dep], check=False, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
    def _exec(self, code, name, args):
        deps = self._extract_deps(code)
        self._install_deps(deps)
        python_venv = os.path.join(self.venv_path, 'Scripts' if platform.system() == "Windows" else 'bin', 'python')
        serialized_args = ', '.join(repr(arg) for arg in args)
        main_function = f"""\ndef main():\n    result = {name}({serialized_args})\n    print(result)\n\n{code}\n\nmain()"""
        result = subprocess.run([python_venv, "-c", main_function], capture_output=True, text=True, shell=False)
        if result.stderr:
            raise RuntimeError(result.stderr.strip())
        return result.stdout.strip()

