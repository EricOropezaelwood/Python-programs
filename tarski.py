def Square(element):
    if(element == "square"):
        return True
    else:
        return False
        
def Red(element):
    if(element == "red"):
        return True
    else:
        return False
        
def tarski (shapes, colors):
    check = True
    for i in range (0,len(shapes)):
        for j in range (0,len(shapes[i])):
            if(Square(shapes[i][j])):
                if(not Red(colors[i][j])):
                    check = False
    return check