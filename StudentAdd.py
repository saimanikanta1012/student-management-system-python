#StudentAdd.py<-- file name and module name
import pickle

from NameValidationProcess import Validate
from NameValidationExpection import SpaceError,InvalidNameError,ZerolengthError

def Duplicated(sno):
    studrecords=[]
    with open("student.pick","rb")as sd:
        while (True):
            try:
                record=pickle.load(sd)
                studrecords.append(record)
            except EOFError:
                break
        dupl=False
        for rec in studrecords:
            if (rec[0]==sno):
                dupl=True
                break
        return dupl

def Recordadd():
    with open("student.pick","ab") as fp:
        while(True):
            try:
                sno=int(input("Enter Student Number:"))
                sname=Validate(input("Enter Student Name:"))
                marks=float(input("Enter marks secured:"))
                colname=Validate(input("Enter College Name:"))
                stlist=[]
                stlist.append(sno)
                stlist.append(sname.upper())
                stlist.append(marks)
                stlist.append(colname.upper())
                #save the stlist data
                if(not Duplicated(sno)):
                    pickle.dump(stlist,fp)
                    print("Record saved successfully")
                else:
                    print("Record already exist with {} student number".format(sno))
                ch = input("Do u want to Insert another student record (Yes/No):")
                if ch.lower() == "no":
                    break
            except ValueError:
                print("Dont Enter alnums, symbols or special characters. ")
            except SpaceError:
                print("Dont Enter spaces")
            except ZerolengthError:
                print("U must enter something Dont leave Blank")
            except InvalidNameError:
                print("Enter a valid name")
