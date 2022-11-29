# consultoriomedico
 
"""En nuestra proyecto, pagina web:
1. para ingresar a nuestro proyecto tiene que copiar en el URL consultorio/

2. Nuestro proyecto cuenta con 4  modelos que son: Paciente, Administrador, Enfermero, Medico

3. En nuestro template padre tenemos un nav, header, una herencia de template y un footer
 3.1 En el nav tenemos los navbar para accesos mas rapido a los diferentes modelos (Pacientes, Medicos, Enfermeros, Administrativos)
 3.2 En el header tenemos nuestro logo o nombre del consultorio
 3.3 Nuestra herencia de padres es lo que modificamos para nuestros diferentes templates

4. En nuestro template (Pacientes, Medicos, Enfermeros, Administrativos) tenemos una lista que recorremos con un bucle for
 4.1 Cada template tiene un href para agregar (Pacientes, Medicos, Enfermeros, Administrativos) mediante un formulario a nuestra base de datos
 4.2 En la URL 'inicio' tenemos un href para buscar por expediente a un paciente.
 4.3 En la URL 'listaPaciente' tenemos un href, para poder recorrer cada ítem de la lista, así como también un href para la edición de los mismos. Otra opción que podemos encontrar    dentro de la misma url es la de eliminar individualmente cualquier elemento de la lista. Además, siendo usuario autorizado, se pueden crear nuevos registros.
  4.4 En la URL 'listaMedicos' tenemos un href, para poder recorrer cada ítem de la lista, así como también un href para la edición de los mismos. Otra opción que podemos encontrar dentro de la misma url es la de eliminar individualmente cualquier elemento de la lista. Además, siendo usuario autorizado, se pueden crear nuevos registros.
  4.5 En la URL 'listaEnfermeros' tenemos un href, para poder recorrer cada ítem de la lista, así como también un href para la edición de los mismos. Otra opción que podemos encontrar dentro de la misma url es la de eliminar individualmente cualquier elemento de la lista. Además, siendo usuario autorizado, se pueden crear nuevos registros.
  4.6 En la URL 'listaAdministrativo' tenemos un href, para poder recorrer cada ítem de la lista, así como también un href para la edición de los mismos. Otra opción que podemos encontrar dentro de la misma url es la de eliminar individualmente cualquier elemento de la lista. Además, siendo usuario autorizado, se pueden crear nuevos registros.

5. Utilizando el siguiente link, se puede acceder a una vista de cómo funciona nuestra página: https://youtu.be/JM_Ydo3UDvQ

 """