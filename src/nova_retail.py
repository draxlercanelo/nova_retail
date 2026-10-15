"""Módulo para procesar vehículos."""


def procesar_vehiculo(codigo_producto, cantidad, stock_actual, precio_unitario, igv_porcentaje):
    """Procesa una venta de vehículo y actualiza el stock."""
    if stock_actual < cantidad:
        print("Sin stock suficiente")
        return None

    subtotal = precio_unitario * cantidad
    igv = subtotal * igv_porcentaje
    total = subtotal + igv

    nuevo_stock = stock_actual - cantidad
    print("Venta registrada:", codigo_producto, total)

    return total, nuevo_stock
