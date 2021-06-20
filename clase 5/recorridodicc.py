diccionario = {'a':{'nombre1':'Marco', 'edad1':31, 'lenguajes':{
                1:'Python',
                2:'C++',
                3:'Java',
                4:'PHP',
                5:'JavaScript',
                6:'C#'}
               },'b':{'nombre1':'Juan', 'edad1':21, 
               'lenguajes':{
                1:'Python',
                2:'C++',
                3:'Java'}
               }}

for dev in diccionario:
    print(dev)
for key in diccionario.keys():
    print(key)

for value in diccionario.values():
    print(value)
for key, value in diccionario.items():
    print(key)
    print(value)
    
    