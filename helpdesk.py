from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('HELP desk')
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1380,height=43)
        
        
        # top images
        img_top=Image.open("images/helpdesk.jpg")
        img_top=img_top.resize((1530,780),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.pack()       
        f_lbl.place(x=0,y=55,width=1530,height=780)
            
         
        
         # emailus
        anyquery_lbl=Label(self.root, text="For any query Email us :",font=("times new roman",29,"bold"),bg="yellow")
        anyquery_lbl.place(x=555,y=300)
        
        email_lbl=Label(self.root, text="ranjeet16pd@gmail.com",font=("times new roman",29,"bold"),bg="yellow")
        email_lbl.place(x=555,y=350)
        
       
          
          

if __name__=="__main__":
    root=Tk()
    obj=Helpdesk(root)
    root.mainloop()
               
        
        
        
        
        
        