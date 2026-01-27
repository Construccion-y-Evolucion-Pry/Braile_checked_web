Introducción
============

¿Qué es el Sistema Braille?
----------------------------

El sistema Braille es un sistema de escritura táctil utilizado por personas ciegas 
o con discapacidad visual. Fue creado por Louis Braille en 1824 y utiliza patrones 
de puntos en relieve para representar letras, números y símbolos.

Sobre este Proyecto
--------------------

Este proyecto es una aplicación web desarrollada con Flask que permite convertir 
texto normal a símbolos Braille Unicode de manera rápida y sencilla.

Objetivos
---------

* Facilitar la conversión de texto a Braille
* Proporcionar una interfaz web accesible y fácil de usar
* Ofrecer una API REST para integración con otras aplicaciones
* Contribuir a la accesibilidad digital

Tecnologías Utilizadas
-----------------------

**Backend:**

* Python 3.7+
* Flask 3.0.0
* Werkzeug 3.0.1

**Frontend:**

* HTML5
* CSS3 con diseño responsivo
* JavaScript (Vanilla)

**Documentación:**

* Sphinx
* Read the Docs Theme

Características del Sistema Braille Implementado
-------------------------------------------------

El conversor actual soporta:

* Alfabeto completo (a-z)
* Números (0-9)
* Espacios
* Signos de puntuación básicos: ``.``, ``,``, ``;``, ``:``, ``!``, ``?``, ``-``, ``(``, ``)``

El sistema utiliza caracteres Unicode de Braille Patterns (U+2800 a U+28FF) para 
representar los símbolos Braille visualmente en navegadores web.
