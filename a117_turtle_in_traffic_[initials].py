 #   a117_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
	#create horiztonal turtles
	ht = trtl.Turtle(shape=s)
	horiz_turtles.append(ht)
	ht.penup()
	new_color = horiz_colors.pop()
	ht.fillcolor(new_color)
	ht.goto(-350, tloc)
	ht.setheading(0)
	#create vertical turtles
	vt = trtl.Turtle(shape=s)
	vert_turtles.append(vt)
	vt.penup()
	new_color = vert_colors.pop()
	vt.fillcolor(new_color)
	vt.goto( -tloc, 350)
	vt.setheading(270)
  
	tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
while steps < 50:
	for h in horiz_turtles:
		for v in vert_turtles:
			v.forward(10)
			x1 = v.xcor()
			y1 = v.ycor() 
			h.forward(10)
		
			x2 =h.xcor() 
			y2 =h.ycor() 
			
			if (abs(x1 - x2 <= 20) and abs(y1 - y2 <= 20)):
				horiz_turtles.remove(h)
				vert_turtles.remove(v)
				h.color("gray")
				v.color("gray")
			
			
	steps = steps + 1
	#while loop or for loop to make each turtle move using t.forward(10)
	#find x, y by using t.xcor(), and t.ycor()
	#if abs(x1 - x2) < 20 and abs(y1 - y2) < 20: 
	#ht.remove(bad turtle)



wn = trtl.Screen()
wn.mainloop()
