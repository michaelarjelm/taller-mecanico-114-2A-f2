from conectar import crear_conexion
from dao.marca_dao import MarcaDAO
from model.marca import Marca
from model.repuesto import Repuesto
from servicios.miinidicador import MiIndicador
import sys

def menu():
    print("\n" + "="*30)
    print("   MANTENEDOR DE MARCAS Y REPUESTOS")
    print("="*30)
    print("1. Crear una Marca")
    print("2. Listar todas las Marcas")
    print("3. Buscar una Marca por ID")
    print("4. Actualizar una Marca")
    print("5. Eliminar una Marca")
    print("6. Cotizar Repuesto")
    print("7. Salir")
    print("="*30)
    return input("Seleccione una opción: ")

def main():
    try:
        conexion = crear_conexion()
        marca_dao = MarcaDAO(conexion)
        # Asegurarnos que la tabla exista antes de operar
        marca_dao.crear_tabla()
        conexion.commit()
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        sys.exit(1)

    while True:
        opcion = menu()

        if opcion == '1':
            print("\n--- CREAR MARCA ---")
            nombre = input("Ingrese el nombre de la nueva marca: ").strip()
            if nombre:
                nueva_marca = Marca(nombre)
                marca_dao.insertar(nueva_marca)
                print(f"✅ Marca '{nueva_marca.nombre}' creada con éxito. ID asignado: {nueva_marca.id}")
            else:
                print("❌ El nombre de la marca no puede estar vacío.")

        elif opcion == '2':
            print("\n--- LISTADO DE MARCAS ---")
            marcas = marca_dao.listar()
            if marcas:
                print(f"{'ID':<5} | {'NOMBRE'}")
                print("-" * 25)
                for marca in marcas:
                    print(f"{marca.id:<5} | {marca.nombre}")
            else:
                print("ℹ️ No hay marcas registradas en el sistema.")

        elif opcion == '3':
            print("\n--- BUSCAR MARCA ---")
            try:
                id_buscar = int(input("Ingrese el ID de la marca a buscar: "))
                marca = marca_dao.buscar(id_buscar)
                if marca:
                    print(f"✅ Marca encontrada - ID: {marca.id}, Nombre: {marca.nombre}")
                else:
                    print(f"❌ No se encontró ninguna marca con el ID {id_buscar}.")
            except ValueError:
                print("❌ Por favor, ingrese un ID numérico válido.")

        elif opcion == '4':
            print("\n--- ACTUALIZAR MARCA ---")
            try:
                id_actualizar = int(input("Ingrese el ID de la marca que desea actualizar: "))
                marca_existente = marca_dao.buscar(id_actualizar)
                
                if marca_existente:
                    print(f"Marca actual: {marca_existente.nombre}")
                    nuevo_nombre = input("Ingrese el nuevo nombre de la marca: ").strip()
                    if nuevo_nombre:
                        marca_existente = Marca(nuevo_nombre) # Instancia nueva ya que no tenemos setter de nombre en el modelo
                        marca_existente.id = id_actualizar
                        
                        resultado = marca_dao.actualizar(marca_existente)
                        if resultado:
                            print(f"✅ Marca actualizada correctamente a: '{resultado.nombre}'")
                        else:
                            print("❌ Ocurrió un error al intentar actualizar la marca.")
                    else:
                        print("❌ El nuevo nombre no puede estar vacío.")
                else:
                    print(f"❌ No se encontró ninguna marca con el ID {id_actualizar}.")
            except ValueError:
                print("❌ Por favor, ingrese un ID numérico válido.")

        elif opcion == '5':
            print("\n--- ELIMINAR MARCA ---")
            try:
                id_eliminar = int(input("Ingrese el ID de la marca a eliminar: "))
                marca_existente = marca_dao.buscar(id_eliminar)
                
                if marca_existente:
                    confirmacion = input(f"¿Está seguro de eliminar la marca '{marca_existente.nombre}' (S/N)?: ").strip().upper()
                    if confirmacion == 'S':
                        eliminado = marca_dao.eliminar(id_eliminar)
                        if eliminado:
                            print("✅ Marca eliminada con éxito.")
                        else:
                            print("❌ Ocurrió un error al intentar eliminar la marca.")
                    else:
                        print("ℹ️ Operación cancelada.")
                else:
                    print(f"❌ No se encontró ninguna marca con el ID {id_eliminar}.")
            except ValueError:
                print("❌ Por favor, ingrese un ID numérico válido.")

        elif opcion == '6':
            print("\n--- COTIZAR REPUESTO ---")
            codigo = input("Ingrese el código del repuesto: ").strip()
            nombre = input("Ingrese el nombre del repuesto: ").strip()
            try:
                precio = float(input("Ingrese el precio del repuesto en origen: "))
            except ValueError:
                print("❌ Precio inválido.")
                continue

            es_importado = input("¿El repuesto es importado? (S/N): ").strip().upper() == 'S'
            fecha_cotizacion = input("Ingrese la fecha (DD-MM-YYYY) o presione Enter para el valor de hoy: ").strip()
            
            # Instanciar el repuesto (asumimos un stock ficticio de 1 para este ejemplo)
            repuesto = Repuesto(codigo, nombre, 1, es_importado, precio)
            
            print("Consultando el valor del dólar...")
            try:
                servicio = MiIndicador()
                dolar = servicio.obtener_valor("dolar", fecha_cotizacion if fecha_cotizacion else None)
                
                if fecha_cotizacion:
                    print(f"Valor del dólar el {fecha_cotizacion}: ${dolar}")
                else:
                    print(f"Valor del dólar hoy: ${dolar}")
                
                precio_final = repuesto.precio_en_pesos(dolar)
                
                print("\n--- RESUMEN COTIZACIÓN ---")
                print(f"Repuesto: {repuesto.nombre} (Cod: {repuesto.codigo})")
                print(f"Importado: {'Sí' if repuesto.es_importado else 'No'}")
                print(f"Precio Base: {precio}")
                print(f"Precio Final en Pesos: ${precio_final}")
                print("--------------------------")
                
            except Exception as e:
                print(f"❌ Error al consultar la API o calcular el precio: {e}")

        elif opcion == '7':
            print("\nCerrando sistema... ¡Hasta luego!")
            conexion.close()
            break
            
        else:
            print("\n❌ Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
