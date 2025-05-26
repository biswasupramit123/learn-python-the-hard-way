from sys import argv

script = argv
prompt = "> "

print("Type the filename again: ")
print(open(input(prompt)).read())
