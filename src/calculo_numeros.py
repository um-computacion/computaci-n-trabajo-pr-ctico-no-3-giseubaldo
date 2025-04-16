import unittest 
from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    """
    Solicita al usuario que ingrese un número y valida que sea positivo.
    
    Returns:
        int: El número ingresado si es válido
        
    Raises:
        ValueError: Si la entrada no es un número
        NumeroDebeSerPositivo: Si el número es negativo
    """
    entrada = input("Ingrese un número: ")
    
    try:
        numero = int(entrada)
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")

    if numero < 0:
        raise NumeroDebeSerPositivo()

    return numero

def main():
    """
    Función principal que maneja el bucle de interacción con el usuario
    y gestiona todas las excepciones posibles.
    """
    print("Programa de validación de números")
    print("Presione Ctrl+C para salir\n")
    
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}\n")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}\n")

if __name__ == "__main__":
    unittest.main()