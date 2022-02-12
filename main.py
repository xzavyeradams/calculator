# Xzavyer Adams (2/11/22)
# This is a rewrite of a project I made in the sandbox.
# You can find this here: https://academy.cs.cmu.edu/sharing/crimsonSpider7815 (10/8/21)

from cmu_graphics import *

Rect(50, 30, 300, 50)
results = Label('Working Calculator', 200, 55, align='center', fill='white', size=25)

def makeButton(val, x, y):
    """This makes a calculator button"""
    textSize = 40
    boxL = 75
    boxW = 75

    shape = Rect(x, y, boxL, boxW, fill='lightSlateGrey', border='darkSlateGrey', borderWidth=2)
    Label(val, x + boxL / 2, y + boxW / 2, fill='white', size=textSize)

    shape.glyph = val

    return shape

# memory for numbers
tempnum = []
tempfin = []

# layout, this can be changed
buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '/',
    'C', '0', '=', '*'
]

# drawing positions
btnShapes = []
tx = 50
ty = 90
i = 0

# draws buttons to canvas
for button in buttons:
    s = makeButton(button, tx, ty)

    if i >= 3:
        # resets the position to the next row
        tx = 50
        ty += 75
        i = 0
    else:
        # moves right
        tx += 75
        i += 1

    btnShapes.append(s)

# clicking buttons & actual calculator logic
def onMousePress(x, y):
    # loops through buttons
    for button in btnShapes:
        if button.contains(x, y):
            button.fill = 'darkSlateGrey'
            button.border = 'lightSlateGrey'

            try:
                # updates memory and display value
                tempnum.append(int(button.glyph))
                results.value = "".join(n for n in tempfin) + "".join(str(i) for i in tempnum)
            except ValueError:
                if button.glyph == 'C':
                    # clears all memory and resets display
                    tempfin.clear()
                    tempnum.clear()
                    results.value = 'Working Calculator'
                elif button.glyph == '=':
                    try:
                        # adds all current numbers in tempnum memory to tempfin
                        tempfin.append("".join(str(i) for i in tempnum))
                        # creates an expression
                        expression = "".join(n for n in tempfin)
                        # gets the results
                        result = eval(expression)
                        # present to user via display
                        results.value = f"{expression} = {str(result)}"
                        # clears
                        tempfin.clear()
                        tempnum.clear()
                    except Exception as ex:
                        # DivisionByZero, etc
                        results.value = ex
                else:
                    # adds all of tempnum's memory to tempfin
                    tempfin.append("".join(str(i) for i in tempnum))
                    # adds operator to tempfin
                    tempfin.append(button.glyph)
                    # clears tempnum memory
                    tempnum.clear()
                    # present to user
                    results.value = "".join(n for n in tempfin) + "".join(str(i) for i in tempnum)

def onMouseRelease(x, y):
    for button in btnShapes:
        button.fill = 'lightSlateGrey'
        button.border = 'darkSlateGrey'

Label("Xzavyer Adams, 2/11/22", 200, 395, size=10)

cmu_graphics.run()
