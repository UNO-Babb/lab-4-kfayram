#TurtleGraphics.py
#Name: Kyle Fayram
#Date: 2/16/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
        
def drawPolygon(myTurtle, sides):
    for s in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)

def fillCorner(myTurtle, corner):
    #draw big square
    drawSquare(myTurtle, 100)
    if corner == 1:
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 2:
        myTurtle.forward(50)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 3:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif corner == 4:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.up()
        myTurtle.forward(50)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
        
def squaresInSquares(myTurtle, squares):
    for i in range(squares):
        size = 200
        drawSquare(myTurtle, size)
        myTurtle.up()
        #myTurtle.forward(10)
        #myTurtle.right(90)
        #myTurtle.forward(10)
        #myTurtle.left(90)
        myTurtle.down()

    


def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()