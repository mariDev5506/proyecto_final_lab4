class Presentismo:
    # Se realiza un construcctor

    #realizar el metodo de encapsuñamiento  PROYECTO
    def __init__(self, Entrenador_idEntrenador=None, Alumno_idAlumno=None, fecha=None, hora=None):
        self.Entrenador_idEntrenador = Entrenador_idEntrenador
        self.Alumno_idAlumno = Alumno_idAlumno
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return (f'Id_Entrenador: {self.Entrenador_idEntrenador}, Id_Alumno: {self.Alumno_idAlumno}, '
                f'Fecha: {self.fecha}, Hora: {self.hora}')