#NameValidationProcess.py
from NameValidationExpection import SpaceError,ZerolengthError,InvalidNameError
def Validate(name):
    if (name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        if len(words)==0:
            raise ZerolengthError
        else:
            res=True
            for word in words:
                if (not word.isalpha()):
                    res=False
                    break
            if(res):
                return name
            else:
                raise InvalidNameError
