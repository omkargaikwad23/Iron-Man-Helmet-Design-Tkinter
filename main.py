import turtle
import time
turtle.bgcolor("black")
t = turtle.Pen()

t.color("#950602","yellow")

t.begin_fill()
t.speed(10)   #speed
t.width(3)
t.forward(40)   #hanuwati

t.left(60)
t.forward(60)   #chick
t.left(30)
t.forward(50)

t.right(20)
t.forward(20)  #corner
t.left(40)
t.forward(20)

t.right(20)
t.forward(80)  # aakh

t.left(60)
t.forward(50)  #in head right

t.left(110)
t.forward(80)  # head gap down journey

t.right(80)
t.forward(35)  #head flat bottom surface


t.right(80)
t.forward(80)   #upward filling making head gap

t.left(110)
t.forward(50)   #in head left

t.left(60)      #left aakh
t.forward(80)

t.right(20)
t.forward(20)
t.left(40)
t.forward(20)   #right corner

t.right(20)
t.forward(50)

t.left(30)
t.forward(60)  #right chick

t.left(60)
t.forward(49)
t.end_fill()            #.....Color Face
t.penup()
t.forward(40)

t.left(60)
t.forward(60)
t.left(30)
t.forward(50) #went pen at right corner bottom

t.pendown()
#t.color("orange")
t.left(150)
t.forward(70)

#t.color("#950602","white")
#t.begin_fill()
t.right(150)  #towards mouth
t.forward(15)
t.left(90)
t.forward(80)
t.left(90)
t.forward(15)  #varch oth unchi
t.right(150)
t.forward(15)

t.left(150)   #started backward journey of mouth
t.forward(25)
t.left(30)
t.forward(10)
t.left(60)
t.forward(33)
t.left(90)
t.forward(10)
t.right(90)
t.forward(20)
t.right(90)
t.forward(10)
t.left(90)
t.forward(33)
t.left(60)
t.forward(10)
t.left(30)
t.forward(27)            #completed backward journey
#t.end_fill()            #mouth mein colour bhar diya

t.left(150)
t.forward(16)
t.right(150)   #upward arrow
#t.pencolor("green")
t.forward(10)
t.left(90)
t.forward(80)
t.left(90)
t.forward(10)
t.right(150)
t.forward(70)

t.right(10)
t.forward(20)
t.color("#950602","red")  #Left_ear work
t.begin_fill()
t.right(20)
t.forward(60)  #ear length
t.left(150)
t.forward(20)  #ear width
t.left(30)
t.forward(30)   #ear edge
t.left(30)
t.forward(20)
t.end_fill()
t.left(150)
#t.penup()
t.forward(70)
#t.pendown()  #curser back to the original position
                 #Done ear left
t.forward(5)
#Kavati Mahakay Prarambha
#t.color("#950602","#00ffff")
#t.begin_fill()

t.forward(60)

t.right(25)
t.forward(20)  #1
t.right(20)
t.forward(20)  #2
t.right(15)
t.forward(25)  #3
t.right(15)
t.forward(20)  #4
t.right(10)
t.forward(20)  #5

t.right(10)
t.forward(20)  #5
t.right(15)
t.forward(20)  #4
t.right(10)
t.forward(25)  #3
t.right(15)
t.forward(20)  #2
t.right(20)
t.forward(20)  #1
t.right(25)            #curve part is DONE here

t.left(0)
t.forward(130)  #came at right corner
t.color("#950602","red")  #right_ear work
t.begin_fill()
t.left(150)
t.forward(20)
t.left(30)
t.forward(30)
t.left(30)
t.forward(20)  #done with the right ear
t.end_fill()
t.penup()
t.left(150)
t.forward(60)
t.right(160)
t.forward(25)
t.pendown()  #corner position

t.pensize(2)
t.color("#950602","white")  #right eye
t.begin_fill()
t.left(80)
t.forward(58)
t.left(90)
t.forward(15)
t.left(90)
t.forward(50)
t.left(90)
t.forward(15)
t.end_fill()
t.penup()
t.left(90)
t.forward(50)
t.right(10)
t.forward(37)
t.pendown()

t.pensize(2)
t.color("#950602","white")
t.begin_fill()
t.right(10)
t.forward(50)
t.left(90)
t.forward(15)
t.left(90)
t.forward(50)
t.left(90)
t.forward(15)
t.end_fill()
t.hideturtle()

turtle.exitonclick()