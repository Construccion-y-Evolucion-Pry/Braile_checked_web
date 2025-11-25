# 📖 Conversor de Texto a Braille

Una aplicación web desarrollada con Flask que permite convertir texto normal a símbolos Braille Unicode.

## 🚀 Características

- ✅ Conversión en tiempo real de texto a Braille
- ✅ Soporte para letras (a-z), números (0-9) y símbolos de puntuación
- ✅ Caracteres especiales del español (ñ, vocales acentuadas, ü)
- ✅ Interfaz moderna y responsiva con tema oscuro
- ✅ **📋 Copiar al portapapeles**: Copia el texto en Braille con un solo clic
- ✅ **🖼️ Exportar como PNG**: Descarga una imagen profesional de la traducción
- ✅ Conversión instantánea mientras escribes
- ✅ Diseño accesible y fácil de usar
- ✅ API REST para integración con otras aplicaciones

## 📋 Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. **Clonar o descargar el repositorio**

2. **Crear un entorno virtual (recomendado)**
   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**
   - En Windows (Git Bash):
     ```bash
     source .venv/Scripts/activate
     ```
   - En Windows (CMD):
     ```cmd
     .venv\Scripts\activate.bat
     ```
   - En Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Uso

1. **Iniciar la aplicación**
   ```bash
   python app.py
   ```

2. **Abrir en el navegador**
   - Ir a: `http://localhost:5000`
   - O usar la IP mostrada en la terminal

3. **Usar el conversor**
   - Escribir el texto en el área de entrada
   - Hacer clic en "Convertir a Braille ⚡"
   - Ver el resultado en símbolos Braille
   - Opcionalmente, copiar el resultado con el botón "📋 Copiar Braille"

## 📁 Estructura del Proyecto

```
Proyecto/
│
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias del proyecto
│
├── templates/
│   └── index.html        # Plantilla HTML principal
│
├── static/
│   └── css/
│       └── style.css     # Estilos CSS
│
├── Documentation/         # Documentación Sphinx
│   ├── source/           # Archivos fuente (.rst)
│   ├── build/            # Documentación generada (HTML)
│   └── README.md         # Instrucciones de documentación
│
├── generar_docs.sh       # Script para generar docs (Bash)
├── generar_docs.bat      # Script para generar docs (Windows)
└── README.md             # Este archivo
```

## 📚 Documentación

Este proyecto incluye documentación completa generada con **Sphinx**.

### Ver la Documentación

La documentación HTML ya está generada. Abre en tu navegador:

```
start Documentation/build/html/index.html
```

### Regenerar la Documentación

Si modificas el código y quieres actualizar la documentación:

**En Windows (Git Bash):**
```bash
./generar_docs.sh
```

**En Windows (CMD):**
```cmd
generar_docs.bat
```

**Manualmente:**
```bash
python -m sphinx -b html Documentation/source Documentation/build/html
```

La documentación incluye:
- 📖 Introducción al sistema Braille
- 🔧 Instrucciones de instalación
- 🎯 Guía de uso (web y API)
- 📡 Referencia completa de la API REST
- 🔍 Documentación automática del código (extraída de los docstrings)

## 🎨 Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Estilos**: CSS personalizado con gradientes y animaciones

## 🔤 Caracteres Soportados

El conversor actualmente soporta:
- Letras del alfabeto (a-z)
- Números (0-9)
- Espacios
- Signos de puntuación básicos (. , ; : ! ? - ( ))

## 🌟 Características Futuras

- [ ] Soporte para más símbolos y caracteres especiales
- [ ] Conversión de Braille a texto normal
- [ ] Soporte para mayúsculas (indicador de mayúscula en Braille)
- [ ] Soporte para múltiples idiomas
- [ ] Exportar resultado como imagen o PDF
- [ ] API REST para integración con otras aplicaciones

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📝 Notas

- Los símbolos Braille se muestran usando caracteres Unicode de Braille Patterns (U+2800 a U+28FF)
- Para una mejor visualización, se recomienda usar navegadores modernos
- El sistema Braille aquí implementado es el Braille literario básico (Grado 1)

## 👨‍💻 Desarrollo

Este proyecto fue desarrollado como parte del curso de Construcción y Evolución del Software.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

Desarrollado con 💙 para mejorar la accesibilidad
