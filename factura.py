## 📚 Programa de Facturación de Venta de Libros 📖

# --- ARREGLOS UNIDIMENSIONALES (Listas Paralelas) ---
nombres_clientes = []
apellidos_clientes = []
cantidades_libros = []
precios_unitarios = []
totales_pagar = [] # Arreglo para registrar el total final de cada cliente


# --- FUNCIONES DE CÁLCULO ---

def calcular_descuento(cantidad_libros):
    """Determina el porcentaje de descuento según la cantidad de libros."""
    
    # NOTA: En los requisitos se menciona "trajes", pero se asume que se refiere a "libros"
    
    if cantidad_libros == 1:
        return 0.05  # 5%
    else:
        if 2 <= cantidad_libros <= 3:
             return 0.10  # 10%
        else:
            if 4 <= cantidad_libros <= 5:
                 return 0.30  # 30%
            else: 
                if cantidad_libros >= 6:
                     return 0.40  # 40%
                else:
                    return 0.00  # 0% si la cantidad es 0 (aunque se valida que sea > 0)

def procesar_compra():
    """Realiza la entrada de datos, cálculos y almacena el registro de una compra."""
    
    print("\n" + "="*40)
    print("         REGISTRO DE NUEVA VENTA")
    print("               MI COMISARIATO   ")
    print("="*40)
    
    # 1. Entrada de Datos del Cliente
    nombre = input("Ingresar el nombre del cliente: ").strip()
    apellido = input("Ingresar el apellido del cliente: ").strip()
    
    while True:
        try:
            cantidad = int(input("Ingresar la cantidad de libros a comprar: "))
            precio = float(input("Ingresar el precio unitario de los libros: $"))
            
            if cantidad <= 0 or precio <= 0:
                print("🔴ERROR: Las cantidades ingresadas deben ser mayores a cero. Intentelo de nuevo.")
                continue
            
            break
        except ValueError:
            print("🔴ERROR: Ingrese un número válido en1" \
            " cantidad o el precio.")

    # 2. Cálculos
    
    # Subtotal antes del descuento
    subtotal = cantidad * precio
    
    # Porcentaje de descuento
    porcentaje_descuento = calcular_descuento(cantidad)
    
    # Monto del descuento aplicado
    monto_descuento = subtotal * porcentaje_descuento
    
    # Total a pagar
    total_a_pagar = subtotal - monto_descuento
    
    # 3. Almacenamiento en Arreglos
    nombres_clientes.append(nombre)
    apellidos_clientes.append(apellido)
    cantidades_libros.append(cantidad)
    precios_unitarios.append(precio)
    totales_pagar.append(total_a_pagar)
    
    print("\n--- Resumen de Venta ---")
    print(f"Subtotal antes de descuento: ${subtotal:,.2f}")
    print(f"Descuento aplicado: {porcentaje_descuento*100:.0f}%")
    print(f"Monto descontado: ${monto_descuento:,.2f}")
    print(f"✅ TOTAL A PAGAR: ${total_a_pagar:,.2f}")
    print("------------------------")


# --- PROGRAMA PRINCIPAL ---

def ejecutar_sistema_ventas():
    
    print("--- Sistema de Registro de Ventas de Libros ---")
    
    # Pre-ciclo: Preguntar cuántas ventas se desean realizar
    while True:
        try:
            num_ventas = int(input("¿Cuántas ventas desea registrar? "))
            if num_ventas < 1:
                print("Debe registrar al menos una venta.")
                continue
            break
        except ValueError:
            print("⚠️ Ingrese un número entero válido.")
            
    # Ciclo WHILE para registrar múltiples clientes
    i = 0
    while i < num_ventas:
        print(f"\nVENTA NÚMERO {i + 1} de {num_ventas}")
        procesar_compra()
        i += 1

    # --- Procesamiento Final ---
    if not nombres_clientes:
        print("\n❌ No se registraron ventas. Fin del programa.")
        return

    print("\n\n" + "#"*60)
    print("          📊 REPORTE FINAL DE VENTAS REGISTRADAS 📊")
    print("#"*60)
    
    # 1. Mostrar la información de cada compra registrada
    mostrar_informacion_compras()
    
    # 2. Cálculos estadísticos
    realizar_analisis_ventas()
    
    print("\n¡Gracias por usar el sistema!")


# --- FUNCIONES DE REPORTE ---

def mostrar_informacion_compras():
    """Imprime el detalle de todas las ventas registradas."""
    print("\n## 📋 Detalle de Compras")
    print(f"{'#':<3} | {'CLIENTE':<20} | {'CANT.':<5} | {'P. UNIT.':<10} | {'TOTAL A PAGAR':>15}")
    print("-" * 60)
    
    # Iterar sobre los arreglos usando el índice para reconstruir el registro
    for i in range(len(nombres_clientes)):
        nombre_completo = f"{nombres_clientes[i]} {apellidos_clientes[i]}"
        
        print(
            f"{i+1:<3} | {nombre_completo:<20} | {cantidades_libros[i]:<5} | "
            f"${precios_unitarios[i]:<9.2f} | ${totales_pagar[i]:>14.2f}"
        )
    print("-" * 60)

def realizar_analisis_ventas():
    """Calcula y muestra el promedio, la venta más alta y la más baja."""
    
    print("\n## 📈 Resumen Estadístico")
    
    # Calcular el promedio de ventas
    total_acumulado = sum(totales_pagar)
    num_ventas = len(totales_pagar)
    promedio_ventas = total_acumulado / num_ventas
    
    print(f"Número total de ventas registradas: **{num_ventas}**")
    print(f"Total acumulado de ventas: **${total_acumulado:,.2f}**")
    print(f"Promedio de ventas realizadas: **${promedio_ventas:,.2f}**")
    
    # Determinar la venta más alta y la más baja
    venta_maxima = max(totales_pagar)
    venta_minima = min(totales_pagar)
    
    # Encontrar los índices (y por lo tanto, el cliente) de estas ventas
    idx_max = totales_pagar.index(venta_maxima)
    idx_min = totales_pagar.index(venta_minima)
    
    cliente_max = f"{nombres_clientes[idx_max]} {apellidos_clientes[idx_max]}"
    cliente_min = f"{nombres_clientes[idx_min]} {apellidos_clientes[idx_min]}"
    
    print("\n--- Ventas Extremas ---")
    print(f"Venta más alta ({cliente_max}): **${venta_maxima:,.2f}**")
    print(f"Venta más baja ({cliente_min}): **${venta_minima:,.2f}**")
    
# Ejecutar el programa principal
if __name__ == "__main__":
    ejecutar_sistema_ventas()