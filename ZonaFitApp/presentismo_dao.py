from presentismo import Presentismo
from conexion import Conexion


class PresentismoDAO:
    SELECCIONAR = 'SELECT * FROM presentismo'
    INSERTAR = "INSERT INTO presentismo (Entrenador_idEntrenador, Alumno_idAlumno, fecha, hora) VALUES (%s, %s, %s, %s)"
    SELECCIONAR_POR_FECHA = 'SELECT * FROM presentismo WHERE fecha = %s'

    @classmethod
    def seleccionar(cls, fecha=None):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            # Si se proporciona una fecha, filtra por esa fecha
            if fecha:
                cursor.execute(cls.SELECCIONAR_POR_FECHA, (fecha,))
            else:
                cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla presentismo
            presentismos = []
            for registro in registros:
                presentismo = Presentismo(registro[0], registro[1],
                                  registro[2], registro[3])
                presentismos.append(presentismo)
            return presentismos

        except Exception as e:
            print(f'Ocurrio un error al seleccionar presentismo: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, presentismo):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (presentismo.Entrenador_idEntrenador, presentismo.Alumno_idAlumno, presentismo.fecha, presentismo.hora)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar presentismo: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    # Listar
    # seleccionar clientes
    presentismos = PresentismoDAO.seleccionar()
    for presentismo in presentismos:
        print(presentismo)