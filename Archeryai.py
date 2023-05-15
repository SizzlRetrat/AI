

# Import the turtle module
import turtle

# Create a screen object
screen = turtle.Screen()
screen.title("Archery Game")
screen.bgcolor("lightblue")

# Create a turtle object for the bow
bow = turtle.Turtle()
bow.shape("square")
bow.color("brown")
bow.shapesize(0.5, 4)
bow.penup()
bow.goto(-300, 0)

# Create a turtle object for the arrow
arrow = turtle.Turtle()
arrow.shape("triangle")
arrow.color("black")
arrow.shapesize(0.5, 2)
arrow.penup()
arrow.goto(-300, 0)
arrow.setheading(90)

# Create a turtle object for the target
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.shapesize(5, 5)
target.penup()
target.goto(200, 0)

# Define a function to shoot the arrow
def shoot():
# Get the angle and force from the user
angle = int(screen.textinput("Angle", "Enter the angle (0-90): "))
force = int(screen.textinput("Force", "Enter the force (1-10): "))

# Set the arrow heading and speed
arrow.setheading(angle)
arrow.speed(force)

# Move the arrow until it hits the target or misses
while True:
arrow.forward(10)
x = arrow.xcor()
y = arrow.ycor()

# Check if the arrow hits the target
if x > 180 and x < 220 and y > -50 and y < 50:
# Display a message and end the game
screen.textinput("Result", "You hit the target!")
break

# Check if the arrow misses the target
if x > 300 or y > 300 or y < -300:
# Display a message and end the game
screen.textinput("Result", "You missed the target!")
break

# Bind the space key to the shoot function
screen.onkey(shoot, "space")

# Listen for keyboard events
screen.listen()

# Main loop
screen.mainloop()

