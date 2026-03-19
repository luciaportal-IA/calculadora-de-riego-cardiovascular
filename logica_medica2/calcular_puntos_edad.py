def calcular_puntos_edad(genero, edad, diabetico, fumar, presionA, colesterolT, HDL,antecedentesF):
    puntos = 0
    if genero == "masculino":
        if edad <= 29:
            puntos += 1
        elif 30 <= edad <= 39:
            puntos += 2
        elif 40 <= edad <= 49:
            puntos += 3
        elif 50 <= edad <= 59:
            puntos += 5
        elif 60 <= edad <= 69:
            puntos += 7
        elif 70 <= edad: 
            puntos += 8
        
    
    elif genero == "femenino":
        if edad <= 29: 
            puntos += 0
        elif 30 <= edad <= 39:
            puntos += 1
        elif 40 <= edad <= 49:
            puntos += 2
        elif 50 <= edad <= 59:
            puntos += 4
        elif 60 <= edad <= 69:
            puntos += 5
        elif 70 <= edad: 
            puntos += 6
            
     #fumar       
    if fumar == "si":
        puntos += 2
    elif fumar == "no":
        puntos -= 2
    #diabetes
    if diabetico == "si":
        puntos += 3
    elif diabetico == "no":
        puntos -= 3
    #presion
    if presionA < 120:
            puntos += 0
    elif 120 <= presionA <= 129:
            puntos += 2
    elif 130 <= presionA <= 139:
            puntos += 3
    elif 140<= presionA <= 179:
            puntos += 4
    elif 180<= presionA: 
            puntos += 5
    #colesterol1    
    if colesterolT < 160:
        puntos += 0
    elif 160 <= colesterolT <= 199:
        puntos += 1
    elif 200<= colesterolT <= 239:
        puntos+= 2
    elif 240 <= colesterolT<= 279:
        puntos += 3
    elif 280 < colesterolT:
        puntos += 4
    #colesterol2
    if HDL < 35:
        puntos += 2
    elif 35 <= HDL <= 44:
        puntos += 1
    elif 45 <= HDL <= 59:
        puntos += 0
    elif 60 < HDL:
        puntos -= 1
    #familia
    if antecedentesF == "si":
        puntos += 2
    elif antecedentesF == "no":
        puntos -= 2


    tabla_hombres = {-1:1, 0:2, 1:2, 2:3, 3:4, 4:4, 5:6, 6:7, 7:8, 8:10, 9:11, 10:14, 11:16, 12:21, 13:25}
    tabla_mujeres = {-1:1, 0:1, 1:1, 2:1, 3:1, 4:1, 5:2, 6:2, 7:3, 8:4, 9:4, 10:6, 11:7, 12:8, 13:10, 14:12, 15:15, 16:20}

    if genero == "masculino":
        porcentaje = tabla_hombres.get(puntos, 45 if puntos > 13 else 1)
    else:
        porcentaje = tabla_mujeres.get(puntos, 45 if puntos > 16 else 1)
    
    # IMPORTANTE: Devolvemos los dos valores
    return puntos, porcentaje