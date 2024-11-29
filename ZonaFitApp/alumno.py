class Alumno:
    # Se realiza un construcctor

    #realizar el metodo de encapsuñamiento  PROYECTO
    def __init__(self, idAlumno=None, nombreAlumno=None, apellidoAlumno=None, dniAlumno=None):
        self.idAlumno = idAlumno
        self.nombreAlumno = nombreAlumno
        self.apellidoAlumno = apellidoAlumno
        self.dniAlumno = dniAlumno

    def __str__(self):
        return (f'Id: {self.idAlumno}, Nombre: {self.nombreAlumno}, '
                f'Apellido: {self.apellidoAlumno}, DNI-Alumno: {self.dniAlumno}')