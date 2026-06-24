def transformar(pies: int, pulgadas:int) -> float: #definimos la función con sus parámetros y el tipo de dato que va a retornar
    pie_a_pulgada= pies*12  #pasamos los pies a pulgadas
    pulgada_a_cm= pulgadas*2.54 + pie_a_pulgada*2.54 #pasamos las pulgadas a cm y sumamos las pulgadas que vienen de los pies
    cm_a_mentros= pulgada_a_cm/100 #pasamos los cm a metros

    return  round(cm_a_mentros, 2)
print(transformar(0, 67))

