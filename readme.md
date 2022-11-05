Para clonar nuestro proyecto debes seguir estos pasos:
1. Ejecutar en tu terminal: git clone https://github.com/JorPallero/Entrega1_Puchurri_Santini_Pallero.git
2. Una vez clonado recuerda abrir la carpeta del proyecto clonado!
3. Crear tu entorno virtual y llamarlo 'venv' (python -m venv venv).  Si quieres puedes chequear que tu entorno quedó creado dentro del proyecto ejecutando en tu terminal: ls.  Deberías poder ver la carpeta del proyecto, la del entorno virtual, la de la aplicación 'home' y los archivos manage.py y requirements.txt
4. Activar tu entorno virtual: . venv/Scripts/Activate
5. Instalar los paquetes requeridos ejecutando: pip install -r requirements.txt
6. Ejecuta en tu terminal: python manage.py migratations.  Luego: python manage.py migrate.
7. Para levantar el proyecto puedes ejecutar: python manage.py runserver  
8. Listo!  Ya puedes navegar en tu página!
9. Aún está en construcción pero puedes ingresar a la sección 'Vehículos' y hacer click en "Crear Vehiculo", ingresar un modelo, una marca, un color, años de antiguedad y fecha de fabricación (optativo) y crear un registro en tu base de datos. Luego se mostrarán todos los registros creados al momento teniendo la posibilidad de hacer una búsqueda por marca (total o parcialmente coincidente en carácteres). 
10. La sección Clientes está en etapa de mejora.
11. En 'About' podrás conocer más acerca de nosotros.
12. Próximamente en 'Contact' agregaremos un formulario de contacto pero hasta entonces puedes escribirnos al mail allí detallado.
13. Para acceder al perfil de administrador el usuario es "admin" y la contraseña "123".
14. Ya se pueden registrar usuarios. Los mismos tienen derechos para Crear, editar y elimninar Clientes; como así también agregar Vehículos a la lista.
