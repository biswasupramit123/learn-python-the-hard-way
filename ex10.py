tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."
list01 =["cat food", "fishes", "Catnip", "Grass"]

fat_cat = '''
I'll do a list:
\t* %s
\t* %s
\t* %s\n\t* %s
'''
print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat % (tuple(list01)))

