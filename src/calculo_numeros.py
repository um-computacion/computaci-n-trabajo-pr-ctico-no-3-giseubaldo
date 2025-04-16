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

if __name__ == "__main__":
    # Código para ejecutar el programa interactivamente
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except NumeroDebeSerPositivo as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nPrograma finalizado.")
            break

if __name__ == '__main__':
    unittest.main()