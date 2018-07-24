def isEven(num):
    pass

def check_proposition(list):
    for each in list:
        if each%2 == 0:
            if (each / 2) not in list:
                return False
    return True