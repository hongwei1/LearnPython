def hasNumbers(inputString): return any(char.isdigit() for char in inputString)

print(hasNumbers("hognog"))
print(hasNumbers("hognog 32"))