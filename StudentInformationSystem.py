#StudentInformationSystem.py
from StudentMenu import menu
from StudentAdd import Recordadd
from StudentDelete import RecordDel
from StudentUpdate import studUpdate
from StudentView import studentview,studentviewall
while(True):
    menu()
    ch=int(input("Enter Your Choice:"))
    match(ch):
        case 1:
            Recordadd()
        case 2:
            RecordDel()
        case 3:
            studUpdate()
        case 4:
            pass
        case 5:
            studentview()
        case 6:
            studentviewall()
        case 7:
            print("Thanks For using this Program")
            break
