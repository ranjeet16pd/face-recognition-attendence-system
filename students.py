from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Students:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Students')
        
        
        
        # <------------------creating the variable--------------------------------->
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
      
        self.var_dob=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
          # first image
        
        img=Image.open("images/st1.JFIF")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.pack()       
        f_lbl.place(x=0,y=0,width=500,height=160)
        
        # second image
        
        img1=Image.open("images/st2.JFIF")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.pack()       
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        # 3rd image
        
        img2=Image.open("images/st3.PNG")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.pack()       
        f_lbl.place(x=1000,y=0,width=500,height=130)
          
        
        
        #background color
        
        img3=Image.open("images/stbg1.JPG")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.pack()       
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-200,y=0,width=1680,height=43)
        
        # main frame
        main_frame=Frame(bg_img,bd=2,bg="pink")
        # main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=9,y=45,width=1335,height=680)
        
        # left frame level
        left_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Students details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width="630",height=550)
        
        img_left=Image.open("images/stclass1.JPG")
        img_left=img_left.resize((600,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.pack()       
        f_lbl.place(x=3,y=4,width=617,height=130)
        
        
        # current  course
        left_frame_course=LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text=" Current Course Detail",font=("times new roman",12,"bold"))
        left_frame_course.place(x=7,y=130,width="620",height=110)
        
        # department
        dep_lbl=Label(left_frame_course, text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_com=ttk.Combobox(left_frame_course, textvariable=self.var_dep, font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_com["values"]=("Select Department ","ECE","Computer science ","Civil","Mechenical","Electrical")
        dep_com.current(0)
        dep_com.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # course
        cour_lbl=Label(left_frame_course,text="Courses",font=("times new roman",12,"bold"),bg="white")
        cour_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        cour_com=ttk.Combobox(left_frame_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        cour_com["values"]=("Select Course ","B.tech","BE ","Phd")
        cour_com.current(0)
        cour_com.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        # Year
        year_lbl=Label(left_frame_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        year_com=ttk.Combobox(left_frame_course,textvariable=self.var_year, font=("times new roman",12,"bold"),width=17,state="readonly")
        year_com["values"]=("Select Year","2022-23","2023-24 ","2024-25","2025-26","2026-27")
        year_com.current(0)
        year_com.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        sem_lbl=Label(left_frame_course,  text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_com=ttk.Combobox(left_frame_course,textvariable=self.var_semester, font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_com["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_com.current(0)
        sem_com.grid(row=1,column=3,padx=3,pady=10,sticky=W)
        
        
        
        # class student information 
        
        left_frame_stud=LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text=" Class Students information ",font=("times new roman",12,"bold"))
        left_frame_stud.place(x=7,y=235,width="615",height=290)
        
        # student id
        stuid_lbl=Label(left_frame_stud,text="StudentID: ",font=("times new roman",12,"bold"),bg="white")
        stuid_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studid_entry=ttk.Entry(left_frame_stud,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
    
        # Name
        name_lbl=Label(left_frame_stud,text="Name:",font=("times new roman",12,"bold"),bg="white")
        name_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        name_entry=ttk.Entry(left_frame_stud, textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        # Class division
        div_lbl=Label(left_frame_stud,text="Section:",font=("times new roman",12,"bold"),bg="white")
        div_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
         
        div_com=ttk.Combobox(left_frame_stud, textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
        div_com["values"]=("A","B","C","D","E")
        div_com.current(0)
        
        div_com.grid(row=1,column=1,padx=10,pady=5,sticky=W)
      
        
        # roll no
        roll_lbl=Label(left_frame_stud,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
    
        
        sroll_entry=ttk.Entry(left_frame_stud, textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        sroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        # Gender
        gender_lbl=Label(left_frame_stud,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_com=ttk.Combobox(left_frame_stud, textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_com["values"]=("Male","Female","other")
        gender_com.current(0)
        gender_com.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
       
        
        
        # Dob
        dob_lbl=Label(left_frame_stud,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry=ttk.Entry(left_frame_stud,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Email
        email_lbl=Label(left_frame_stud,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        email_entry=ttk.Entry(left_frame_stud,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #phone no
        phone_lbl=Label(left_frame_stud,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(left_frame_stud,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #Adderess
        address_lbl=Label(left_frame_stud,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_lbl.grid(row=4,column=0,padx=8,pady=5,sticky=W)
        
        address_entry=ttk.Entry(left_frame_stud,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
      
        #Profesor  name
   
        teacher_lbl=Label(left_frame_stud,text="Prof. Name",font=("times new roman",12,"bold"),bg="white")
        teacher_lbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(left_frame_stud,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        # radio button
        
        self.var_radio1=StringVar() 
        rbtn1=Radiobutton(left_frame_stud,variable=self.var_radio1,text="take sample",value="yes")
        rbtn1.grid(row=5,column=0)
  

        # radio button 
      
        rbtn2=Radiobutton(left_frame_stud,variable=self.var_radio1, text="No sample", value="no")
        rbtn2.grid(row=5,column=1)
        
        
        # button frame
        
        btn_frame=Frame(left_frame_stud,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=205,width=615,height=100)
        
        
        # <=====SAVE BUTTON FOR SAVE THE DATA==============>
        save_btn=Button(btn_frame,text="Save", command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0) 
        
        
        # <============UPDATE BUTTON FOR UPDATE THE DATA OF EXISTING PERSON==============>
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        
      #  <================DELETE BUTTON FOR DELETE THE DATA==============>
        del_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=14,font=("times new roman",13,"bold"),bg="red",fg="white")
        del_btn.grid(row=0,column=3)
        
        
        # <==========RESET BUTTON==============>
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,  width=16,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=4)
        
        
        btn_frame1=Frame(left_frame_stud,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=233,width=615,height=30)
        
        # <===========for taking sample of photos==========>
        takepic_btn=Button(btn_frame1, text="Take Photo",command=self.generate_dataset, width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        takepic_btn.grid(row=0,column=0)
        
        # <=============for updating sample of photos==============>
        update_btn1=Button(btn_frame1,text="Update photo Sample ",command=self.generate_dataset, width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn1.grid(row=0,column=1)
        
        
      
        # right frame level
        ryt_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Students details",font=("times new roman",12,"bold"))
        ryt_frame.place(x=670,y=10,width="660",height=540)
        
        
        img_ryt=Image.open("images/stclass2.JPG")
        img_ryt=img_ryt.resize((650,200),Image.ANTIALIAS)
        self.photoimg_ryt=ImageTk.PhotoImage(img_ryt)
        f_lbl=Label(ryt_frame,image=self.photoimg_ryt)
        f_lbl.pack()       
        f_lbl.place(x=4,y=9,width=650,height=200)
        

        # <===============table==========>
        
        table_frame=Frame(ryt_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=8,y=220,width=638,height=290)
        
        scrool_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrool_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
                                                                                                                          
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        
        
        
        
        scrool_x.config(command=self.student_table.xview)
        scrool_y.config(command=self.student_table.yview)
        self.student_table.heading("dep",text="Department")
        
        
        # <================for adding the table heading============================>
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        # <=============for setting width============>
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
    
    
      # conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
      #       my_curr=conn.cursor(buffered=True)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
#     # <---------------function decelation for  data add-------------------------------->
    
    def add_data(self):
      if self.var_dep.get()=="Select department" or self.var_std_name.get()=="" or self.var_std_id=="":
       messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
       
           try:
           
            conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
            my_curr=conn.cursor(buffered=True)
            
            # conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
            # my_curr=conn.cursor(buffered=True)
            
            my_curr.execute("insert into  student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                              self.var_dep.get(),
                                                              self.var_course.get(),
                                                              self.var_year.get(),
                                                              self.var_semester.get(),
                                                              self.var_std_id.get(),
                                                              self.var_std_name.get(),
                                                              self.var_div.get(),
                                                              self.var_roll.get(),
                                                              self.var_gender.get(),
                                                              self.var_dob.get(),
                                                              self.var_email.get(),
                                                             
                                                              self.var_phone.get(),
                                                              self.var_address.get(),
                                                              self.var_teacher.get(),
                                                              self.var_radio1.get()
                                                              
                                                            
                
                                                          ))
                                    
              
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","students details has been added Successfully ",parent=self.root)
        
        
        # <===================showing error in any wrong input is filled===========>
           except Exception as es:
             messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
            
      
#       # <----------------fetching  data from databse to table------------------------------>
      
      
    def fetch_data(self):
        
         conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
         my_curr=conn.cursor(buffered=True)
         
        #  conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
        #  my_curr=conn.cursor(buffered=True)
         
         my_curr.execute("select * from student")
         data=my_curr.fetchall()
         
         
         if len(data)!=0:
               self.student_table.delete(*self.student_table.get_children())
               for i in data:
                     self.student_table.insert("",END,values=i)
                
         conn.commit()
         conn.close()
         
         
         
#     # <----------------------------------get cursor-----------------------
    
    def get_cursor(self,event=""):
          cursor_focus=self.student_table.focus()
          content=self.student_table.item(cursor_focus)
          data=content["values"]
   
          self.var_dep.set(data[0]),
          self.var_course.set(data[1]),
          self.var_year.set(data[2]),
          self.var_semester.set(data[3]),
          self.var_std_id.set(data[4]),
          
          self.var_std_name.set(data[5]),
          self.var_div.set(data[6]),
          self.var_roll.set(data[7]),
          self.var_gender.set(data[8]),
          self.var_dob.set(data[9]),
          self.var_email.set(data[10]),
          self.var_phone.set(data[11]),
          self.var_address.set(data[12]),
          self.var_teacher.set(data[13]),
          self.var_radio1.set(data[14]),
            
                             
#      <---------------update function----------------------------->

    def update_data(self):
         if self.var_dep.get()=="Select department" or self.var_std_name.get()=="":
          messagebox.showerror("Error","All fields are required",parent=self.root)
         else :
               try:
                   update=messagebox.askyesno("Update","Do you want to update the students detail",parent=self.root)
                   if update>0:
                         conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
                         my_curr=conn.cursor(buffered=True)
                         
                        #  conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
                        #  my_curr=conn.cursor(buffered=True)
                         
                         
                         my_curr.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,photoSample=%s where Student_id=%s"  ,(
                         
                           #  conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
                          #  my_curr=conn.cursor(buffered=True)
                         
                                                                                                                           
                                                              self.var_dep.get(),
                                                              self.var_course.get(),
                                                              self.var_year.get(),
                                                              self.var_semester.get(),
                                                              self.var_std_name.get(),
                                                              self.var_div.get(),
                                                              self.var_roll.get(),
                                                              self.var_gender.get(),
                                                              self.var_dob.get(),
                                                              self.var_email.get(),
                                                              self.var_phone.get(),
                                                              self.var_address.get(),
                                                              self.var_teacher.get(),
                                                              self.var_radio1.get(),
                                                              self.var_std_id.get()
                                                                                      
                                                                                                                           
                           
                           
                           
                           
                           
                           
                                                                                                                           ))
                   else:
                         if not update:
                               return 
                              
                          
                 
                   messagebox.showinfo("Success","student details successfully update completed",parent=self.root)
                   conn.commit()
                   self.fetch_data()
                   conn.close()
          
               except Exception as es:
                 messagebox.showerror("Error",f"due to {str(es)}",parent=self.root)
                 
           
     
     
#     # <------------------------------------------delete data-------------------------------->
    def delete_data(self):
            if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student Id no must be required",parent=self.root)
            else :
                   try:
                       delete=messagebox.askyesno("Student Delete page","Do you really wnat to delte this studet ",parent=self.root)
                       if delete>0:
                           
                            
                            conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
                            my_curr=conn.cursor(buffered=True)
                            
                            # conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
                            # my_curr=conn.cursor(buffered=True)
                            
                            
                            sql="delete from student where Name=%s"
                            val=(self.var_std_name.get(),)
                            my_curr.execute(sql,val)
                       else:
                         if not delete:
                            return
                                  
                       conn.commit()
                       self.fetch_data()
                       conn.close()                                                                                                                                                                                             
                       messagebox.showinfo("delete","successfully deleted student details",parent=self.root)
                
                   except Exception as es:
                        messagebox.showerror("Error",f"due to {str(es)}",parent=self.root)
                  
                        
                      
                    
    
#     #  <---------------------------reset--------------------------------->
    def reset_data(self):
         self.var_dep.set("Select department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("")
         self.var_roll.set("")
         self.var_gender.set("")
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")
     
#         #  <------------generate data set--------------------------->
    
    
    def generate_dataset(self):
          if self.var_dep.get()=="Select Department " or self.var_roll.get()=="" :
                messagebox.showerror("Error ","All Fields are required ",parent=self.root)
          else:
                try:
                  conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",user="sql6494949",password="1ZQ9x3RNIi",database="sql6494949",auth_plugin="mysql_native_password")
                  my_cursor=conn.cursor(buffered=True)
                  
                  # conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit123@.",database="face_recognition",auth_plugin="mysql_native_password")
                  # my_cursor=conn.cursor(buffered=True)
                  
                  my_cursor.execute("select * from student")  
                  myresult=my_cursor.fetchall()
                  id=0
                  for x in myresult:
                        id+=1
                        
                        
                  my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,photoSample=%s where Student_id=%s"  ,(
                                                                                                                           
                                                              self.var_dep.get(),
                                                              self.var_course.get(),
                                                              self.var_year.get(),
                                                              self.var_semester.get(),
                                                              self.var_std_name.get(),
                                                              self.var_div.get(),
                                                              self.var_roll.get(),
                                                              self.var_gender.get(),
                                                              self.var_dob.get(),
                                                              self.var_email.get(),
                                                              
                                                              self.var_phone.get(),
                                                              self.var_address.get(),
                                                              self.var_teacher.get(),
                                                              self.var_radio1.get(),
                                                              self.var_std_id.get()==id+1
                                                                                                                      ))
                                                                                                                  
                                                                                                                            
                  
                  conn.commit()
                  self.fetch_data()
                  self.reset_data()
                  conn.close()
                  
                  # <-------------------load predefined data on face frontals from opencv
                  
                  
                  
                  face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                  
                  def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        
                        # 1.3==> scalling factor 
                        # 5==> minimum neighbour
                        
                        for (x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                                                          
            
                  cap=cv2.VideoCapture(0)
                  img_id=0
                  while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame)  is not None:
                      img_id+=1
                      face=cv2.resize(face_cropped(my_frame),(450,450))
                      face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                      file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                      cv2.imwrite(file_name_path,face)
                      cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                      cv2.imshow("Crooped Face ",face)
                      
                    if cv2.waitKey(1)==13 or int(img_id)==8:
                          break
                        
                  cap.release()
                  cv2.destroyAllWindows()
                  messagebox.showinfo("Result","Genrating data sets copmlited !!!!!")
                  
                
                except Exception as es:
                        messagebox.showerror("Error",f"due to {str(es)}",parent=self.root)
                     
                                   


if __name__=="__main__":
    root=Tk()
    obj=Students(root)
    root.mainloop()
       