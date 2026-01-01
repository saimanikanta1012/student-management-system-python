#StudentDelete.py
import pickle

def RecordDel():
    while(True):
        studRecords=[]
        with open("student.pick","rb") as fp:
            while(True):
                try:
                    record=pickle.load(fp)
                    studRecords.append(record)
                except EOFError:
                    break
            #Accept student number to delete
            try:
                sno=int(input("Enter Student number to delete the Record:"))
                found=False
                for ri in range(len(studRecords)):
                    if(studRecords[ri][0]==sno):
                        found=True
                        recordindex=ri
                        break
            except ValueError:
                print("Dont Enter Alnums, Symbols and special characters")
            if(found):
                studRecords.pop(recordindex)
                print("Record Deleted")
                with open("student.pick", "wb") as fp:
                    for record in studRecords:
                        pickle.dump(record,fp)
            else:
                print("Record doesn't Exist!")
            ch=input("Do U want to Delete Another Record(Yes/No):")
            if ch.lower()=="no":
                break
