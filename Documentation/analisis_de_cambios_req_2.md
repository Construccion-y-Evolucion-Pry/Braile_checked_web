<div align="center">
  <h2>Escuela Politécnica Nacional</h2>
  <h3>Facultad de Ingeniería de Sistemas</h3>
  <h4>Construcción y Evolución de Software</h4>
  
  <hr width="60%">
  
  <br>
  
  <table align="center">
    <tr>
      <td><b>Versión:</b></td>
      <td>1.0</td>
    </tr>
    <tr>
      <td><b>Grupo:</b></td>
      <td>5</td>
    </tr>
    <tr>
      <td><b>Fecha:</b></td>
      <td>Enero 2026</td>
    </tr>
  </table>
</div>

<div style="page-break-after: always;"></div>

---

# Análisis Comparativo y Evaluación de la Funcionalidad de Exportación Invertida para Braille Táctil en *BraiLator*

## Implementación del Requerimiento de Generación de Documentos con Braille Invertido para Perforación

## Resumen

Este informe analiza la incorporación de una funcionalidad de exportación de Braille invertido en la rama develop del proyecto *Braille_web*. La característica permite generar documentos en formato .docx con texto Braille espejado horizontalmente y con el orden de caracteres invertido, facilitando la perforación manual desde el reverso del papel. La evaluación se realiza mediante comparación con la rama master, revisión del código fuente y análisis del impacto en accesibilidad física, destacando la integración de la librería python-docx y el enfoque centrado en la persona usuaria final.

## 1. Introducción

La lectura táctil de Braille perforado requiere que los puntos sean generados desde el reverso del soporte físico, lo que implica invertir tanto la orientación de cada celda Braille como el orden de lectura. La mayoría de las herramientas digitales de Braille no contemplan este requerimiento físico, limitando su utilidad fuera del entorno digital.

La funcionalidad implementada en la rama develop responde a esta necesidad, permitiendo a docentes, familiares y personas cuidadoras generar material Braille listo para perforación, ampliando el alcance práctico del sistema más allá de la pantalla.

## 2. Metodología de Análisis

El análisis se realizó mediante:

- Inspección de commits y comparación funcional entre ramas.
- Revisión del código responsable de la transformación e inversión Braille.
- Pruebas manuales de generación y descarga de documentos.
- Evaluación conceptual del proceso de perforación Braille.

## 3. Análisis de Cambios

En la rama master no existe soporte para exportación ni manipulación física de Braille. En contraste, la rama develop introduce:

- La función espejo_braille en app.py.
- Una nueva ruta /descargar-braille-word para generación de documentos.
- La dependencia externa python-docx>=1.1.0.
- Elementos de interfaz que permiten disparar la descarga desde la aplicación web.

## 4. Descripción de la Transformación Braille

La función espejo_braille implementa una transformación compuesta definida por:

1. Inversión horizontal de cada patrón Unicode Braille.
2. Reversión del orden completo de la secuencia de caracteres.

Esta transformación asegura que, tras la perforación desde el reverso del papel, el texto sea legible táctilmente en el anverso, respetando la orientación estándar del Braille.

## 5. Generación de Documentos

La exportación se realiza mediante la librería python-docx, generando archivos .docx completamente en memoria, sin persistencia en el servidor. El documento incluye el Braille invertido, el texto original como referencia y una instrucción explícita de uso ("Perfore desde el reverso"), lo que mejora la usabilidad y reduce errores en el proceso físico.

## 6. Aprendizajes y Limitaciones

La implementación demuestra cómo transformaciones geométricas aplicadas a codificaciones simbólicas pueden mejorar la accesibilidad física. Refuerza la importancia del diseño centrado en el usuario y la validación de requisitos que trascienden el entorno digital.

Entre las limitaciones identificadas se encuentran la ausencia de validación específica para distintos dispositivos de impresión y la dependencia de la correcta interpretación de Unicode Braille por el sistema operativo.

## 7. Conclusión

La funcionalidad de exportación de Braille invertido constituye una extensión de alto valor práctico, integrando consideraciones físicas y de accesibilidad en un sistema web. Esta mejora posiciona a *Braile_checked_web* como una herramienta más completa e inclusiva, alineada con principios de accesibilidad universal y evolución incremental del software.

## 8. Referencias

1. Repositorio principal del proyecto *Braile_checked_web*.  
   Disponible en: https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web

2. Documentación técnica generada con Sphinx - guía de uso y API.  
   https://github.com/Construccion-y-Evolucion-Pry/Braile_checked_web/tree/develop/Documentation

3. **Unicode Consortium.**  
   *Unicode Standard, Version 15.1 - Braille Patterns (U+2800-U+28FF).*  
   The Unicode Consortium, 2023.  
   Disponible en: https://www.unicode.org/charts/PDF/U2800.pdf

4. **World Wide Web Consortium (W3C).**  
   *Web Content Accessibility Guidelines (WCAG) 2.2.*  
   W3C Recommendation, 2023.  
   Disponible en: https://www.w3.org/TR/WCAG22/