# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1,arg2))

def print_one(arg1):
    print("arg1: %r" % arg1)

def print_none():
    print("I got nothing.")

print_two("Biswa","Chetna")
print_one("BIswa")
print_none()
