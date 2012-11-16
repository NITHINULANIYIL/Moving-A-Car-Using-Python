
from Tkinter import *
import Tkinter as tk
class Carcontrol(Frame):
	def __init__(self,name):
		Frame.__init__(self,bg='white')
		self.pack(expand=YES,fill=BOTH)
		self.master.title("Control the CAR")		

		f=Frame(self,width=500,height=500,bg='white')
		f.pack()
		
		self.f1=Frame(f)
		self.f1.pack(side=TOP,padx=10,pady=10)
		f2=Frame(f)
		f2.pack(side=TOP)

		self.w=Canvas(self.f1)
		self.w.canvasx ( 500, gridspacing=None )
		self.w.canvasy ( 500, gridspacing=None )
		self.p=self.w.create_polygon( 50,50,100,50,125,75,25,75,fill="green")
		self.r=self.w.create_rectangle(10,75,140,100,fill="red")
		self.o1=self.w.create_oval(20,95,45,125,fill="black")
		self.o2=self.w.create_oval(105,95,130,125,fill="black")
		self.w.pack()
		
		b1=Button(f2,text="LEFT",command=self.left)
		b1.pack(side=LEFT)
	
		b2=Button(f2,text="RIGHT",command=self.right)
		b2.pack(side=RIGHT)

	def left(self):
		print "left"
		self.w.move(self.p,-10,0)
		self.w.move(self.r,-10,0)
		self.w.move(self.o1,-10,0)
		self.w.move(self.o2,-10,0)
		
	def right(self):
		print "right"
		self.w.move(self.p,10,0)
		self.w.move(self.r,10,0)
		self.w.move(self.o1,10,0)
		self.w.move(self.o2,10,0)
		
def main():
	Carcontrol("").mainloop()

if __name__=="__main__":
	main()

