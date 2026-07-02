# Sistema de Facturación - Modulación de Facturación

Este proyecto corresponde al desarrollo grupal de un sistema automatizado para la gestión y modulación de facturación, desarrollado para la materia de Programación II de la Universidad Nacional de Chimborazo. El sistema está diseñado para estructurar el proceso de ventas, aplicar normativas fiscales vigentes y garantizar la persistencia de datos mediante el uso de herramientas externas.

---

## Integrantes del Grupo
* Lisseth Tapia
* Sebastián Llanos
* Fabio Machado
* Antony Parreño
* Jonathan Sagñay

---

## Descripción del Proyecto
El objetivo principal del proyecto es el diseño e implementación de un módulo de facturación robusto y eficiente. El sistema permite procesar transacciones comerciales calculando subtotales, aplicando descuentos específicos y desglosando impuestos de manera precisa. Además, incluye la capacidad de exportar e integrar los registros con hojas de cálculo para facilitar la auditoría y el control financiero.

---

## Arquitectura y Funcionalidades Principales

### 1. Módulo de Registro y Control
* **Gestión de Clientes:** Almacenamiento de datos esenciales como nombres, apellidos, número de cédula o RUC y datos de contacto.
* **Control de Productos:** Catálogo de artículos disponibles con sus respectivos precios unitarios y niveles de inventario.

### 2. Lógica de Facturación (Cálculos Financieros)
* **Procesamiento de Ventas:** Generación de facturas detalladas por cada transacción efectuada.
* **Cálculo Automatizado:** Determinación exacta del subtotal, cálculo del Impuesto al Valor Agregado (IVA) aplicable y desglose del valor total neto a pagar.

### 3. Persistencia de Datos e Integración con Excel
* **Almacenamiento Local:** Registro permanente de cada factura emitida en archivos estructurados.
* **Compatibilidad con Hojas de Cálculo:** Exportación de reportes financieros en formato CSV, asegurando una apertura e interpretación nativa y ordenada dentro de Microsoft Excel.

---

