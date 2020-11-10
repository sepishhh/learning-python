import re

run = True
previous = 0

print("Our Magical Calculator:")
print("Type 'quit' to exit\n")


def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("The first statement:")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Goodbye dear Sepi!")
        run = False
    else:
        equation = re.sub("[a-zA-Z,.:()' ']", "", equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
