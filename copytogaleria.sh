#!/bin/bash

CONTENEDOR="infomesas"
DESTINO="/media/data/infomesas2/fotos/galeria"

# Verificar que se pasó un argumento
if [ -z "$1" ]; then
  echo "❌ Error: debés indicar la ruta de la foto."
  echo "   Uso: $0 <ruta_de_la_foto>"
  exit 1
fi

FOTO="$1"

# Verificar que el archivo existe
if [ ! -f "$FOTO" ]; then
  echo "❌ Error: el archivo '$FOTO' no existe."
  exit 1
fi

# Copiar la foto
cp "$FOTO" "${DESTINO}/$(basename "$FOTO")"

if [ $? -eq 0 ]; then
  echo "✅ Foto copiada exitosamente en: ${DESTINO}/$(basename "$FOTO")"
else
  echo "❌ Falló la copia. Verificá que el path destino exista dentro del contenedor."
fi
