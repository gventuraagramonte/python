

#Lista binaria, se usa para capturar datos en grandes cantidades.
#La búsqueda binaria se usa mayormente cuando el usuario esta constantemente trabajando con iteracciones constantes.
def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

# Obtenemos el punto medio
    mid = int((low + high)/2) #Tenemos que agregar int a la variable para que el numero salga entero

    if numbers[mid] == number_to_find:
        return True                         #Preguntamos si el punto medio es igual al numero que queremos encontrar
        # Si el numero medio es mayor al que queremos encontrar, entonces debemos buscar de la mitad hacia abajo
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid -1)  
    else: # Si el numero medio es mayor al que queremos encontrar, entonces debemos buscar de la mitad hacia arriba
        return binary_search(numbers, number_to_find, mid + 1, high)



if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find = int(input('Ingresa un numero: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers)-1)

    if result is True:
        print('El numero si esta en la lista')
    else:
        print('El numero no esta en la lista')
