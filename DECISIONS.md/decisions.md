## Fecha: 06/10/2026

### Decisions

Se dividió la función `procesar_vehiculo` en tres funciones auxiliares:

- `verificar_stock`: valida que exista suficiente stock antes de realizar la venta.
- `calcular_subtotal`: calcula el subtotal multiplicando el precio unitario por la cantidad.
- `calcular_igv`: calcula el IGV correspondiente al subtotal.

La función `procesar_vehiculo` mantiene la responsabilidad de coordinar el proceso completo de venta, calcular el total, actualizar el stock y registrar la operación.

### Justificación

El criterio arquitectónico utilizado fue el principio de **Responsabilidad Única (SRP)**. Cada función realiza una tarea específica y claramente definida, evitando concentrar toda la lógica en una sola función.

Esta división mejora la legibilidad, facilita las pruebas unitarias, permite reutilizar las operaciones de cálculo y hace que el código sea más sencillo de mantener y modificar.

La separación también permite detectar y corregir errores de forma independiente en cada etapa del proceso de venta.
