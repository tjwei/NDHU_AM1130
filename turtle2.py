import turtle
wn = turtle.Screen()
wn.clearscreen()
alex = turtle.Turtle()
alex.shape('turtle')
alex.shapesize(2)
alex.width(5)
alex.clear()
length = 350
alex.clear()
length = 350
for i in range(12):    
    r=i%3    
    if r==0:
        alex.color('red')
    elif r==1:
        alex.color('green')
    elif r==2:
        alex.color('blue')  
    else:
        print("??????")
    alex.forward(length)
    alex.left(150)