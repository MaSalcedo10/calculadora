class operaciones:
    
    @staticmethod    
    def suma (a,b):
        return a + b

    @staticmethod   
    def resta(a,b):
        return a - b
    
    @staticmethod
    def multiplicacion(a,b):
        return a * b
    
    @staticmethod
    def division(a,b):
        try:
            return a / b
        except ZeroDivisionError as err:
            print(f"Ha ocurrido un error: {err}")
            return None
        
            
def main():
    
    print("Bienvenido a mi calculadora¡")
    
    
  
    while True:
        print("\nOpciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
    
        opcion = input("Ingrese una opción: ")
        
        if opcion == "5":
            print("Ha salido del programa¡")
            break
        
        if opcion in {"1","2","3","4"}:
            try:
                a = float(input("Ingrese el primer numero: "))
                b = float(input("Ingrese el segundo numero: "))
            except ValueError:
                print("Por favor, ingrese numeros válidos")
                continue
                
            if opcion == "1":
                resultado = operaciones.suma(a,b)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == "2":
                resultado = operaciones.resta(a,b)
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == "3":
                resultado = operaciones.multiplicacion(a,b)
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == "4":
                resultado = operaciones.division(a,b)
                print(f"El resultado de la división es: {resultado}")
                
    
main()    