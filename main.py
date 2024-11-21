#   a123_pear_1.py
import turtle as trtl

#-----setup-----
pear_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(pear_image) # Make the screen aware of the new file

pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def drawpear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

def letter():
  pear.setheading(90)
  pear.forward(100)
  pear.write("A", (font = 'Arial', 12, 'normal'))
  pear.backward(100)
def drop():
  pear.penup()
  pear.setheading(270)
  pear.forward(125)
  pear.hideturtle()



#-----function calls-----
letter()
drawpear(pear)
wn.onkeypress(drop, "a")
wn.listen()
wn.mainloop()
