import turtle

x1, y1 = eval(input("Enter x1 and y1 for point 1:"))
x2, y2 = eval(input("Enter x2 and y2 for point 2:"))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)
turtle.done()
