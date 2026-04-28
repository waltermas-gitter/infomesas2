#!/bin/bash

# ─────────────────────────────────────────────
# Copia una foto al contenedor Docker "infomesas"
# Uso: ./copiar_foto.sh <ruta_de_la_foto>
# ─────────────────────────────────────────────

CONTENEDOR="infomesas"
DESTINO="/home/waltermas/infomesas2/fotos/galeria"

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

# Verificar que el contenedor está corriendo
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTENEDOR}$"; then
  echo "❌ Error: el contenedor '$CONTENEDOR' no está corriendo."
    docker start infomesas
fi

# Copiar la foto
echo "📂 Copiando '$(basename "$FOTO")' al contenedor '$CONTENEDOR'..."
docker cp "$FOTO" "${CONTENEDOR}:${DESTINO}/$(basename "$FOTO")"

if [ $? -eq 0 ]; then
  echo "✅ Foto copiada exitosamente en: ${DESTINO}/$(basename "$FOTO")"
else
  echo "❌ Falló la copia. Verificá que el path destino exista dentro del contenedor."
fi
