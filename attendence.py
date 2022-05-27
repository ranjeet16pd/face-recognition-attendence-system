from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata=[]


class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Attendence Data')

     
        
        #<=================================making text variable================================>
        
     
        self.var_roll=StringVar()
        self.var_dep=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_name=StringVar()
        self.var_atten_status=StringVar()
        
        
        
        
        
        img=Image.open("images/st1.JFIF")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.pack()       
        f_lbl.place(x=0,y=0,width=500,height=160)
        
        #second image
        
        img1=Image.open("images/st2.JFIF")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.pack()       
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #3rd image
        
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
        
        title_lbl=Label(bg_img,text="ATTENDENCE DETAILS",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=-90,y=0,width=1680,height=43)
        
        # main frame
        main_frame=Frame(bg_img,bd=2,bg="pink")
        # main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=9,y=45,width=1335,height=580)
        
        # left frame level
        left_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Students Attendence  details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width="630",height=480)
        
        img_left=Image.open("images/stclass1.JPG")
        img_left=img_left.resize((600,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.pack()       
        f_lbl.place(x=3,y=4,width=617,height=130)
        
        
        
        left_frame_details=LabelFrame(left_frame,bd=3,bg="white",relief=RIDGE,text=" Current Course Detail",font=("times new roman",12,"bold"))
        left_frame_details.place(x=7,y=130,width="620",height=280)
        
        # labelland entry
        
        
        #time
        attendecetime_lbl=Label(left_frame_details,text="Time ",font=("times new roman",12,"bold"),bg="white")
        attendecetime_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        attendecetime_entry=ttk.Entry(left_frame_details,width=20,textvariable=self.var_time,font=("times new roman",12,"bold"))
        attendecetime_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        # roll
        attendeceroll_lbl=Label(left_frame_details,text="Roll no ",font=("times new roman",12,"bold"),bg="white")
        attendeceroll_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    
        attendeceroll_entry=ttk.Entry(left_frame_details,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        attendeceroll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # name
        attendecetime_lbl=Label(left_frame_details,text="Name",font=("times new roman",12,"bold"),bg="white")
        attendecetime_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        attendecetime_entry=ttk.Entry(left_frame_details,width=20,textvariable=self.var_name,font=("times new roman",12,"bold"))
        attendecetime_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # date
        attendecedate_lbl=Label(left_frame_details,text="Date",font=("times new roman",12,"bold"),bg="white")
        attendecedate_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        attendecedate_entry=ttk.Entry(left_frame_details,width=20,textvariable=self.var_date,font=("times new roman",12,"bold"))
        attendecedate_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
       
    #    attendence 
        attendece_lbl=Label(left_frame_details,text="Attendence Status",font=("times new roman",12,"bold"),bg="white")
        attendece_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
           
        attendence_com=ttk.Combobox(left_frame_details,textvariable=self.var_atten_status,font=("times new roman",12,"bold"),width=17,state="readonly")
        attendence_com["values"]=("PRESENT","ABSENT")
        attendence_com.current(0)
        attendence_com.grid(row=2,column=1,padx=10,pady=5,sticky=W)
      
        #  department
      
        attendecedep_lbl=Label(left_frame_details,text="Depart",font=("times new roman",12,"bold"),bg="white")
        attendecedep_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)
    
        attendecedep_entry=ttk.Entry(left_frame_details,width=20,textvariable=self.var_dep,font=("times new roman",12,"bold"))
        attendecedep_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
         
        # button frame
        
        btn_frame=Frame(left_frame_details,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=205,width=615,height=100)
        
        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv, width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0) 
        
        
        export_btn=Button(btn_frame,text="export csv",command=self.exportcsv,width=20,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)
        

        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,  width=20,font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        
        # right frame level
        
        ryt_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Attendence Details ",font=("times new roman",12,"bold"))
        ryt_frame.place(x=670,y=15,width="720",height="480")
        
        
    #  =====================scroll bar table========================
       
        table_frame=Frame(ryt_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=8,y=13,width=638,height=420)
        
        scrool_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrool_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
    
        self.Attendencetable=ttk.Treeview(table_frame,column=("name","department","roll","time","date","attendence"),xscrollcommand=scrool_x.set,yscrollcommand=scrool_y.set)
        scrool_x.pack(side=BOTTOM,fill=X)
        scrool_y.pack(side=RIGHT,fill=Y)
        
        scrool_x.config(command=self.Attendencetable.xview)
        scrool_y.config(command=self.Attendencetable.yview)
    
        # self.Attendencetable.heading("id",text="AttendenceId")
        
        self.Attendencetable.heading("roll",text="Rollno")
        self.Attendencetable.heading("name",text="Name")
        
        self.Attendencetable.heading("department",text="Department")
        self.Attendencetable.heading("time",text="Time")
        self.Attendencetable.heading("date",text="Date")
        self.Attendencetable.heading("attendence",text="Attedence")
        self.Attendencetable["show"]="headings"
        
        
        # self.Attendencetable.column("id",width=100)
        self.Attendencetable.column("roll",width=100)
        self.Attendencetable.column("name",width=100)
        self.Attendencetable.column("department",width=100)
        self.Attendencetable.column("time",width=100)
        self.Attendencetable.column("date",width=100)
        self.Attendencetable.column("attendence",width=100)
    
        
        self.Attendencetable.pack(fill=BOTH,expand=1)
        self.Attendencetable.bind("<ButtonRelease>",self.get_cursor)
        
    #  <=================fetching data============================>
    
    def fetchData(self,rows):
        self.Attendencetable.delete(*self.Attendencetable.get_children())
        for i in rows:
            self.Attendencetable.insert("",END,values=i)
      
      
            
     # <==========import csv======================>
            
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
                
    # <==========Export csv======================>
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data Found",parent=self.root)
                return False
                
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetype=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
             exp_write=csv.writer(myfile)
             for i in mydata:
                 exp_write.writerow(i)
                 messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+"successfully")  
           
                
        except Exception as es:
            messagebox.showerror("Error",f"due to {str(es)}",parent=self.root)
                     
    
    # <======fill box using table=====================>
    
    def get_cursor(self,event=""):
        cursor_row=self.Attendencetable.focus()
        content=self.Attendencetable.item(cursor_row)
        rows=content['values']
     
        self.var_name.set(rows[0]) 
        self.var_dep.set(rows[1]) 
        self.var_roll.set(rows[2])
        self.var_time.set(rows[3]) 
        self.var_date.set(rows[4]) 
        self.var_atten_status.set(rows[5]) 
        
    # <=================resetdata===========================>
        
    
    def  reset_data(self,event=""):
        cursor_row=self.Attendencetable.focus()
        content=self.Attendencetable.item(cursor_row)
        rows=content['values']
     
        self.var_name.set("") 
        self.var_dep.set("") 
        self.var_roll.set("")
        self.var_time.set("") 
        self.var_date.set("") 
        self.var_atten_status.set("") 
                                  
          

if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
               