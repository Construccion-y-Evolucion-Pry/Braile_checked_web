#!/bin/bash
# Script para generar la documentación con Sphinx

echo "🔨 Generando documentación con Sphinx..."

# Ruta al Python del entorno virtual
PYTHON_PATH="C:/Users/alexi/OneDrive/Documents/VII Semestre/Construccion y Evolucion del Software/Proyecto/.venv/Scripts/python.exe"

# Cambiar al directorio del proyecto
cd "$(dirname "$0")"

# Limpiar la build anterior (opcional)
if [ -d "Documentation/build" ]; then
    echo "🧹 Limpiando documentación anterior..."
    rm -rf Documentation/build/*
fi

# Generar la documentación
echo "📚 Compilando documentación HTML..."
"$PYTHON_PATH" -m sphinx -b html Documentation/source Documentation/build/html

if [ $? -eq 0 ]; then
    echo "✅ ¡Documentación generada exitosamente!"
    echo "📂 Ubicación: Documentation/build/html/index.html"
    echo ""
    echo "Para ver la documentación, abre:"
    echo "   file:///$(pwd | sed 's|/c/|C:/|')/Documentation/build/html/index.html"
else
    echo "❌ Error al generar la documentación"
    exit 1
fi
