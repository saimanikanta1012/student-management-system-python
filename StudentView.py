#StudentView.py
import pickle

def studentview():
    try:
        vsno = int(input("Enter Student Number to View details:"))
        found = False

        with open("student.pick","rb")as f:
            while(True):
                try:
                    record = pickle.load(f)

                    if isinstance(record, list):
                        record = {
                            "sno": record[0],
                            "sname": record[1],
                            "marks": record[2],
                            "colname": record[3]
                        }
                    if record["sno"]==vsno:
                        print("-"*50)
                        print(f"\t\tStudent Name:{record['sname']}")
                        print(f"\t\tStudent Marks:{record['marks']}")
                        print(f"\t\tStudent College Name:{record['colname']}")
                        print("-" * 50)
                        found=True
                        break
                except EOFError:
                    break
            if not found:
                print("NO Record Exists with the Student Number")
    except FileNotFoundError:
        print("File not Found!")
    except ValueError:
        print("Please enter valid Integer Value for student number. ")

def studentviewall():
    try:
        with open("student.pick","rb")as f:
            print("="*40)
            print("\t\t\tStudent Records")
            print("=" * 40)
            while(True):
                try:
                    record = pickle.load(f)
                    print(f"\tStudent Number={record[0]}")
                    print(f"\tStudent Name={record[1]}")
                    print(f"\tStudent Marks={record[2]}")
                    print(f"\tStudent College Name={record[3]}")
                    print("-" * 40)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not Found")

