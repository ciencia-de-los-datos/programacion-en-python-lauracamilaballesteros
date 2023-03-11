"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""



#La funcion pregunta_01 la suma de la segunda columna.

def pregunta_01():
    
    
    with open('data.csv', 'r') as f:
        sum_col2 = 0
        for row in f:
            row = row.split("\t")
            sum_col2 = sum_col2 + float(row[1]) 
            
            
    return sum_col2



def pregunta_02():


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
 
    with open('data.csv', 'r') as f:
        
        
    
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]
            
        #Extrae el primer dato de la columna
        row_0 = [t[0][0] for t in f]
        #Crea una lista de tuplas con la letra y la cuenta de la letra
        result = [(letter, row_0.count(letter)) for letter in sorted(set(row_0))]
        
        
        

    
    return result


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    
     
    with open('data.csv', 'r') as f:
        
        
    
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]


        # Extrae los valores de las letras y de numeros 
        letters = [t[0][0] for t in f]
        values = [int(t[1]) for t in f]


        sum_letters = {}

        #Itera los valores de letras y valores al tiempo
        for letter, value in zip(letters, values):
            if letter in sum_letters:
                sum_letters[letter] += value
            else:
                sum_letters[letter] = value

        #Ordena los valores de las letras en forma ascendente y se vuelve una lista de tuplas
        result = sorted([(letter, sum) for letter, sum in sum_letters.items()])
        
    return result


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    
    with open('data.csv', 'r') as f:
        
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]
    
    

        fecha_mes = [t[2].split("-")[1] for t in f]
        fecha_mes

        result = [(mes, fecha_mes.count(mes)) for mes in sorted(set(fecha_mes))]

    return result
    


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', 'r') as f:


        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        #Extracción de los valores de letras y numeros y construcción de una lista con letras y numeros
        letters = [t[0][0] for t in f]
        values = [int(t[1][0]) for t in f]
        lista = list(zip(letters, values))

        maximos_minimos = {}

        #Construcción del diccionario
        for letra, valor in lista:
            if letra not in maximos_minimos:
                maximos_minimos[letra] = {"maximo": valor, "minimo": valor}
            else:
                #Reemplazo de valores máximos y mínimos en el diccionario
                if valor > maximos_minimos[letra]["maximo"]:
                    maximos_minimos[letra]["maximo"] = valor
                if valor < maximos_minimos[letra]["minimo"]:
                    maximos_minimos[letra]["minimo"] = valor

        result = [(letra, maximos_minimos[letra]["maximo"], maximos_minimos[letra]["minimo"]) for letra in maximos_minimos]
        result = sorted(result, key=lambda result: result[0])

        
        return result

    
    
   


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    with open('data.csv', 'r') as f:


        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]
        
        min_max_dict = {}

        # Extrae el elemento 5
        for row in f:
            col5_dict = row[4]
            #Separa los elementos que estan separados por , y los vuelve lista
            for key_value in col5_dict.split(","):
                # Separa los elementos llave y valor separados por ,
                key, value = key_value.split(":")
                value = int(value)
                if key in min_max_dict:

                    min_max_dict[key].append(value)
                else:
                    min_max_dict[key] = [value]
            min_max_dict
            result = []
            for key, values in sorted((min_max_dict.items())):
                result.append((key, min(values), max(values)))

        
    return result


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    
    with open('data.csv', 'r') as f:
        dict_letters_values = {}
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        for row in f:
            col5_dict = row[4]
            for key_value in col5_dict.split(","):
                key, value = key_value.split(":")
                value = int(value)
                if key in dict_letters_values:
                    dict_letters_values[key].append(value)
                else:
                    dict_letters_values[key] = [value]
                    



        result = { key:len(values) for key, values in sorted(dict_letters_values.items()) }
    
    return result



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open('data.csv', 'r') as f:
        dict_letters_values = {}
        f = [x.replace("\n", "") for x in f ]
        f = [y.split("\t") for y in f ]

        for row in f:
            col5_dict = row[4]
            for key_value in col5_dict.split(","):
                key, value = key_value.split(":")
                value = int(value)
                if key in dict_letters_values:
                    dict_letters_values[key].append(value)
                else:
                    dict_letters_values[key] = [value]



        result = { key:len(values) for key, values in sorted(dict_letters_values.items()) }
        
    return result
