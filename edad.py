def edad():
    while True:
        try:
           annio = int(input("Ingresa tu año de nacimiento: "))

        except ValueError:
            return("Fecha invalida")
            continue
        edad = 2022 - annio
        if edad >= 18:
            return("Eres mayor de edad")
            break
        
        elif edad >= 0:
            return("Eres menor de edad")
            break
        elif edad < 0:
            return("Fecha invalida")
            break
 
    


