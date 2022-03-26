import os,pickle,hashlib
import time
from cryptography.fernet import Fernet as aes
def pat(T):
 choice=1
 while(choice!=0):
    print("Enter 0 to exit")
    print("Enter 1 to add patient record")
    print("Enter 2 to display patient record")
    choice=int(input("Enter choice: "))
    if choice==1:
        p1=medRecord()
        p1.insRecord()
        f=open("Patient records.bin","ab")
        pickle.dump(p1,f)
        f.close()
    elif choice==2:
        pid=input("Enter patient ID: ")
        f=open("Patient records.bin","rb")
        try:
            while True:
                p1=pickle.load(f)
                if cipher.decrypt(p1.pid).decode()==pid:
                    break
        except EOFError:
            print("Patient doesn't exist")
        else:
            p1.printRec()
            g=open("logbook.bin","ab")
            q=("Doctor ID " +str(T),str(time.asctime(time.localtime(time.time()))),"Patient ID :" + str(pid))
            pickle.dump(q,g)
            g.close()
fernet_key=b'rrm-9Rx_5eeVLJQRehibrO_AwjazFV_mEb7RrzcHans='
cipher=aes(fernet_key)
#patient
class medRecord:
    def __init__(self):
        self.pid=""
        self.name=""
        self.btype=""
        self.gender=""
        self.age=0
        self.dob=""
        self.height=0
        self.weight=0
        self.allergies=[]
        self.medications=[]
        self.conditions=[]
        self.pTestRep=""
        self.phone=""
        self.emerno=""
        self.remarks=[]
        self.time=""
    def insRecord(self):
        self.pid=cipher.encrypt(input("Enter patient ID: ").encode())
        self.name=cipher.encrypt(input("Enter patient name: ").encode())
        self.btype=cipher.encrypt(input("Enter patient blood type: ").encode())
        self.gender=cipher.encrypt(input("Enter patient gender: ").encode())
        self.age=cipher.encrypt(input("Enter patient age: ").encode())
        self.dob=cipher.encrypt(input("Enter patient's DoB: ").encode())
        self.height=cipher.encrypt(input("Enter patient's height: ").encode())
        self.weight=cipher.encrypt(input("Enter patient's weight: ").encode())
        n=int(input("Enter no: of allergies: "))
        for i in range(0,n):
            self.allergies+=[cipher.encrypt(input("Enter allergy: ").encode())]
        n=int(input("Enter no: of medications: "))
        for i in range(0,n):
            self.medications+=[cipher.encrypt(input("Enter medication: ").encode())]
        n=int(input("Enter no: of medical conditions: "))
        for i in range(0,n):
            self.conditions+=[cipher.encrypt(input("Enter medical condition: ").encode())]
        self.pTestRep=cipher.encrypt(input("Enter pathological test report: ").encode())
        self.phone=cipher.encrypt(input("Enter phone no.: ").encode())
        self.emerno=cipher.encrypt(input("Emter emergency no.: ").encode())
        n=int(input("Enter no: of remarks: "))
        for i in range(0,n):
            self.remarks+=[cipher.encrypt(input("Enter remarks: ").encode())]
        self.time=cipher.encrypt(str(time.asctime(time.localtime(time.time()))).encode())
    def printRec(self):
        print("\n")
        print("Patient ID: ",cipher.decrypt(self.pid).decode())
        print("Patient name: ",cipher.decrypt(self.name).decode())
        print("Patient blood type: ",cipher.decrypt(self.btype).decode())
        print("Patient gender: ",cipher.decrypt(self.gender).decode())
        print("Patient age: ",cipher.decrypt(self.age).decode())
        print("Patient's DoB: ",cipher.decrypt(self.dob).decode())
        print("Patient height: ",cipher.decrypt(self.height).decode())
        print("Patient weight",cipher.decrypt(self.weight).decode())
        print("Patient allergies:")
        for i in self.allergies:
            print("\t-",cipher.decrypt(i).decode())
        print("Patient medications:")
        for i in self.medications:
            print("\t-",cipher.decrypt(i).decode())
        print("Patient medical conditions:")
        for i in self.conditions:
            print("\t-",cipher.decrypt(i).decode())
        print("Pathological test report: ",cipher.decrypt(self.pTestRep).decode())
        print("Patient phone no.: ",cipher.decrypt(self.phone).decode())
        print("Patient emergency no.: ",cipher.decrypt(self.emerno).decode())
        print("Remarks:")
        for i in self.remarks:
            print("\t-",cipher.decrypt(i).decode())
        print("Patient since : " ,cipher.decrypt(self.time).decode())
        print("\n")

#Doctor class
class doc:
    def _init_(self):
        self.did=""
        self.hash=""
    def insrec(self):
        self.did=input("Enter doctor ID: ")
        P1=input("Enter new password: ")
        self.hash=((hashlib.sha256(P1.encode())).hexdigest())
#Dean hash
DH="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
c0=1
while c0!=0:
    print("Enter 0 to exit")
    print("Enter 1 for dean login")
    print("Enter 2 for doctor login")
    print("Enter 3 for patient login") 
    c0=int(input("Enter choice: "))
    #Dean 
    if c0==1:
        P=input("Enter password: ")
        deanh=((hashlib.sha256(P.encode())).hexdigest())
        #Dean basic 
        if deanh==DH:
            print("Verified")
            c1=1
            while c1!=0:
                print("Enter 0 to exit")
                print("Enter 1 to add new doctor credentials")
                print("Enter 2 to access patient record")
                print("Enter 3 to access log book")
                c1=int(input("Enter choice"))
                if c1==2:
                    pat("Dean")
                elif c1==3:
                    w=open("logbook.bin","rb")
                    try:
                        while True:
                            e=pickle.load(w)
                            print(e)
                    except EOFError:
                        w.close()
                        print()
                elif c1==1:
                    d1=doc()
                    d1.insrec()
                    
                    f=open("Doctor records.bin","ab")
                    pickle.dump(d1,f)
                    f.close()
        else:
            print("Access denied")
    #Doctor
    if c0==2:
        did=input("Enter doctor ID: ")
        f=open("Doctor records.bin","rb")
        dip=input("Enter password :")
        dih=((hashlib.sha256(dip.encode())).hexdigest())
        try:
            while True:
                p1=pickle.load(f)
                if p1.did==did:
                    if p1.hash==dih:
                        print("Verified")
                        pat(str(did))
                    else:
                        print("Access denied")
                    break
                
                        
        except EOFError:
            print("Doctor does not exist")
    #Patient
    if c0==3:
        pid=input("Enter patient ID: ")
        pdob=input("Enter date of birth : ")
        f=open("Patient records.bin","rb")
        try:
            while True:
                p1=pickle.load(f)
                if cipher.decrypt(p1.pid).decode()==pid:
                    if cipher.decrypt(p1.dob).decode()==pdob:
                        p1.printRec()
                        break
                    else:
                        print("Access denied")
                        break
        except EOFError:
            print("Patient doesn't exist")
    print("\n")
            

        
        

                    
                    

            
            
            
    
