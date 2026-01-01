#StudentUpdate.py
import pickle


def studUpdate():
    try:
        sno_to_update = int(input("Enter Student Number to update the Record Details:"))
        found = False
        updatedrecords=[]

        with open("student.pick","rb")as f:
            while True:
                try:
                    record=pickle.load(f)
                    updatedrecords.append(record)
                except EOFError:
                    break

            for i in range(len(updatedrecords)):
                if updatedrecords[i][0] == sno_to_update:
                    print("=" * 40)
                    print("\t\tCurrent Details")
                    print("="*40)
                    print(f"Current Student Name:{updatedrecords[i][1]}")
                    print(f"Current Student Marks:{updatedrecords[i][2]}")
                    print(f"Current College Name:{updatedrecords[i][3]}")
                    print("=" * 40)
                    print("Update New Details:")
                    print("=" * 40)
                    try:
                        nsname = input("Enter New Name to Update:")
                        nmarks = int(input("Enter New Marks:"))
                        ncolname = input("Enter New College name:")
                        print("=" * 40)

                        if nsname.strip():
                            updatedrecords[i][1]=nsname
                        if nmarks:
                            updatedrecords[i][2]=nmarks
                        if ncolname:
                            updatedrecords[i][3]=ncolname

                        found=True
                        print("Record Saved Successfully")
                        break
                    except ValueError:
                        print("Dont Enter Alnums, Symbols and special characters")
            if not found:
                print("Student Number doesnot exists")
        with open("student.pick","wb")as f:
            for record in updatedrecords:
                pickle.dump(record,f)
    except ValueError:
        print("Please Enter a valid number! ")
    except FileNotFoundError:
        print("File not Found")