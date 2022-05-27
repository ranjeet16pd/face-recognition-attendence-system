# face-recognition-attendence-system


i used python (3.9.7 version)

To Run the Program first install the required library:

(RUN FROM MAIN FILE. the main file is    login.py)

pip3 install opencv-python

pip3 install opencv-contrib-python

pip3 install MySQL-python

pip3 install mysql-connector-python

pip3 install numpy

pip3 install DateTime

pip3 install tk

pip3 install Pillow

pip install pyttsx3

i host the database with online sever by chance if online server is not working then do the following instruction :

so i also provide the two sql file 

(i) face_recognition_studnet.sql 

(ii) face_recognition_register.sql

so just import these sql file in MySQL workbench in your local machine and make a new databse file and give the databse name as (face_recognition).

then go to server->data import now selcect (import from self-contained file) and choose the above sql file location then go to default target schema and select ( face_recognition) and now finally clik on (start import)

DO SAME FOR BOTH FILE

Now in code i connect mysql in two ways online sever and localhost. i just comment the connection with localhost if online server do not work then just uncomment localhost connection and comment online server connection in login.py ,students.py,face_recognition.py file

the localhost connection look like this

conn=mysql.connector.connect(host="localhost",user="root",password="Rnjit",database="face_recognition",auth_plugin="mysql_native_password") my_curr=conn.cursor(buffered=True)

Now finall change the password accorrding to your mysqlworkbench

and then Run
