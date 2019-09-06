


def run():
    with open('numeros.txt','w') as f:  #si el archivo no existe paython lo crea y modo de escritura
        for i in range(10): #escribira los numeros del 1 al 9
            f.write(str(i))


if __name__ == '__main__':
    run()