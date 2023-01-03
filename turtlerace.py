from turtle import Turtle 

riley = Turtle()  # create an instance of a turtle object
riley.color('red')  # customise color attribute using the color method
riley.shape('turtle')  # customise shape attribute using the shape method
riley.penup()
riley.goto(-160, 100)
riley.pendown()

dylan = Turtle()
dylan.color('blue')
dylan.shape('turtle')
dylan.penup()
dylan.goto(-160, 70)
dylan.pendown()

kyle = Turtle()
kyle.color('purple')
kyle.shape('turtle')
kyle.penup()
kyle.goto(-160, 40)
kyle.pendown()

mum = Turtle()
mum.color('pink')
mum.shape('turtle')
mum.penup()
mum.goto(-160, 10)
mum.pendown()

from random import randint

for movement in range(100):
    riley.forward(randint(1,5))
    dylan.forward(randint(1,5))
    kyle.forward(randint(1,5))
    mum.forward(randint(1,5))
    
    