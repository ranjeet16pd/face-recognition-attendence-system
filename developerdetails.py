from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Developer Details')
        
        title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1380,height=43)
        
        
        # top images
        img_top=Image.open("images/developer1.jpg")
        img_top=img_top.resize((1530,780),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.pack()       
        f_lbl.place(x=0,y=55,width=1530,height=780)
            
         
        # frame
        
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=830,y=3,width=500,height=600)
        
        img_top1=Image.open("images/ranjeet photo.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
    
        f_lblimg=Label(main_frame,image=self.photoimg_top1)
        f_lblimg.place(x=300,y=0,width=200,height=200)
        
        
         # about
        dev_lbl=Label(main_frame, text="Hello! my name is Ranjeet",font=("times new roman",15,"bold"),bg="white")
        dev_lbl.place(x=15,y=10)
        
        about_lbl=Label(main_frame, text="I am 2nd year student at",font=("times new roman",15,"bold"),bg="white")
        about_lbl.place(x=15,y=40)
        
        collage_lbl=Label(main_frame, text="DTU pursuing ECE.",font=("times new roman",15,"bold"),bg="white")
        collage_lbl.place(x=15,y=70)
        
        
        
        hoby_lbl=Label(main_frame, text="I JUST FALL IN LOVE",font=("times new roman",15,"bold"),bg="white")
        hoby_lbl.place(x=15,y=100)
    
        
        
        LOVE_lbl=Label(main_frame, text="WITH CODE",font=("times new roman",15,"bold"),bg="white")
        LOVE_lbl.place(x=15,y=130)
    
        
        # bottom images
        img_bottom=Image.open("images/programer2.jpg")
        img_bottom=img_bottom.resize((500,400),Image.ANTIALIAS)
        self.photoimg_bottom=img_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(main_frame,image=self.photoimg_bottom)
        f_lbl.pack()       
        f_lbl.place(x=0,y=210,width=500,height=400)
            
        
        

          
          

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
               
        
        
        
        
        
        
        
        
        
        