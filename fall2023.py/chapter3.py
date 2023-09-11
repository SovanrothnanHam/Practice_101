# abs(-3) # Returns the absolute value
# # 3
# abs(-3.5) # Returns the absolute value
# # 3.5
# max(2, 3, 4, 6) # Returns the maximum number
# # 6
# min(2, 3, 4) # Returns the minimum number
# # 2
# pow(2, 3) # Same as 2 ** 3
# # 8
# pow(2.5, 3.5) # Same as 2.5 ** 3.5
# # 24.705294220065465
# round(3.51) # Rounds to its nearest integer
# # 4
# round(3.4) # Rounds to its nearest integer
# # 3
# round(3.1456, 3) # Rounds to 3 digits after the decimal poin
# # 3.146

# import math
# math.fabs(-2)
# # 2.0
# math.ceil(2.1) 
# # 3
# math.ceil(-2.1) is -2
# math.floor(2.1) is 2
# math.floor(-2.1) is -3
# math.exp(1) is 2.71828
# math.log(2.71828) is 1.0
# math.log(100, 10) is 2.0
# math.sqrt(4.0) is 2
# math.sin(3.14159 / 2) is 1
# math.sin(3.14159) is 0
# math.asin(1.0) is 1.57
# math.asin(0.5) is 0.523599
# math.cos(3.14159 / 2) is 0
# math.cos(3.14159) is -1
# math.acos(1.0) is 0
# math.acos(0.5) is 1.0472
# math.tan(3.14159 / 4) is 1
# math.tan(0.0) is 0
# math.degrees(1.57) is 90
# math.radians(90) is 1.57
# import math# import math module to use the math functions
# # Test algebraic functions
# print("exp(1.0) =", )
# print("log(2.78) =", ) 
# print("log10(10, 10) =", )
# print("sqrt(4.0) =", )

# # Test trigonometric functions
# print("sin(PI / 2) =", )
# print("cos(PI / 2) =", )
# print("tan(PI / 2) =", )
# print("degrees(1.57) =", )
# print("radians(90) =", math.radians(90))
# math.degrees

# import turtle
# turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")
# turtle.done()

# import turtle 
# turtle.pensize(3)# Set pen thickness to 3 pixels
# turtle.penup()# Pull the pen up
# turtle.goto(-200, -50)
# turtle.pendown()# Pull the pen down
# turtle.circle(40, steps = 3)# Draw a triangle

# turtle.penup()
# turtle.goto(-100, -50)
# turtle.pendown()
# turtle.circle(40, steps = 4) # Draw a square

# turtle.penup()
# turtle.goto(0, -50)
# turtle.pendown()
# turtle.circle(40, steps = 5) # Draw a pentagon

# turtle.penup()
# turtle.goto(100, -50)
# turtle.pendown()
# turtle.circle(40, steps = 6) # Draw a hexagon

# turtle.penup()
# turtle.goto(200, -50)
# turtle.pendown()
# turtle.circle(40) # Draw a circle

# turtle.done()

import turtle
turtle.pensize(3)# Set pen thickness to 3 pixels
turtle.penup()# Pull the pen up
turtle.goto(-200, -50)
turtle.pendown()# Pull the pen down
turtle.begin_fill()
turtle.color("red")
turtle.circle(40, steps = 3)# Draw a triangle
turtle.end_fill()

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5) # Draw a pentagon

# turtle.penup()
# turtle.goto(100, -50)
# turtle.pendown()
# turtle.circle(40, steps = 6) # Draw a hexagon

# turtle.penup()
# turtle.goto(200, -50)
# turtle.pendown()
# turtle.circle(40) # Draw a circle









