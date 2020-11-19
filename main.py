# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def mensaje(nombre,paterno,materno):
    print('Hola, mi nombre es: {} y mis apellidos son {} {}'.format(nombre,paterno,materno))

def suma(a,b):
    print(f'El resultado es: {a+b}')

def resta(a,b):
    print(f'El resultado es: {a - b}')

    '''
    Comentario de varias lineas en
    python
    '''
def tipos():
    a = 10
    b = 12.4
    t = 'hola'
    v = True
    print(int(a))
    print(float(b))
    print(str(t))
    print(bool(v))


    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm edsonfer')
    suma(5,8)
    resta(10,8)
    mensaje('Edson Fernando', 'Ventura', 'Oropeza')
    tipos()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
