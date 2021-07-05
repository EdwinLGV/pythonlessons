txt = 'Pero qué luz se deja ver allí'
palabras = txt.split()
t = list()
for palabra in palabras:
    t.append((len(palabra), palabra))
    print(t)
t.sort(reverse=True) 

res = list()
for longitud, palabra in t:
    res.append(palabra)
    
print(res)    
    
    

