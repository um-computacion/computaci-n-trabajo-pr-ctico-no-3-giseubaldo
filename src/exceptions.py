import unittest

from src.exceptions import NumeroDebeSerPositivo

class NumeroDebeSerPositivo(Exception):
    """Excepción personalizada para números negativos."""
    
    def __init__(self, mensaje="El número debe ser positivo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


if __name__ == '__main__':
    unittest.main()