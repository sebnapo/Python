from tkinter import *

def segment(A,B,canvas):
    if((abs(A[0] - B[0]) < 0.1) and (abs(A[1] - B[1]) < 0.1)):
        canvas.create_line(A[0],A[1],B[0],B[1], width = 1,fill="black")
        return 0
    C = ((A[0] + B[0])/2,(A[1] + B[1])/2)
    print(C)
    segment(A,C,canvas)
    segment(C,B,canvas)



Xa = float(input("Coordonée en x de A"))
Ya = float(input("Coordonée en y de A"))
Xb = float(input("Coordonée en x de B"))
Yb = float(input("Coordonée en y de B"))

A = (Xa,Ya)
B = (Xb,Yb)

window = Tk()
w = Canvas(window,width = 200, height = 100)
w.pack()

segment(A,B,w)
mainloop()
