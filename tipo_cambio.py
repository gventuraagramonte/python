

def foreign_exchange_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('CALCULADORA DE DIVISAS')
    print('Convierte pesos mexicanos a persos colombianos.')
    print('')

    ammount = float(input('ingresa la cantidad de pesos mexicanos que quieres convertir '))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')

if __name__=='__main__':
    run()