def ECTS(bal):
    """Функція, яка визначає оцінку за шкалою ECTS"""
    ECTS_tabl= {'A':[100,95], 'B':[94,85], 'C':[84,75], 'D':[74,65], 'E':[64,60], 'FX':[59,30], 'F':[30,0]}
    key_list=list(ECTS_tabl.keys())
    val_list=list(ECTS_tabl.values())
    
    for x in range(len(ECTS_tabl)):
            if bal<= val_list[x][0] and bal>=val_list[x][1]:
             o = key_list[x]
             return o
             break

bal = int(input('Сума балів: '))
o = ECTS(bal)
print('Оцінка ECTS: ', o)
print('')
help(ECTS)
