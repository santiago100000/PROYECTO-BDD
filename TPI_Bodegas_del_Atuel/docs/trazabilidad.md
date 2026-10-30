# Trazabilidad de Reglas de Negocio

| RN | Regla | Mecanismo esperado (PDF) | Mecanismo implementado | Caso de prueba |
|----|-------|-------------------------|------------------------|----------------|
| RN-01 | Precio de vino único y > 0 | Atributo + CHECK | TODO | TODO |
| RN-02 | Sala en una localidad; localidad con encargado único | FK + 3FN | TODO | TODO |
| RN-03 | Empleado en una sola sala | FK NOT NULL | TODO | TODO |
| RN-04 | Parcela con una cepa; cosecha 1 por campaña | FK + UNIQUE (parcela, campaña) | TODO | TODO |
| RN-05 | Porcentajes de corte suman 100 | Constraint trigger diferido | TODO | TODO |
| RN-06 | Descuento por tipo de cliente | Función + CHECK rango | TODO | TODO |
| RN-07 | Permisos de exportador; vencimiento > emisión | Tabla permisos + CHECK columnas | TODO | TODO |
| RN-08 | Total = suma renglones con descuento | Función + trigger | TODO | TODO |
| RN-09 | No vender más stock; stock >= 0 | Trigger BEFORE + CHECK | TODO | TODO |
| RN-10 | Transiciones ingreso en_confeccion→terminado→procesado | ENUM + trigger + procedimiento | TODO | TODO |
| RN-11 | Idem para transferencias; fecha confección = actual | Trigger estados + fecha + procedimiento | TODO | TODO |
| RN-12 | Renglones solo si documento en confección | Trigger sobre renglones | TODO | TODO |
| RN-13 | Auditoría de precio de vino | Trigger AFTER UPDATE + tabla | TODO | TODO |
| RN-14 | No borrar transportista/bodega/vino con movimientos | FK ON DELETE RESTRICT | TODO | TODO |
| RN-15 | Cantidades/kilos/precios > 0; graduación 5-20 | CHECK | TODO | TODO |
