from ai69 import ai

ai.set_key('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')

print(ai.getWeather('Chennai'))
print(ai.randomNumberBetween(1, 10))
print(ai.slugify('My Article'))
print(ai.hasProfanityRegex('f*ck this lol'))
print(ai.extractHashtags('this is #really cool! #ai #code'))
print(ai.getProgrammerJoke())
