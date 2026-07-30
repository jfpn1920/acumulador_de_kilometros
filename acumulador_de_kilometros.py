ids = []
conductores = []
placas = []
fechas = []
origenes = []
destinos = []
kilometros = []
tipos_viaje = []
observaciones = []
#---------------------------------------------#
#--|menu_principal_acumulador_de_kilometros|--#
#---------------------------------------------#
while True:
    print("menu principal acumulador de kilometros")
    print("1) crear registro")
    print("2) editar registro")
    print("3) eliminar registro")
    print("4) buscar registro")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #-----------------------#
    #--|crear_kilometraje|--#
    #-----------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_kilometro = 1
        else:
            id_kilometro = ids[-1] + 1
        conductor = input("nombre del conductor: ")
        placa = input("placa del vehículo: ")
        fecha = input("fecha del recorrido: ")
        origen = input("origen del recorrido: ")
        destino = input("destino del recorrido: ")
        kilometro = float(input("kilómetros recorridos: "))
        tipo_viaje = input("tipo de viaje: ")
        observacion = input("observación: ")
        ids.append(id_kilometro)
        conductores.append(conductor)
        placas.append(placa)
        fechas.append(fecha)
        origenes.append(origen)
        destinos.append(destino)
        kilometros.append(kilometro)
        tipos_viaje.append(tipo_viaje)
        observaciones.append(observacion)
        print("kilometraje registrado correctamente.")
        print("id:", id_kilometro)
    #------------------------#
    #--|editar_kilometraje|--#
    #------------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar kilometraje")
            for i in range(len(ids)):
                print(f"{ids[i]} | {conductores[i]} | {placas[i]} | {fechas[i]} | {origenes[i]} | {destinos[i]} | {kilometros[i]} | {tipos_viaje[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {conductores[posicion]} | {placas[posicion]} | {fechas[posicion]} | {origenes[posicion]} | {destinos[posicion]} | {kilometros[posicion]} | {tipos_viaje[posicion]} | {observaciones[posicion]}")
                conductores[posicion] = input("nuevo conductor: ")
                placas[posicion] = input("nueva placa: ")
                fechas[posicion] = input("nueva fecha: ")
                origenes[posicion] = input("nuevo origen: ")
                destinos[posicion] = input("nuevo destino: ")
                kilometros[posicion] = float(input("nuevos kilómetros: "))
                tipos_viaje[posicion] = input("nuevo tipo de viaje: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #--------------------------#
    #--|eliminar_kilometraje|--#
    #--------------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar kilometraje")
            for i in range(len(ids)):
                print(f"{ids[i]} | {conductores[i]} | {placas[i]} | {fechas[i]} | {origenes[i]} | {destinos[i]} | {kilometros[i]} | {tipos_viaje[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {conductores[posicion]} | {placas[posicion]} | {fechas[posicion]} | {origenes[posicion]} | {destinos[posicion]} | {kilometros[posicion]} | {tipos_viaje[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    conductores.pop(posicion)
                    placas.pop(posicion)
                    fechas.pop(posicion)
                    origenes.pop(posicion)
                    destinos.pop(posicion)
                    kilometros.pop(posicion)
                    tipos_viaje.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #------------------------#
    #--|buscar_kilometraje|--#
    #------------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar kilometraje")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {conductores[posicion]} | {placas[posicion]} | {fechas[posicion]} | {origenes[posicion]} | {destinos[posicion]} | {kilometros[posicion]} | {tipos_viaje[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = kilometros[0]
            menor = kilometros[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {conductores[i]} | {placas[i]} | {fechas[i]} | {origenes[i]} | {destinos[i]} | {kilometros[i]} | {tipos_viaje[i]} | {observaciones[i]}")
                suma += kilometros[i]
                if kilometros[i] > mayor:
                    mayor = kilometros[i]
                if kilometros[i] < menor:
                    menor = kilometros[i]
            promedio = suma / len(ids)
            print("estadísticas acumulador de kilómetros")
            print("cantidad de registros:", len(ids))
            print("kilómetros acumulados:", suma)
            print("promedio de kilómetros:", round(promedio, 2))
            print("mayor recorrido:", mayor)
            print("menor recorrido:", menor)
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el programa.")
        break
    else:
        print("opción inválida.")