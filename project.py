import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='dps45',database='orion_hospital')
mycur=con.cursor()

def psignin():
    x=input("Patient ID: ")
    y=input("Password: ")
    try:
        n="select * from p_login where Patient_ID="+x+";"
        mycur.execute(n)
        a=mycur.fetchone()
        if a[0]==x and a[1]==y:
            
            print("==================================================================================================================================")
            print("                                                  LOGGED IN SUCCESSFULLY                                                          ")
            print("==================================================================================================================================")
    except:
        print("ERROR")
        print("PLEASE TRY AGAIN")
        psignin()



def preg():
    n="select * from p_login;"
    mycur.execute(n)
    for i in mycur:
        m=i
    a=int(m[0])
    b=a+1
    name=input("enter name: ")
    g=input("enter your gender: ")
    age=int(input("enter your age: "))
    dob=input("enter your DOB: ")
    bg=input("enter your blood group: ")
    m=input("enter your mobile no.: ")
    e=input("enter your email ID: ")
    y=input("Create Password: ")
    sql="insert into p_login values(%s,%s)"
    c=(b,y)
    mycur.execute(sql,c)
    f="insert into p_details values(%s,%s,%s,%s,%s,%s,%s,%s)"
    d=((b,name,g,age,dob,bg,m,e))
    mycur.execute(f,d)
    con.commit()
    print(" Patient ID : ",b)
    print()
    print()
    print("=======================================================================================================================================")
    print("                                               REGISTERED SUCCESSFULLY                                                                 ")
    print("=======================================================================================================================================")

def dsignin():
    x=input("Doctor ID: ")
    y=input("Password: ")
    try:
        n="select * from dr_login where dr_id="+x+";"
        mycur.execute(n)
        a=mycur.fetchone()
        if a[0]==x and a[1]==y:
            
            print("============================================================================================================================")
            print("                                              LOGGED IN SUCCESSFULLY                                                        ")
            print("============================================================================================================================")
    except:
        print("Error")
        dsignin()


def finddr():
    a= input("Enter Speciality")
    sql="select * from dr_details where speciality=%s"
    mycur.execute(sql,(a,))
    m=mycur.fetchall()

    for i in m:
        print("====================================================================================================================================")
        print(i)
        print("====================================================================================================================================")    


def contact():
    print("========================================================================================================================================")
    print("                                             EMERGENCY CONTACT NUMBER: 106020                                                           ")
    print("========================================================================================================================================")


def feedback():
    print("========================================================================================================================================")
    print("                                                   SHARE YOUR FEEDBACK                                                                  ")
    print("                          We love to hear about our doctors,facilities and your treatment at Orion                                      ")
    print("========================================================================================================================================")
    print()
    print()
    feedback=input("Enter Feedback: ")
    print()
    n=input("Enter Name: ")
    m=input("Enter Mobile Number: ")
    a=input("Enter Email.id: ")
    f=open("feedback.txt","r+")
    l=[n,m,a]
    f.writelines(l)
    f.close()
    print("=======================================================================================================================================")
    print("                                                 THANK YOU FOR YOUR FEEDBACK                                                           ")
    print("=======================================================================================================================================")
    print()
    print()

def payment():
     print("*******************************")
     print("Choose the payment method: ")
     print("******************************")
     print("1.Cash")
     print("2.Debit Card")
     print("3.Credit Card")
     print("4.Online Payment")
     print()
     p=int(input("Please enter your choice : "))
     print()
     print()

    
def hlthckup():
    print("=======================================================================================================================================")
    print("                                                  HEALTH CHECKUP PAKAGES                                                               ")
    print("=======================================================================================================================================")
    print()
    print("                                                1. Advanced Health Check                                                               ")
    print("                                                2. Basic Heath Check                                                                   ")
    print("                                                3. Whole Body Check For Men                                                            ")
    print("                                                4. Women Executive Heath Check                                                         ")
    print("                                                5. Book Checkup                                                                        ")                      
    print()
    print()
    while True:
        n=input("Enter choice to see Features: ")
        if n=="1":
            print("Blood Investigation")
            print("Blood group and Ab Screening")
            print("Hemogram")
            print("Diabetes Health")
            print("Kidney Health")
            print("Heart Health")
            print("Liver Health")
            print("Infection Screening")
            print("Routine Urine Analysis")
            print()
            print()
            print("PRICE - Rs 4000")
        if n=="3":
            print("General Health")
            print("Diabetes Check")
            print("Kidney Health ( RFT )")
            print("Liver Health")
            print("Cardiac Health")
            print("Lung Health")
            print("Body Fat Analysis")
            print("Eye Examination")
            print("Hormone Health")
            print("Bone and Joint Health")
            print("Viral Markers")
            print("Dental Examination")
            print("Cancer Screening")
            print()
            print()
            print("PRICE- Rs 20000")
        
        if n=="2":
            print("Blood Investigation")
            print("Diabetes Health")
            print("Kidney Health ( RFT )")
            print("Heart Health")
            print("Liver Health")
            print("Infection Screening")
            print("Hormone")
            print("Lung Health")
            print("Consultations")
            print("General Health")
            print()
            print()
            print("PRICE- Rs 3000")

        if n=="4":
            print("General Health")
            print("Diabetes Evaluation")
            print("Kidney Profile")
            print("Cardiac Evaluation")
            print("Cancer Screening")
            print("Liver Health")
            print("Nutrition Health")
            print("Lung Health")
            print("Consultations")
            print()
            print()
            print("PRICE-Rs 4000")
            
        if n=="5":
            break
        
    m=input("Do you want to book a health checkup? (y/n): ")
    if m=="y":
        
        c= input("Enter choice(1,2,3,4): ")
        if c=="1":
            p=input("Enter patient id: ")
            n=input("Enter Patient name: ")
            d=input("Enter date for appointment (YYYY-MM-DD): ")
            s="Advanced Health Check"
            sql="insert into healthcheckup values(%s,%s,%s,%s)"
            t=(p,n,s,d)
            mycur.execute(sql,t)
            con.commit()
            print()
            print("Price - Rs 4000")
            payment()
        if c=="2":
            p=input("Enter patient id: ")
            n=input("Enter Patient name: ")
            d=input("Enter date for appointment (YYYY-MM-DD): ")
            s="Basic Heath Check"
            sql="insert into healthcheckup values(%s,%s,%s,%s)"
            t=(p,n,s,d)
            mycur.execute(sql,t)
            con.commit()
            print("PRICE- Rs 3000")
            payment()
        if c=="3":
            p=input("Enter patient id: ")
            n=input("Enter Patient name: ")
            d=input("Enter date for appointment (YYYY-MM-DD): ")
            s="Whole Body Check For Men"
            sql="insert into healthcheckup values(%s,%s,%s,%s)"
            t=(p,n,s,d)
            mycur.execute(sql,t)
            con.commit()
            print()
            print("PRICE- Rs 20000")
            payment()
        if c=="4":
            p=input("Enter patient id: ")
            n=input("Enter Patient name: ")
            d=input("Enter date for appointment (YYYY-MM-DD): ")
            s="Women Executive Heath Check"
            sql="insert into healthcheckup values(%s,%s,%s,%s)"
            t=(p,n,s,d)
            mycur.execute(sql,t)
            con.commit()
            print()
            print("PRICE-Rs 4000")
            payment()
    print("=======================================================================================================================================")
    print("                                               APPOINTMENT BOOKED                                                                      ")
    print("=======================================================================================================================================")
    print()
    print()
    
        
def appointment():
    s=input("Enter Speciality: ")
    sql="select * from dr_details where speciality=%s"
    mycur.execute(sql,(s,))
    m=mycur.fetchall()
    for i in m:
        print("====================================================================================================================================")
        print(i)
        print("====================================================================================================================================")
    print()
    q=input("Enter doctor name with whom you want to take an appointment")
    i=input("Enter doctor id: ")
    n=input("Enter Patient name: ")
    p=input("Enter patient id: ")
    d=input("Enter date for appointment (YYYY-MM-DD): ")
    t=input("Enter preferred time: ")
    f="insert into appointment values(%s,%s,%s,%s,%s,%s)"
    t=(i,q,n,p,t,d)
    mycur.execute(f,t)
    con.commit()
    print()
    print("Amount to be paid : 800")
    payment()
    print("=======================================================================================================================================")
    print("                                               APPOINTMENT BOOKED                                                                      ")
    print("=======================================================================================================================================")
    print()
    print()
    

print("****************************************************************************************************************************************************")   
print("****************************************************************************************************************************************************")
print("                                                    WELCOME TO ORION HOSPITAL                                                                       ")
print("****************************************************************************************************************************************************")
print("****************************************************************************************************************************************************")
print()
print()
print("1. DOCTOR")
print("2. PATIENT")
a=int(input("Enter choice: "))
if a==1:
    dsignin()
    i=input("Enter dr id")
    t=(i,)
    sql="select * from appointment where dr_id=%s"
    mycur.execute(sql,t)
    m=mycur.fetchall()
    for i in m:
        print("====================================================================================================================================")
        print(i)
        print("====================================================================================================================================")

if a==2:
    print()
    print()
    n=input("Are you a registered patient? (y/n): ")
    if n=="y":
        psignin()
    if n=="n":
        preg()
    print()
    print()
    while True:
        print("====================================================================================================================================")
        print("====================================================================================================================================")
        print("                                             1. BOOK AN APPOINTMENT                                                                 ")
        print("                                             2. BOOK A HEALTH CHECKUP                                                               ")
        print("                                             3. FIND A DOCTOR                                                                       ")
        print("                                             4. SHARE YOUR FEEDBACK                                                                 ")
        print("                                             5. CONTACT US                                                                          ")
        print("                                             6. EXIT                                                                                ")
        print("====================================================================================================================================")
        print("====================================================================================================================================")
        print()
        print()
        q=int(input("Enter Choice: "))
        if q==1:
            appointment()
        if q==2:
            hlthckup()
        if q==3:
            finddr()
        if q==4:
            feedback()
        if q==5:
            contact()
        if q==6:
            print("===================================================================================================================================")
            print("                                                HAVE A NICE DAY!                                                                   ")
            print("===================================================================================================================================")
            break
            
            
            
            
        
        
    
        
        
    
    
    
    


    
    
    
    

            
    


   
    
    
    
