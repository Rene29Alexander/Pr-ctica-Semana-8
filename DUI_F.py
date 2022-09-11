def DUI():

     dui = input("Ingresa tu dui: ")

     if dui.isdigit():
        if len(dui)==9:
            print("DUI VALIDO")
        else:
            print("DUI INVALIDO")
     else:
        print("DUI INVALIDO")
        