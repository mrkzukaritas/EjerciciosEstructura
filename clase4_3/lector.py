cadena=")(sdhfj)((((((("
cadena2="()()"
cadena3="((a*c)+(b/2))"
def verificar(cadena):
    if cadena[0]==")":
        return False
    else:
        parent=0
        for i in range(len(cadena)):
            if cadena[i]=="(":
                parent+=1
            elif cadena[i]==")":
                parent-=1
            else:
                pass
        if parent==0:
            return True
        else:
            return False
print(verificar(cadena))  
print(verificar(cadena2))
print(verificar(cadena3))