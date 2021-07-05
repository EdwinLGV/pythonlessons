import pandas as pd

serie_1 = pd.Series([5, 8, 9])
serie_2 = pd.Series({10:50, 20:80, 30:40})

frame_1 = pd.DataFrame({10:[25, 34, 15], 20:[24, 36, 20], 30:[28, 32, 19]})
frame_2 = pd.DataFrame([[25, 34, 15], [24, 36, 20], [28, 32, 19]], columns=[10, 'Hola', 30])

print(serie_2)
print(frame_1)
print(frame_2)
