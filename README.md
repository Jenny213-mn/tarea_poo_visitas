# Sistema de Registro de Visitantes

Aplicación de escritorio desarrollada en Python utilizando Tkinter, implementando arquitectura modular por capas (Modelos, Servicios, UI y Main).

## Descripción
Este sistema permite gestionar el registro de visitantes en una oficina mediante operaciones CRUD (Crear, Leer y Eliminar), manteniendo la información en memoria.

## Cómo ejecutar el programa 
1. Abrir la carpeta del proyecto.
2. Ejecutar el archivo principal:

## Funcionalidades
- Registrar nuevos visitantes
- Visualizar visitantes en una tabla
- Eliminar registros seleccionados
- Limpiar campos del formulario
- Validación de datos (campos obligatorios y cédula única)

## Arquitectura del Proyecto
El proyecto está organizado de la siguiente manera:

visitas_app/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py


## 👩‍💻 Autor
- Jenny Carolina Manzano Narváez