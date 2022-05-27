from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import waitKey
import mysql.connector
import cv2
import os
import  numpy as np
from  datetime import datetime
import tkinter



class Face_Recognition:
    
         
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Face Recognition process')
        
        # <======================================title=====================>
        
        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1380,height=43)
       
        #  rigth image
        
        img_left=Image.open("images/face1.JPEG")
        img_left=img_left.resize((650,700),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.pack()       
        f_lbl.place(x=0,y=45,width=650,height=700)
        
        # ryt imag
         
        img_ryt=Image.open("images/face2.JPG")
        img_ryt=img_ryt.resize((800,720),Image.ANTIALIAS)
        self.photoimg_ryt=ImageTk.PhotoImage(img_ryt)
        f_lbl=Label(self.root,image=self.photoimg_ryt)
        f_lbl.pack()       
        f_lbl.place(x=600,y=45,width=800,height=720)
        
        
        # button for recognize
        btn =Button(f_lbl,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="white")
        btn.place(x=230,y=460,width=500,height=40)
        
        
        # button for exit
        btnexit =Button(f_lbl,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",20,"bold"),bg="red",fg="white")
        btnexit.place(x=230,y=560,width=500,height=40)
        
        
        
       
                
        # <================face recognition==========================================>
        
        
    def face_recog(slef):
        def draw_boundary(img,classifier,Scalefactor,minNeighbors,color,text,clf):
            
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,Scalefactor,minNeighbors)
            
            
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                
                # predict confindence
                confidence=int((100*(1-predict/300)))
                
                # <============connecting to database===================================>
                
                
                conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor(buffered=True)
                
                # conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
                # my_cursor=conn.cursor(buffered=True)
                
                
                my_cursor.execute("select Name  from student where Student_id="+str(id)) 
                n=my_cursor.fetchone()
                n="+".join(n)
                
                
                my_cursor.execute("select Dep  from student where Student_id="+str(id))  
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))  
                r=my_cursor.fetchone()
                r="+".join(r)
        
              
                 
                 
                if confidence>77:
                    
                    
                    cv2.putText(img,f"Roll No :{r}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name :{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    
                    
                    
                    
                    with open('attendence_sheet.csv','r+',newline='\n') as f:
                       mydatalist=f.readlines()
                       name_list=[]
                       for line in mydatalist:
                         entry=line.split(",")
                         name_list.append(entry[0])
                       if((r not in name_list)and (n not in name_list) and (d not in name_list) ):
                          now=datetime.now()
                          d1=now.strftime("%d/%m/%Y")
                          dtstring=now.strftime("%H:%M:%S")
                          f.writelines(f"\n{n},{d},{r},{dtstring},{d1},Present")    
                else :
                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                     cv2.putText(img,"Unknown Face",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,255),3)
                          
         
                coord=[x,y,w,h]
            return coord
              
        def recognize(img,clf,faceCascade):
         coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
         return img
            
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        
        # <==============reading the trained file which contains images==========================>
        clf.read("classifier.xml")
    
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face recognization",img)   
            
            if cv2.waitKey(1)==13:
               break
        video_cap.release()
     
        cv2.destroyAllWindows(1)
            
      
    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this page",parent=self.root)
      if self.iExit>0:
        self.root.destroy()
      else:
         return  
                  
        
        
        
        
        
        
        
        
      

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
         