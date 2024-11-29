from alumno import Alumno
from alumno_dao import AlumnoDAO
from entrenador import Entrenador
from entrenadores_dao import EntrenadorDAO
from presentismo import Presentismo
from presentismo_dao import PresentismoDAO
from datetime import datetime


print('***  Gimnasio Zona Fit  *** ')
opcion = None
while True:
    print('''Menu:
    1. Presentismo
    2. Alumnos
    3. Entrenadores
    4. Salir
    ''')
    try:
        opcion = int(input('Escribe tu opcion ( 1-4 ): '))
        if 1 <= opcion <= 4:
            if opcion == 1:  # Presentismo
                opcion1 = None
                while True:
                    print('''Menu:
                            1. Lista de Presentes
                            2. Nueva Asistencia
                            3. Volver
                            ''')
                    try:
                        opcion1 = int(input('Escribe tu opcion ( 1-3 ): '))
                        if 1 <= opcion1 <= 3:
                            if opcion1 == 1:  # Listar                                
                                opcion2 = None
                                presentismos = PresentismoDAO.seleccionar()
                                if not presentismos:
                                    print("No hay registro de presentismos disponibles")
                                    opcion2=4
                                else:
                                    while True:
                                        print('''Menu:
                                                    1. Lista General
                                                    2. Fecha Ascendente
                                                    3. Fecha Descendente
                                                    4. Volver
                                        ''')
                                        try:
                                            opcion2 = int(input('Escribe tu opción (1-4): '))  # Convertimos a entero
                                            if 1 <= opcion2 <= 4:  # Validar si está dentro del rango permitido
                                                if opcion2 == 1:  # Lista General
                                                    presentismos = PresentismoDAO.seleccionar()
                                                    if not presentismos:
                                                        print("No hay registro de presentismos disponibles")
                                                    else:
                                                        print('\n*** Listado de Alumnos ***')
                                                        for presentismo in presentismos:
                                                            print(presentismo)
                                                    print()
                                                elif opcion2 == 2:  # Lista Ascendente
                                                    presentismos_fecha_ascendente = PresentismoDAO.seleccionar()
                                                    presentismos_fecha_ascendente = sorted(
                                                        presentismos_fecha_ascendente,
                                                        key=lambda presentismo: presentismo.fecha # Usar directamente el atributo fecha
                                                    )
                                                    print('\n*** Listado de Alumnos (Fecha Ascendente) ***')
                                                    for presentismo in presentismos_fecha_ascendente:
                                                        print(presentismo)
                                                    print()
                                                elif opcion2 == 3:  # Lista Descendente
                                                    presentismos_fecha_descendente = PresentismoDAO.seleccionar()
                                                    presentismos_fecha_descendente = sorted(
                                                        presentismos_fecha_descendente,
                                                        key=lambda presentismo: presentismo.fecha,
                                                        # Usar directamente el atributo fecha
                                                        reverse=True  # Ordenar de forma descendente
                                                    )
                                                    print('\n*** Listado de Alumnos (Fecha Descendente) ***')
                                                    for presentismo in presentismos_fecha_descendente:
                                                        print(presentismo)
                                                    print()
                                                elif opcion2 == 4:  # Volver
                                                    break
                                            else:
                                                print("Opción fuera de rango. Por favor, selecciona un número entre 1 y 4.")
                                        except ValueError:
                                            print("Entrada no válida. Por favor, escribe un número entre 1 y 4.")
                            elif opcion1==2:   # Nueva Asistencia
                                while True:
                                    idEntrenador_var = input('Escribe el Id del Entrenador: ')
                                    if idEntrenador_var.isdigit() and 0 <= len(idEntrenador_var) <= 10:
                                        print("¡El id es válido!")
                                        break
                                    else:
                                        print("El id no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                while True:
                                    idAlumno_var = input('Escribe el Id del Alumno: ')
                                    if idAlumno_var.isdigit() and 0 <= len(idAlumno_var) <= 10:
                                        print("¡El id es válido!")
                                        break
                                    else:
                                        print("El id no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                while True:
                                    fecha_var = input('Escribe la fecha en formato AAAA-MM-DD: ')
                                    formato = "%Y-%m-%d"  # Formato de la fecha esperado
                                    try:
                                        # Intenta convertir la fecha ingresada al formato esperado
                                        fecha_valida = datetime.strptime(fecha_var, formato)
                                        print(f"¡La fecha es válida! ({fecha_valida.strftime('%Y-%m-%d')})")
                                        break
                                    except ValueError:
                                        print("La fecha no es válida. Asegúrate de usar el formato DD-MM-AAAA e intenta de nuevo.")
                                while True:
                                    hora_var = input('Escribe la hora en formato HH:MM (24 horas): ')
                                    formato = "%H:%M"  # Formato de la hora esperado
                                    try:
                                        # Intenta convertir la hora ingresada al formato esperado
                                        hora_valida = datetime.strptime(hora_var, formato)
                                        print(f"¡La hora es válida! ({hora_valida.strftime('%H:%M')})")
                                        break
                                    except ValueError:
                                        print("La hora no es válida. Asegúrate de usar el formato HH:MM (24 horas) e intenta de nuevo.")
                                presentismo = Presentismo(Entrenador_idEntrenador=idEntrenador_var, Alumno_idAlumno=idAlumno_var,
                                                  fecha=fecha_var, hora=hora_var)
                                presentismo_insertado = PresentismoDAO.insertar(presentismo)
                                print(f'Presentismo insertado: {presentismo_insertado}\n')
                            elif opcion1 == 3:  # Volver
                                break
                        else:
                            print("Opción fuera de rango. Por favor, selecciona un número entre 1 y 3.")
                    except ValueError:
                        print("Entrada no válida. Por favor, escribe un número entre 1 y 3.")
            elif opcion == 2:  # alumnos
                opcion1 = None
                while True:
                    print('''Menu:
                    1. Listar Alumnos
                    2. Nuevo Alumno
                    3. Modificar Alumno
                    4. Eliminar Alumno
                    5. Volver
                    ''')
                    try:
                        opcion1 = int(input('Escribe tu opcion ( 1-5 ): '))
                        if 1 <= opcion1 <= 5:
                            if opcion1 == 1:  # Listar
                                opcion2 = None
                                alumnos = AlumnoDAO.seleccionar()
                                if not alumnos:
                                    print("No hay registros de alumnos disponibles")
                                    opcion2=6
                                else:
                                    while True:
                                        print('''Menu:
                                                1. Lista General
                                                2. Lista ascendente por alumno
                                                3. Lista descendente por alumno
                                                4. Lista ascendente por id
                                                5. Lista descendente por id
                                                6. Volver
                                                ''')
                                        try:
                                            opcion2 = int(input('Escribe tu opcion ( 1-6 ): '))
                                            if 1 <= opcion2 <= 6:
                                                if opcion2 == 1:  # Lista General
                                                    alumnos = AlumnoDAO.seleccionar()
                                                    print('\n*** Listado de Alumnos ***')
                                                    for alumno in alumnos:
                                                        print(alumno)
                                                    print()
                                                elif opcion2==2: # Lista ascendente por alumno
                                                    alumnos = AlumnoDAO.seleccionar()
                                                    print('\n*** Listado de Ascendente por Nombre ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    alumnos_ordenados = sorted(alumnos,
                                                                            key=lambda alumno: alumno.nombreAlumno)
                                                    # Imprimir los clientes ordenados
                                                    for alumno in alumnos_ordenados:
                                                        print(alumno)
                                                    print()
                                                elif opcion2==3:  # Lista descendente por alumno
                                                    alumnos = AlumnoDAO.seleccionar()
                                                    print('\n*** Listado Descendenete por Nombre ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    alumnos_ordenados = sorted(alumnos,
                                                                            key=lambda alumno: alumno.nombreAlumno,
                                                                            reverse=True)
                                                    # Imprimir los clientes ordenados
                                                    for alumno in alumnos_ordenados:
                                                        print(alumno)
                                                    print()
                                                elif opcion2==4:  # Lista ascendente por id
                                                    alumnos = AlumnoDAO.seleccionar()
                                                    print('\n*** Listado Ascendente por Id ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    alumnos_ordenados = sorted(alumnos, key=lambda alumno: alumno.idAlumno)
                                                    # Imprimir los clientes ordenados
                                                    for alumno in alumnos_ordenados:
                                                        print(alumno)
                                                    print()
                                                elif opcion2==5:  # Lista descendente por id
                                                    alumnos = AlumnoDAO.seleccionar()
                                                    print('\n*** Listado Descendente por Id ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    alumnos_ordenados = sorted(alumnos, key=lambda alumno: alumno.idAlumno,
                                                                            reverse=True)
                                                    # Imprimir los clientes ordenados
                                                    for alumno in alumnos_ordenados:
                                                        print(alumno)
                                                    print()
                                                elif opcion2==6:
                                                    break
                                            else:
                                                print('Opcion fuera de rango. Por favor seleccione un numero entre 1 y 6')
                                        except ValueError:
                                            print('Entrada no valida. Por favor, escriba un numero entre 1 y 6')
                            elif opcion1==2:   # Nuevo Alumno
                                while True:
                                    nombre_var = input('Escribe el nombre: ')
                                    if nombre_var.isalpha() and 3 <= len(nombre_var) <= 30:
                                        nombre_var = nombre_var.capitalize()  # Capitaliza la primera letra
                                        print("¡La cadena es válida!")
                                        break
                                    else:
                                        print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                while True:
                                    apellido_var = input('Escribe el apellido: ')
                                    if apellido_var.isalpha() and 3 <= len(apellido_var) <= 30:
                                        apellido_var = apellido_var.capitalize()
                                        print("¡La cadena es válida!")
                                        break
                                    else:
                                        print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                while True:
                                    dni_var = input('Escribe el DNI: ')
                                    if dni_var.isdigit() and len(dni_var) == 8:
                                        print("¡El número es válido!")
                                        break
                                    else:
                                        print("El número no es válido(solo dígitos, entre 8 y 10 caracteres). Inténtalo de nuevo.")

                                alumno = Alumno(nombreAlumno=nombre_var, apellidoAlumno=apellido_var,
                                                  dniAlumno=dni_var)
                                alumnos_insertados = AlumnoDAO.insertar(alumno)
                                print(f'Alumnos insertados: {alumnos_insertados}\n')
                            elif opcion1==3:  # Modificar Alumno
                                alumnos = AlumnoDAO.seleccionar()
                                if not alumnos:
                                    print("No hay registros de alumnos disponibles")
                                    opcion=2
                                else:
                                    id_alumno_var = int(input('Escribe el id del alumno a modificar: '))
                                    while True:
                                        nombre_var = input('Escribe el nombre: ')
                                        if nombre_var.isalpha() and 3 <= len(nombre_var) <= 30:
                                            nombre_var = nombre_var.capitalize()  # Capitaliza la primera letra
                                            print("¡La cadena es válida!")
                                            break
                                        else:
                                            print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                    while True:
                                        apellido_var = input('Escribe el apellido: ')
                                        if apellido_var.isalpha() and 3 <= len(apellido_var) <= 30:
                                            apellido_var = apellido_var.capitalize()
                                            print("¡La cadena es válida!")
                                            break
                                        else:
                                            print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                    while True:
                                        dni_var = input('Escribe el dni: ')
                                        if dni_var.isdigit() and len(dni_var) == 8:
                                            print("¡El número es válido!")
                                            break
                                        else:
                                            print("El número no es válido(solo dígitos, entre 8 y 10 caracteres). Inténtalo de nuevo.")
                                    alumno = Alumno(id_alumno_var, nombre_var, apellido_var, dni_var)
                                    alumnos_actualizados = AlumnoDAO.actualizar(alumno)
                                    print(f'Alumnos actualizados: {alumnos_actualizados}\n')
                            elif opcion1==4: # Eliminar Alumno
                                alumnos = AlumnoDAO.seleccionar()
                                if not alumnos:
                                    print("No hay registros de alumnos disponibles")
                                    opcion=2
                                else:
                                    id_alumno_var = int(input('Escribe el id del alumno a eliminar: '))
                                    alumno = Alumno(idAlumno=id_alumno_var)
                                    alumnos_eliminados = AlumnoDAO.eliminar(alumno)
                                    print(f'Alumnos eliminados: {alumnos_eliminados}\n')
                            elif opcion1==5:
                                break
                        else:
                            print('Opcion fuera de rango. Por favor seleccione un numero entre 1 y 5')
                    except ValueError:
                        print('Entrada no valida. Por favor, escribe un numero entre 1 y 4')
            elif opcion == 3:  # Entrenadores
                opcion1 = None
                while True:
                    print('''Menu:
                    1. Listar Entrenador
                    2. Nuevo Entrenador
                    3. Modificar Entrenador
                    4. Eliminar Entrenador
                    5. Volver
                    ''')
                    try:
                        opcion1 = int(input('Escribe tu opcion ( 1-5 ): '))
                        if 1 <= opcion1 <= 5:
                            if opcion1 == 1:  # Listar
                                opcion2 = None
                                entrenadores = EntrenadorDAO.seleccionar()
                                if not entrenadores:
                                    print("No hay registros de entrenadores disponibles")
                                    opcion2=6
                                else:
                                    while True:
                                        print('''Menu:
                                                1. Lista General
                                                2. Lista ascendente por entrenador
                                                3. Lista descendente por entrenador
                                                4. Lista ascendente por id
                                                5. Lista descendente por id
                                                6. Volver
                                                ''')
                                        try:
                                            opcion2 = int(input('Escribe tu opcion ( 1-5 ): '))
                                            if 1<= opcion2 <= 6:
                                                if opcion2 == 1:  # Lista General
                                                    entrenadores = EntrenadorDAO.seleccionar()
                                                    print('\n*** Listado de Entrenadores ***')
                                                    for entrenador in entrenadores:
                                                        print(entrenador)
                                                    print()
                                                elif opcion2 == 2:  # Lista ascendente por entrenador
                                                    entrenadores = EntrenadorDAO.seleccionar()
                                                    print('\n*** Listado de Entrenadores Ascendente por Nombre ***')
                                                    # Ordenar la lista de entrenadores por el atributo 'nombre'
                                                    entrenadores_ordenados = sorted(entrenadores, key=lambda
                                                        entrenador: entrenador.nombreEntrenador)
                                                    # Imprimir los entrenadores ordenados
                                                    for entrenador in entrenadores_ordenados:
                                                        print(entrenador)
                                                    print()
                                                elif opcion2 == 3:  # Lista descendente por entrenador
                                                    entrenadores = EntrenadorDAO.seleccionar()
                                                    print('\n*** Listado de Entrenadores Descendente por Nombres ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    entrenadores_ordenados = sorted(entrenadores, key=lambda
                                                        entrenador: entrenador.nombreEntrenador, reverse=True)
                                                    # Imprimir los clientes ordenados
                                                    for entrenador in entrenadores_ordenados:
                                                        print(entrenador)
                                                    print()
                                                elif opcion2 == 4:  # Lista ascendente por id
                                                    entrenadores = EntrenadorDAO.seleccionar()
                                                    print('\n*** Listado de Entrenadores Ascendente por Id ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    entrenadores_ordenados = sorted(entrenadores, key=lambda
                                                        entrenador: entrenador.idEntrenador)
                                                    # Imprimir los clientes ordenados
                                                    for entrenador in entrenadores_ordenados:
                                                        print(entrenador)
                                                    print()
                                                elif opcion2 == 5:  # Lista descendente por id
                                                    entrenadores = EntrenadorDAO.seleccionar()
                                                    print('\n*** Listado de Entrenadores Descendiente por Id ***')
                                                    # Ordenar la lista de clientes por el atributo 'nombre'
                                                    entrenadores_ordenados = sorted(entrenadores, key=lambda
                                                        entrenador: entrenador.idEntrenador, reverse=True)
                                                    # Imprimir los clientes ordenados
                                                    for entrenador in entrenadores_ordenados:
                                                        print(entrenador)
                                                    print()
                                                elif opcion2==6:
                                                    break
                                            else:
                                                print('Opcion fuera de rango. Por favor seleccione un numero entre 1 y 6')
                                        except ValueError:
                                            print('Entrada no valida. Por favor, escribe un numero entre 1 y 6')
                            elif opcion1 == 2:  # Nuevo entrenador
                                while True:
                                    nombre_var = input('Escribe el nombre: ')
                                    if nombre_var.isalpha() and 3 <= len(nombre_var) <= 30:
                                        nombre_var = nombre_var.capitalize()  # Capitaliza la primera letra
                                        print("¡La cadena es válida!")
                                        break
                                    else:
                                        print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                while True:
                                    apellido_var = input('Escribe el apellido: ')
                                    if apellido_var.isalpha() and 3 <= len(apellido_var) <= 30:
                                        apellido_var = apellido_var.capitalize()
                                        print("¡La cadena es válida!")
                                        break
                                    else:
                                        print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                while True:
                                    dni_var = input('Escribe el DNI: ')
                                    if dni_var.isdigit() and len(dni_var) == 8:
                                        print("¡El número es válido!")
                                        break
                                    else:
                                        print("El número no es válido(solo dígitos, entre 8 y 10 caracteres). Inténtalo de nuevo.")
                                # modificar
                                entrenadores = Entrenador(nombreEntrenador=nombre_var, apellidoEntrenador=apellido_var,
                                                          dniEntrenador=dni_var)
                                entrenadores_insertados = EntrenadorDAO.insertar(entrenadores)  # aca!!
                                print(f'Entrenadores insertados: {entrenadores_insertados}\n')
                            elif opcion1 == 3:  # Modificar entrenador
                                entrenadores = EntrenadorDAO.seleccionar()
                                if not entrenadores:
                                    print("No hay registros de entrenadores disponibles")
                                    opcion=2
                                else:
                                    id_entrenador_var = int(input('Escribe el id del entrenador a modificar: '))
                                    while True:
                                        nombre_var = input('Escribe el nombre: ')
                                        if nombre_var.isalpha() and 3 <= len(nombre_var) <= 30:
                                            nombre_var = nombre_var.capitalize()  # Capitaliza la primera letra
                                            print("¡La cadena es válida!")
                                            break
                                        else:
                                            print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                    while True:
                                        apellido_var = input('Escribe el apellido: ')
                                        if apellido_var.isalpha() and 3 <= len(apellido_var) <= 30:
                                            apellido_var = apellido_var.capitalize()
                                            print("¡La cadena es válida!")
                                            break
                                        else:
                                            print("La cadena no es válida(solo letras, entre 3 y 30 caracteres) Inténtalo de nuevo.")
                                    while True:
                                        dni_var = input('Escribe el dni: ')
                                        if dni_var.isdigit() and len(dni_var) == 8:
                                            print("¡El número es válido!")
                                            break
                                        else:
                                            print("El número no es válido(solo dígitos, entre 8 y 10 caracteres). Inténtalo de nuevo.")
                                    entrenadores = Entrenador(id_entrenador_var, nombre_var, apellido_var, dni_var)
                                    entrenadores_actualizados = EntrenadorDAO.actualizar(entrenadores)
                                    print(f'Entrenadores actualizados: {entrenadores_actualizados}\n')
                            elif opcion1 == 4:  # Eliminar entrenador
                                entrenadores = EntrenadorDAO.seleccionar()
                                if not entrenadores:
                                    print("No hay registros de entrenadores disponibles")
                                    opcion=2
                                else:
                                    id_entrenador_var = int(input('Escribe el id del entrenador a eliminar: '))
                                    entrenadores = Entrenador(idEntrenador=id_entrenador_var)
                                    entrenadores_eliminados = EntrenadorDAO.eliminar(entrenadores)
                                    print(f'Entrenadores eliminados: {entrenadores_eliminados
                                    }\n')
                            elif opcion1 ==5:
                                break
                        else:
                            print('Opcion fuera de rango. Por favor seleccione un numero entre 1 y 5')
                    except ValueError:
                        print('Entrada no valida. Por favor, escriba un numero entre 1 y 5.')
            elif opcion == 4:  # Volver
                print("Saliendo del menú...")
                break
        else:
            print("Opción fuera de rango. Por favor, selecciona un número entre 1 y 4.")
    except ValueError:
        print("Entrada no válida. Por favor, escribe un número entre 1 y 4.")