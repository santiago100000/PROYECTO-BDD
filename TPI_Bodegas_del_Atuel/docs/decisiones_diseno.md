# Decisiones de Diseño

Cinco decisiones obligatorias de la sección 5:

1. **Jerarquía de clientes**: tabla única con columna de tipo, una tabla por subtipo, o supertipo más subtipos.
2. **Claves naturales o subrogadas**: CUIT y código postal frente a identificadores autogenerados.
3. **Tipos de datos**: NUMERIC(p,s) para dinero (nunca FLOAT), DATE/TIMESTAMP para fechas, ENUM para estados.
4. **Atributos derivados**: subtotales, totales y descuento — cuáles se almacenan y cuáles se calculan.
5. **Acciones referenciales**: ON DELETE y ON UPDATE de cada FK (RESTRICT en movimientos, CASCADE solo en renglones).

Cada decisión debe incluir ventajas, desventajas y la justificación de la opción elegida.
