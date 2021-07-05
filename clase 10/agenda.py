import pandas as pd
from pandas.core.frame import DataFrame

def get_data():
    return pd.read_csv('agenda.csv')

def show_menu():
    print("""
        Opciones \n1. Crear \n2. Listar \n3. Buscar \n4. Editar \n5. Eliminar \n7. Salir""")
    option = input('Digite la opción. ')
    if option == '1':
        create()
    elif option == '2':
        list_contacts()
    elif option == '3':
        search()
    elif option == '4':
        update()
    elif option == '5':
        delete()
    elif option == '7':
        exit()
        
def create():
    name, phone, email = input('Nombre: '), input('Celular: '), input('E-mail: ')
    filer = open('agenda.csv','a')
    filer.write(f'{name},{phone},{email}\n')
    filer.close()    
    
def update():
    list_contacts()
    id = int(input('Digite Id contacto: '))
    option = input("""¿Qué desea editar?\n1. Nombre\n2. Celular\n3. E-mail""")
    dataf = get_data()
    if option == '1':
        dataf.loc[id, 'nombre'] = input('Nombre: ')
    elif option == '2':
        dataf.loc[id, 'celular'] = input('Celular: ')        
    elif option == '3':
        dataf.loc[id, 'e-mail: '] = input('E-mail')
    dataf.to_csv('agenda.csv', index=False) 
    
def delete():
    list_contacts()
    id = int(input('Id de contacto: '))
    dataf = get_data()
    dataf.drop([id], inplace=True,axis=0)
    dataf.to_csv('agenda.csv', index=False)    

def search():
    name = input('Digita el nombre que deseas buscar: ')
    dataf = get_data()
    print( dataf[dataf['nombre'].str.contains(name)] )

def list_contacts():
    print(get_data())

def run():
    show_menu()
    run()

if __name__ == '__main__':
    run()



if __name__ == 'main':
   run() 