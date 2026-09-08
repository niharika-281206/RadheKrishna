import cv2
import numpy as np
import turtle


image_path = 'radha.jpg'
img = cv2.imread(image_path)

if img is None:
    print("Error: 'radha.jpg' nahi mili! Check karein ki photo sahi folder me hai.")
    exit()



width, height = 600, 600
img = cv2.resize(img, (width, height))



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 60, 150)


contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


screen = turtle.Screen()
screen.setup(width=750, height=750)
screen.bgcolor("black")
screen.title("Python Color Sketch Drawing")
turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)          
t.hideturtle()      
t.shape("classic")  
t.showturtle()
t.pensize(2)

screen.tracer(2)

print("Drawing start ho rahi hai...")

for cnt in contours:
    if len(cnt) < 8:  
        continue
        
    t.penup()
    first_pt = cnt[0][0]
    
    
    b, g, r = img[first_pt[1], first_pt[0]]
    
    
    if r < 40 and g < 40 and b < 40:
        t.pencolor(0, 200, 255)  # Cyan/Blue
    else:
                t.pencolor(min(int(r * 1.3), 255), min(int(g * 1.3), 255), min(int(b * 1.3), 255))
    
    
    start_x = first_pt[0] - width // 2
    start_y = height // 2 - first_pt[1]
    
    t.goto(start_x, start_y)
    t.pendown()
    
    for pt in cnt[1:]:
        x = pt[0][0] - width // 2
        y = height // 2 - pt[0][1]
        t.goto(x, y)

print("Drawing Complete!")
turtle.done()