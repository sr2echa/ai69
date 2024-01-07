from setuptools import setup, find_packages

with open("README.md", "r") as f:
    discription = f.read()

setup(
    name='ai69',
    version='0.1.1',
    author='Sreecharan S.',
    description='An AI function generator for runtime',
    url='https://github.com/sr2echa/ai69', 
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=discription,
    long_description_content_type="text/markdown",
)
