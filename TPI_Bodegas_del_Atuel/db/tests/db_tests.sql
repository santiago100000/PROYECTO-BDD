-- =============================================================================
-- db/tests/db_tests.sql — Pruebas SQL por regla de negocio (RN-01 a RN-15)
-- Cada sección contiene:
--   - Caso que debe funcionar
--   - Caso que debe fallar (con error esperado en comentario)
--   - TODO (grupo): implementar la prueba real
-- =============================================================================

-- -----------------------------------------------------------------------------
-- RN-01: El precio de un vino es único para toda la red de salas y siempre mayor que cero.
-- Mecanismo esperado: Atributo en vino + CHECK
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de vino con precio > 0

-- Caso que debe fallar (error esperado: violación de CHECK precio > 0):
-- TODO (grupo): INSERT de vino con precio <= 0

-- -----------------------------------------------------------------------------
-- RN-02: Una sala pertenece a una sola localidad. Cada localidad tiene un único encargado regional.
-- Mecanismo esperado: FK + diseño normalizado (3FN)
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de sala con localidad válida

-- Caso que debe fallar (error esperado: violación de FK localidad):
-- TODO (grupo): INSERT de sala con localidad inexistente

-- -----------------------------------------------------------------------------
-- RN-03: Cada empleado trabaja en una sola sala.
-- Mecanismo esperado: FK NOT NULL
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de empleado con sala válida

-- Caso que debe fallar (error esperado: violación de FK sala o NOT NULL):
-- TODO (grupo): INSERT de empleado con sala inexistente o sin sala

-- -----------------------------------------------------------------------------
-- RN-04: Una parcela tiene una sola cepa y se cosecha como máximo una vez por campaña.
-- Mecanismo esperado: FK + UNIQUE (parcela, campaña)
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de lote con parcela y campaña únicas

-- Caso que debe fallar (error esperado: violación de UNIQUE (parcela, campaña)):
-- TODO (grupo): INSERT de segundo lote para misma parcela y campaña

-- -----------------------------------------------------------------------------
-- RN-05: Los porcentajes de corte de un vino suman exactamente 100.
-- Mecanismo esperado: Constraint trigger diferido
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de composiciones que sumen 100 dentro de una transacción

-- Caso que debe fallar (error esperado: violación de constraint trigger suma=100):
-- TODO (grupo): INSERT de composiciones que no sumen 100 al COMMIT

-- -----------------------------------------------------------------------------
-- RN-06: El descuento depende del tipo de cliente: socio 10 %, distribuidor 20 %, exportador 30 %.
-- Mecanismo esperado: Función de descuento + CHECK de rango
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de cliente con descuento válido según tipo

-- Caso que debe fallar (error esperado: violación de CHECK rango de descuento):
-- TODO (grupo): INSERT de cliente con descuento fuera del rango permitido

-- -----------------------------------------------------------------------------
-- RN-07: Un exportador puede tener varios permisos; el vencimiento es posterior a la emisión.
-- Mecanismo esperado: Tabla de permisos + CHECK entre columnas
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de permiso con vencimiento > emisión

-- Caso que debe fallar (error esperado: violación de CHECK vencimiento > emisión):
-- TODO (grupo): INSERT de permiso con vencimiento <= emisión

-- -----------------------------------------------------------------------------
-- RN-08: El total del comprobante es la suma de sus renglones con el descuento aplicado. No se carga a mano.
-- Mecanismo esperado: Función de cálculo + trigger
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de renglón y verificar total calculado por trigger

-- Caso que debe fallar (error esperado: intento de asignar total manualmente):
-- TODO (grupo): UPDATE de total comprobante rechazado por trigger

-- -----------------------------------------------------------------------------
-- RN-09: No se puede vender más de lo que hay en stock de la sala. El stock nunca es negativo.
-- Mecanismo esperado: Trigger BEFORE INSERT + CHECK (cantidad >= 0)
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de renglón de venta con stock suficiente

-- Caso que debe fallar (error esperado: stock insuficiente / stock negativo):
-- TODO (grupo): INSERT de renglón de venta que exceda stock de sala

-- -----------------------------------------------------------------------------
-- RN-10: Sólo un ingreso terminado impacta en el depósito y pasa a procesado. Las transiciones son
--        en_confeccion → terminado → procesado y no retroceden.
-- Mecanismo esperado: Tipo ENUM + trigger de estados + procedimiento
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): LLAMAR sp_procesar_ingreso con ingreso en estado terminado

-- Caso que debe fallar (error esperado: transición de estado inválida):
-- TODO (grupo): Intentar pasar de procesado a en_confeccion

-- -----------------------------------------------------------------------------
-- RN-11: Igual que RN-10 para transferencias. La fecha de confección es la actual y no se puede modificar.
-- Mecanismo esperado: Trigger de estados y de fecha + procedimiento
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): LLAMAR sp_procesar_transferencia con transferencia válida

-- Caso que debe fallar (error esperado: intento de modificar fecha de confección):
-- TODO (grupo): UPDATE de fecha_confección en transferencia ya creada

-- -----------------------------------------------------------------------------
-- RN-12: Un ingreso o una transferencia que no está en confección no admite agregar,
--        modificar ni quitar renglones.
-- Mecanismo esperado: Trigger sobre los renglones
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de renglón en ingreso en estado en_confeccion

-- Caso que debe fallar (error esperado: documento no está en confección):
-- TODO (grupo): INSERT de renglón en ingreso en estado terminado o procesado

-- -----------------------------------------------------------------------------
-- RN-13: Todo cambio de precio de un vino queda auditado (fecha, usuario, precio anterior y nuevo).
-- Mecanismo esperado: Trigger AFTER UPDATE + tabla de auditoría
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): UPDATE de precio de vino y verificar fila en auditoría

-- Caso que debe fallar (error esperado: trigger de auditoría impide operación):
-- TODO (grupo): UPDATE de precio sin contexto de usuario válido (si aplica)

-- -----------------------------------------------------------------------------
-- RN-14: No se puede borrar un transportista, una bodega ni un vino que tengan movimientos asociados.
-- Mecanismo esperado: FK con ON DELETE RESTRICT
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): DELETE de transportista sin movimientos asociados

-- Caso que debe fallar (error esperado: violación de FK ON DELETE RESTRICT):
-- TODO (grupo): DELETE de bodega con vinos asociados

-- -----------------------------------------------------------------------------
-- RN-15: Cantidades, superficies, kilos y precios son siempre positivos.
--        La graduación está entre 5 y 20.
-- Mecanismo esperado: CHECK
-- -----------------------------------------------------------------------------
-- Caso que debe funcionar:
-- TODO (grupo): INSERT de lote con kg > 0 y graduación entre 5 y 20

-- Caso que debe fallar (error esperado: violación de CHECK kg > 0 o graduación 5-20):
-- TODO (grupo): INSERT de lote con kg <= 0 o graduación fuera de rango

-- -----------------------------------------------------------------------------
-- Demostración de concurrencia (dos sesiones)
-- -----------------------------------------------------------------------------
-- Caso: dos sesiones psql intentan vender la última botella de un vino al mismo tiempo.
-- Sesión A (con SELECT ... FOR UPDATE):
--   BEGIN;
--   SELECT cantidad FROM stock_sala WHERE sala_id = X AND vino_id = Y FOR UPDATE;
--   -- Si cantidad >= 1, INSERT renglón de venta y actualizar stock
--   COMMIT;
-- Sesión B (sin SELECT ... FOR UPDATE):
--   BEGIN;
--   SELECT cantidad FROM stock_sala WHERE sala_id = X AND vino_id = Y;
--   -- Lee la misma cantidad que A, intenta vender
--   COMMIT;
-- Resultado esperado: con FOR UPDATE, una de las dos espera y luego ve stock 0 (falla).
-- Sin FOR UPDATE, ambas pueden leer stock 1 y ambas venden (race condition), provocando
-- stock negativo o violación de CHECK, según el nivel de aislamiento.
-- Nivel de aislamiento sugerido: READ COMMITTED por defecto; SERIALIZABLE para detectar
-- conflictos de escritura y forzar reintento (40001/40P01 → 503 en la API).
-- TODO (grupo): implementar la demostración con dos sesiones psql reales.
