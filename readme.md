Para clonar nuestro proyecto debes seguir estos pasos:
1. Ejecutar en tu terminal: git clone https://github.com/JorPallero/Entrega1_Puchurri_Santini_Pallero.git
2. Una vez clonado recuerda abrir la carpeta del proyecto clonado!
3. Crear tu entorno virtual y llamarlo 'venv' (python -m venv venv).  Si quieres puedes chequear que tu entorno quedó creado dentro del proyecto ejecutando en tu terminal: ls.  Deberías poder ver la carpeta del proyecto, la del entorno virtual, la de la aplicación 'home' y los archivos manage.py y requirements.txt
4. Activar tu entorno virtual: . venv/Scripts/Activate
5. Instalar los paquetes requeridos ejecutando: pip install -r requirements.txt
6. Ejecuta en tu terminal: python manage.py migratations.  Luego: python manage.py migrate.
7. Para levantar el proyecto puedes ejecutar: python manage.py runserver  
8. Listo!  Ya puedes navegar en tu página!
9. Antes que nada debes registrarte para poder ejecutar acciones.  Debes dirigirte a "Registrarse" e indicando Usuario, email y contraseña puedes crear un usuario.
10. Luego puedes loguearte accediendo desde "Iniciar sesión".
11. Una vez dentro ya puedes ir a las secciones "Vehículos" y/o "Clientes" y crear registros eligiendo la opción "Crear Vehículo" o "Crear Cliente" dependiendo de la sección donde te encuentres.
12. En "Vehiculos" se pueden visualizar todos los registros creados y tienes la posibilidad de Buscar registros por medio del campo "Marca" (total o parcialmente coincidente en carácteres).
13. En "Clientes" además de crearlos puedes buscar registros a través del campo "Apellido".
14. Para crear registros debes estar logueado, no asi para verlos o para buscarlos.
15. Además puedes agregar datos a tu perfil: "Nombre", "Apellido", "Descripción", "Link Página", un avatar. También puedes modificarlos, incluyendo tu email y tu contraseña.
16. En 'About' podrás conocer más acerca de nosotros.
17. Próximamente en 'Contact' agregaremos un formulario de contacto pero hasta entonces puedes escribirnos al mail allí detallado.
18. Puedes crear un usuario de administrador ejecutando en tu terminal: python manage.py createsuperuser

