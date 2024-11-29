class Entrenador:
    # Se realiza un construcctor

    #realizar el metodo de encapsuñamiento  PROYECTO
    def __init__(self, idEntrenador=None, nombreEntrenador=None, apellidoEntrenador=None, dniEntrenador=None):
        self.idEntrenador = idEntrenador
        self.nombreEntrenador = nombreEntrenador
        self.apellidoEntrenador = apellidoEntrenador
        self.dniEntrenador = dniEntrenador

    def __str__(self):
        return (f'Id: {self.idEntrenador}, Nombre: {self.nombreEntrenador}, '
                f'Apellido: {self.apellidoEntrenador}, DNI-Entrenador: {self.dniEntrenador}')