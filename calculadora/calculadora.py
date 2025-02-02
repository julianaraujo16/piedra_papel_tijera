"""
Nombre: calculadora.py
Autor: Juliana Bolaños
Fecha: 1/02/2025
Descripción: Implementación de una calculadora basica
"""

print("\n¡Bienvenid@ a su Calculadora! 📱")

print("\nMenu: \n1 - Sumar \n2 - Restar \n3 - Multiplicar \n4 - Dividir \n5 - Salir")

def calculator(number1, number2, operation):
        if operation == 1:
              answer = number1+number2
              return answer
        elif operation == 2:
              answer = number1-number2
              return answer
        elif operation == 3:
              answer = number1*number2
              return answer
        elif operation == 4:
            if number2 == 0:
                    answer ="\nError; divicion entre 0"
                    return answer
            else:
                  answer = number1/number2
                  return answer
        else:
            answer ="\nDigitos invalidos"
            return answer



while True:
    operation = int(input("\nIngrese una opcion del Menu: "))

    if operation == 5:
         print("\nSaliendo...")
         break
    elif operation in [1,2,3,4]:
        while True:
                number1 = (input("\nPrimer digito: "))
                number2 = (input("Segundo digito: "))

                if number1.isnumeric() & number2.isnumeric():
                    answer = calculator(int(number1),int(number2),int(operation))
                    if type(answer) == str:
                          print(answer)
                    else:
                          print(f"\nLa respuesta es: {answer}")
                    break
                else:
                      print("Ingrese solo numeros")

    else:
          print("Ingrese un valor valido")
