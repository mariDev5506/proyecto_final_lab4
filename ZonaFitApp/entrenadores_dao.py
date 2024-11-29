from entrenador import Entrenador 
from conexion import Conexion

class EntrenadorDAO:
    SELECCIONAR = 'SELECT * FROM entrenador'
    INSERTAR = 'INSERT INTO entrenador(nombreEntrenador, apellidoEntrenador, dniEntrenador) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE entrenador SET nombreEntrenador=%s, apellidoEntrenador=%s, dniEntrenador=%s WHERE idEntrenador=%s'
    ELIMINAR = 'DELETE FROM entrenador WHERE idEntrenador=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla entrenadores
            entrenadores = []
            for registro in registros:
                entrenador = Entrenador(registro[0], registro[1],
                                  registro[2], registro[3])
                entrenadores.append(entrenador)
            return entrenadores

        except Exception as e:
            print(f'Ocurrio un error al seleccionar entrenadores: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, entrenador):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (entrenador.nombreEntrenador, entrenador.apellidoEntrenador, entrenador.dniEntrenador)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar entrenador: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, entrenador):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (entrenador.nombreEntrenador, entrenador.apellidoEntrenador,
                       entrenador.dniEntrenador, entrenador.idEntrenador)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar entrenador: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, entrenador):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (entrenador.idEntrenador,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar entrenador: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
if __name__ == '__main__':
    # seleccionar clientes
    entrenadores = EntrenadorDAO.seleccionar()
    for entrenador in entrenadores:
        print(entrenador)
