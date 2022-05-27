
from importlib.resources import open_binary
from tkinter import*
from tkinter import ttk
from turtle import right
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from datetime import date 
from time import strftime
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developerdetails import Developer
from helpdesk import Helpdesk
from students import Students
import tkinter

def main():
    win=Tk()
    app=Login_win(win)
    win.mainloop()
    


class Login_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        heading_Frame=Frame(self.root,bg="black")
        heading_Frame.place(x=30,y=46,width=30,height=10)
        
        
        
        
        # <==============placing background pic===============>
        self.bg_img=ImageTk.PhotoImage(file=r"images/loginbgimg.jpg")
        
        lebel_bg=Label(self.root,image=self.bg_img)
        lebel_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        heading_lbl=Label(self.root,text="Welcome to Face Recognition Attendence System",font=("times new roman",39,"bold"),bg="black",fg="white")
        heading_lbl.place(x=0,y=0,width=1380,height=54)
        
        
        # <====creating the frame=============>
        F_rame=Frame(self.root,bg="black")
        F_rame.place(x=515,y=160,width=350,height=460)
        
        
        img_icon=Image.open("images/loginicon.png")
        img_icon=img_icon.resize((100,100),Image.ANTIALIAS)
        self.photoimg_icon=ImageTk.PhotoImage(img_icon)
        f_lbl=Label(self.root,image=self.photoimg_icon)
        f_lbl.pack()       
        f_lbl.place(x=642,y=175,width=100,height=100)
        
        get_started=Label(F_rame,text="Get Started ",font=("times new roman ",20,"bold"),fg="white",bg="black")
        get_started.place(x=95,y=110)

       
       
    #    <======label for username================>
    
        username_lbl=Label(F_rame,text="Username",font=("times new roman ",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=78,y=165)
    
        self.txtuser=ttk.Entry(F_rame,font=("times new roman ",15,"bold"))
        self.txtuser.place(x=40,y=195,width=270)
    # <==========label for password=====> 
    
    
        userpaswrd_lbl=Label(F_rame,text="Password",font=("times new roman ",15,"bold"),fg="white",bg="black")
        userpaswrd_lbl.place(x=78,y=235)
    
        self.txtpaswrd=ttk.Entry(F_rame,show="*",font=("times new roman ",15,"bold"))
        self.txtpaswrd.place(x=40,y=260,width=270)
    
    # setting user name icon===========>
    
        user_icon=Image.open("images/usernameicon.png")
        user_icon=user_icon.resize((30,30),Image.ANTIALIAS)
        self.photouser_icon=ImageTk.PhotoImage(user_icon)
        f_lbl=Label(F_rame,image=self.photouser_icon)
        f_lbl.pack()       
        f_lbl.place(x=40,y=160,width=30,height=30)
 
 
    
        # <===========setting passward icon==============>
        
        passward_icon=Image.open("images/passicon.png")
        passward_icon=passward_icon.resize((25,25),Image.ANTIALIAS)
        self.photopassward_icon=ImageTk.PhotoImage(passward_icon)
        f_lbl=Label(F_rame,image=self.photopassward_icon)  
        f_lbl.pack()       
        f_lbl.place(x=40,y=230,width=25,height=25)
 
# <===================login button================>
        loginbtn=Button(F_rame,command=self.login,text="Login",font=("times new roman ",15,"bold"),bd="3",relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=100,y=300,height=35,width="120")


                 
    #  <===========register  btn================>
        loginbtn=Button(F_rame,text="New user register",command=self.register_win,font=("times new roman ",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        loginbtn.place(x=20,y=350,width="160")
       
                 
    #  <==========forgot passward btn======================>
    
        loginbtn=Button(F_rame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman ",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="red")
        loginbtn.place(x=20,y=380,width="160")
         
         
         
         
   
    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
             
               
                 
    def login(self):
        if self.txtuser.get()=="" or self.txtpaswrd.get()=="":
            messagebox.showerror("Error","all fields are required")
        elif self.txtuser.get()=="rj" and self.txtpaswrd.get()=="rj12":
            messagebox.showinfo("Success","welcome to you")      
        else:
                    
          
           conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
           my_curr=conn.cursor(buffered=True)  
           
        #    conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
        #    my_curr=conn.cursor(buffered=True)
           my_curr.execute("select * from register where email=%s and password=%s",(             
                                                           self.txtuser.get(),
                                                           self.txtpaswrd.get()
                
                
                
                
                                                            ))      
              
              
           row=my_curr.fetchone()
           if row==None:
               messagebox.showerror("Error","Invalid Username and password")
           else :
               open_main=messagebox.askyesno('YesNo',"Want to go to next page")
               if open_main>0:
                   self.new_window=Toplevel(self.root)
                   self.app=face_recognition_system(self.new_window)
               else :
                   if not open_main:
                       return        
           conn.commit()
           conn.close()
                
                
                
                # <=============reset password======================>
           
           
           
           
           
                
    def reset_pass(self):
         if self.combo_sequrity_Q.get()=="Select":
             messagebox.showerror("Error","Select sequrity question ",parent=self.root)
         elif self.seqAns.get()=="":
             messagebox.showerror("Error","Please enter the answer",parent=self.root)
                 
         elif self.newpassword_entry.get()=="":
             messagebox.showerror("Error","Please Enter the new Password",parent=self.root)        
             
         else :
             
             
             
             
             conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
             my_curr=conn.cursor(buffered=True)
             
            #  conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
            #  my_curr=conn.cursor(buffered=True)
            
             query=("select * from register where email=%s and sequrityQ=%s and sequrityA=%s")
             value=(self.txtuser.get(),self.combo_sequrity_Q.get(),self.seqAns.get())
             my_curr.execute(query,value)
             row=my_curr.fetchone()
             if row==None:
                 messagebox.showerror("Error","Please Entre the Correct Answer")
             else :
                 query=("update register set password =%s where email=%s")
                 value=(self.newpassword_entry.get(),self.txtuser.get())    
                 my_curr.execute(query,value)
                 
                 conn.commit()
                 conn.close()
                 messagebox.showinfo("Information","Your password has been reset",parent=self.root)
                 self.root2.destroy()
             
             
             
                
                
                
                
                
                
                
                
        #    <==================forgot passward window===================> 

    def forgot_password_window(self):
        if self.txtuser.get()=="" :
            messagebox.showerror("Error ","Please entre the email address to reset password")
        else :
            conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
            my_curr=conn.cursor(buffered=True)
            
            # conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
            # my_curr=conn.cursor(buffered=True)
            
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_curr.execute(query,value)
            row=my_curr.fetchone()
            
            if row==None:
                messagebox.showerror('My error',"Please enter the valid user name")
                
            else :
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+600+170")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman ",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
               
                sequrityques_lbl=Label(self.root2,text="Select Sequrity Question",font=("times new roman ",13,"bold"),fg="black",bg="white")
                sequrityques_lbl.place(x=48,y=80)
  
                self.combo_sequrity_Q=ttk.Combobox(self.root2,font=("times new roman ",13,"bold"),state="readonly") 
                self.combo_sequrity_Q["values"]=("Select","Your Birth Place ","Your Pet Name","Friend Name")
                self.combo_sequrity_Q.place(x=50,y=110,width=250) 
                self.combo_sequrity_Q.current(0) 
        
                seqAns_lbl=Label(self.root2,text="Sequrity Answer",font=("times new roman ",13,"bold"),fg="black",bg="white")
                seqAns_lbl.place(x=50,y=150)
    
          
                self.seqAns=ttk.Entry(self.root2,font=("times new roman ",13,"bold"))
                self.seqAns.place(x=50,y=180,width=250)

                
                
                newpassword_lbl=Label(self.root2,text="New Password",font=("times new roman ",13,"bold"),fg="black",bg="white")
                newpassword_lbl.place(x=50,y=220)
                self.newpassword_entry=ttk.Entry(self.root2,show="*",font=("times new roman ",13,"bold"))
                self.newpassword_entry.place(x=50,y=250,width=250)
            
                btn=Button(self.root2,text="Reset ",command=self.reset_pass,font=("times new roman ",13,"bold"),fg="white",bg="green")
                btn.place(x=120,y=290)





class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")
        
        
        
        
        
        
        
        # <==================creating the variables=======================>
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_sequrityQ=StringVar()
        self.var_sequrityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
      # <==============placing background pic===============>
        self.bg_img=ImageTk.PhotoImage(file=r"images/loginbgimg.jpg")
        
        lebel_bg=Label(self.root,image=self.bg_img)
        lebel_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        
        # <====creating the frame=============>
        F_rame=Frame(self.root,bg="white")
        F_rame.place(x=320,y=80,width=750,height=560)
        
        
        get_started=Label(F_rame,text="Register Here ",font=("times new roman ",28,"bold"),fg="blue",bg="white")
        get_started.place(x=25,y=30)

        
            # <======label for firstname================>
        fname_lbl=Label(F_rame,text="First Name",font=("times new roman ",13,"bold"),fg="black",bg="white")
        fname_lbl.place(x=48,y=95)
    
        fname_entry=ttk.Entry(F_rame,textvariable=self.var_fname,font=("times new roman ",13,"bold"))
        fname_entry.place(x=48,y=125,width=250)
       
           
         # <======label for lasttname================>
        lastname_lbl=Label(F_rame,text="Last Name",font=("times new roman ",13,"bold"),fg="black",bg="white")
        lastname_lbl.place(x=400,y=98)
    
        lastname_entry=ttk.Entry(F_rame,textvariable=self.var_lname,font=("times new roman ",13,"bold"))
        lastname_entry.place(x=400,y=125,width=250)
        
        
            # <======label for contact no.================>
        contact_lbl=Label(F_rame,text="Contact No.",font=("times new roman ",13,"bold"),fg="black",bg="white")
        contact_lbl.place(x=48,y=165)
    
        contact_entry=ttk.Entry(F_rame,textvariable=self.var_contact,font=("times new roman ",13,"bold"))
        contact_entry.place(x=48,y=195,width=250)
               


 
            # <======label for Email================>
        emaillbl=Label(F_rame,text="Email",font=("times new roman ",13,"bold"),fg="black",bg="white")
        emaillbl.place(x=400,y=165)
    
        email_entry=ttk.Entry(F_rame,textvariable=self.var_email,font=("times new roman ",13,"bold"))
        email_entry.place(x=400,y=195,width=250)
        
                 
 
            # <======label for sequrity question================>
        sequrityques_lbl=Label(F_rame,text="Select Sequrity Question",font=("times new roman ",13,"bold"),fg="black",bg="white")
        sequrityques_lbl.place(x=48,y=235)
  
        self.combo_sequrity_q=ttk.Combobox(F_rame,textvariable=self.var_sequrityQ,font=("times new roman ",13,"bold"),state="readonly") 
        self.combo_sequrity_q["values"]=("Select","Your Birth Place ","Your Pet Name","Friend Name")
        self.combo_sequrity_q.place(x=48,y=265,width=250) 
        self.combo_sequrity_q.current(0)
               
         # <======label for sequrity ans================>
        seqAns_lbl=Label(F_rame,text="Sequrity Answer",font=("times new roman ",13,"bold"),fg="black",bg="white")
        seqAns_lbl.place(x=400,y=235)
    
        seqAns_entry=ttk.Entry(F_rame,textvariable=self.var_sequrityA,font=("times new roman ",13,"bold"))
        seqAns_entry.place(x=400,y=265,width=250)
        
                      
            # <======label for pasward================>
        password_lbl=Label(F_rame,text="Password",font=("times new roman ",13,"bold"),fg="black",bg="white")
        password_lbl.place(x=48,y=310)
    
        password_entry=ttk.Entry(F_rame,textvariable=self.var_pass,font=("times new roman ",13,"bold"),show="*")
        password_entry.place(x=48,y=340,width=250)
            
            
               
         # <======label for confier pasward================>
        sequconfrirm_password_lbl=Label(F_rame,text="Confirm Password",font=("times new roman ",13,"bold"),fg="black",bg="white")
        sequconfrirm_password_lbl.place(x=400,y=310)
    
    
        confrirm_password_entry=ttk.Entry(F_rame,textvariable=self.var_confpass,font=("times new roman ",13,"bold"),show="*")
        confrirm_password_entry.place(x=400,y=340,width=250)
        
                      
        # <=========creating check button=================>
        
        self.var_check=IntVar()
        
        check_btn=Checkbutton(F_rame,variable=self.var_check,text="I Agree All Terms and Condition",font=("times new roman ",10,"bold"),onvalue=1,offvalue=0) 
        check_btn.place(x=40,y=380)        
         
         
         
        #  >=============Register btn===================>
        b1=Button(F_rame,command=self.register_data,text="Register Now",borderwidth=0,cursor="hand2",font=("times new roman ",10,"bold"),fg="black",bg="gray")
        b1.place(x=45,y=440,width=100,height=40)
           
         
         
           
         
         
           
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_sequrityQ.get()=="Select":
            messagebox.showerror("Error ","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and confirm Password must be same",parent=self.root)
                
        elif self.var_check.get()==0:
             messagebox.showerror("Error","Please agree terms & condition",parent=self.root)
                 
        else:
            conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
            my_curr=conn.cursor(buffered=True)
            
            # conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
            # my_curr=conn.cursor(buffered=True)
            
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_curr.execute(query,value)
            row=my_curr.fetchone()
            if row!=None:
                messagebox.showerror("Error ","User already exist  Plaese try another Email ",parent=self.root)
                
            else :
                my_curr.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                              
                                                              self.var_fname.get(),
                                                              self.var_lname.get(),
                                                              self.var_contact.get(),
                                                              self.var_email.get(),
                                                              self.var_sequrityQ.get(),
                                                              self.var_sequrityA.get(),
                                                              self.var_pass.get()
                                                          
                                                              
                                                              
                                                                                 ))
                               
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully",parent=self.root)
                 
                 
                 
                 
                 



class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('face recognition system')
        
        # #first image
        
        img=Image.open("images/imgg1.JFIF")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.pack()       
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # #second image
        
        img1=Image.open("images/img1.JFIF")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.pack()       
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        # #3rd image
        
        img2=Image.open("images/imgface1.JPG")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.pack()       
        f_lbl.place(x=1000,y=0,width=500,height=130)
          
        # background image
        
        img3=Image.open("images/stbg1.JpG")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.pack()       
        bg_img.place(x=0,y=110,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1380,height=43)
          
          
          
       #    <===================Time=========================>
       
        def time():
               string =strftime("%H:%M:%S %p")
               lbl.config(text=string)
               lbl.after(1000,time)
               
               
        lbl=Label(root,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=40,y=160,width=110,height=50)
        time()  
          
          
         
          #STUDENTS BUTTON(upperbutton)
        img4=Image.open("images/studentsimage.JPG")
        img4=img4.resize((150,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4) 
        
        b1=Button(bg_img,image=self.photoimg4,command=self.students_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=150)
        
        b1_text=Button(bg_img,text="Student Detail",command=self.students_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_text.place(x=200,y=220,width=151,height=30)
        
        # face detection btn
        img5=Image.open("images/face1.JPEG")
        img5=img5.resize((150,150),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5) 
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.facedata)
        b2.place(x=470,y=100,width=150,height=150)
        b2_text=Button(bg_img,text="Mark Attendence",command=self.facedata,   cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=470,y=220,width=151,height=30)
        
        
        img6=Image.open("images/attendencebutton.JPG")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6) 
        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b2.place(x=740,y=100,width=150,height=150)
        b2_text=Button(bg_img,command=self.attendence_data,text="View Atendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=740,y=220,width=151,height=30)
        
        
        img7=Image.open("images/helpbtn.JFIF")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7) 
        b2=Button(bg_img,image=self.photoimg7,command=self.helpdexk_data,cursor="hand2")
        b2.place(x=1020,y=100,width=150,height=150)
        b2_text=Button(bg_img,text="HELPDESK",command=self.helpdexk_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=1020,y=220,width=151,height=30)
        
        
     
          #lowerbutton
          
        img8=Image.open("images/train.JFIF")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8) 
        b1=Button(bg_img,image=self.photoimg8, command=self.train_data, cursor="hand2")
        b1.place(x=200,y=350,width=150,height=150)
        b1_text=Button(bg_img,text="Train Data",command=self.train_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_text.place(x=200,y=470,width=151,height=30)
        
        
        img9=Image.open("images/photoimg.jfif")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9) 
        b2=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b2.place(x=470,y=350,width=150,height=150)
        b2_text=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=470,y=470,width=151,height=30)
        
        
        img10=Image.open("images/developerbutton.jpg")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10) 
        b2=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b2.place(x=740,y=350,width=150,height=150)
        b2_text=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=740,y=470,width=151,height=30)
        
        
        img11=Image.open("images/exitbtn.JFIF")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11) 
        b2=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b2.place(x=1020,y=350,width=150,height=150)
        b2_text=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_text.place(x=1020,y=470,width=151,height=30)
        
        
     
        # <-----------------------------function button--------------------->
      
    def students_details(self):
           self.new_window=Toplevel(self.root)
           self.app=Students( self.new_window)
       
    def train_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Train( self.new_window)
       
    def facedata(self):
       self.new_window=Toplevel(self.root)
       self.app=Face_Recognition( self.new_window)
       
       
    def attendence_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Attendence( self.new_window)
       
    def developer_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Developer( self.new_window)
       
    def helpdexk_data(self):
       self.new_window=Toplevel(self.root)
       self.app=Helpdesk( self.new_window)
       
       
       
       
          
    def open_img(self):
          os.startfile("data")      
      
      
    def iExit(self):
      self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this page",parent=self.root)
      if self.iExit>0:
        self.root.destroy()
      else:
         return  
          
          
          
                                            
                 
                 
                 
                 
                 
if __name__=="__main__":
      main()