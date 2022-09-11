import edad
import DUI_F

print("-------------------------------------------------------------------------------")
menu = int(input("Bienvenido al sistema que desea hacer: 1:calcular tu edad, 2:DUI: "))
print("-------------------------------------------------------------------------------")

if menu == 1:
    calculo = edad.edad()
    print(calculo)

elif menu == 2:
    calculo_f = DUI_F.DUI()
    print(calculo_f)

else:
    print("Numero no valido.")
    


