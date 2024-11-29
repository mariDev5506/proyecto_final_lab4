from alumno import Alumno
from conexion import Conexion


class AlumnoDAO:
    SELECCIONAR = 'SELECT * FROM alumno'
    INSERTAR = 'INSERT INTO alumno(nombreAlumno, apellidoAlumno, dniAlumno) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE alumno SET nombreAlumno=%s, apellidoAlumno=%s, dniAlumno=%s WHERE idAlumno=%s'
    ELIMINAR = 'DELETE FROM alumno WHERE idAlumno=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla alumnos
            alumnos = []
            for registro in registros:
                alumno = Alumno(registro[0], registro[1],
                                  registro[2], registro[3])
                alumnos.append(alumno)
            return alumnos

        except Exception as e:
            print(f'Ocurrio un error al seleccionar alumnos: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, alumno):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (alumno.nombreAlumno, alumno.apellidoAlumno, alumno.dniAlumno)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar alumno: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, alumno):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (alumno.nombreAlumno, alumno.apellidoAlumno,
                       alumno.dniAlumno, alumno.idAlumno)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar alumno: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, alumno):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (alumno.idAlumno,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar alumno: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Listar
    # seleccionar clientes
    alumnos = AlumnoDAO.seleccionar()
    for alumno in alumnos:
        print(alumno)