#!/bin/bash

# Ruta del archivo a eliminar
archivo_a_eliminar="/storage/.kodi/warp.sh"

# Verificar y eliminar el contenedor wgcfconf si existe
if docker ps -a --format '{{.Names}}' | grep -q '^wgcfconf$'; then
    docker rm -f wgcfconf
    echo "Detenido y eliminado contenedor 'wgcfconf'"
fi

# Verificar y eliminar el contenedor wgcf si existe
if docker ps -a --format '{{.Names}}' | grep -q '^wgcf$'; then
    docker rm -f wgcf
    echo "Detenido y eliminado contenedor 'wgcf'"
fi

# Verificar y eliminar el contenedor ace_proxy si existe
if docker ps -a --format '{{.Names}}' | grep -q '^ace_proxy$'; then
    docker rm -f ace_proxy
    echo "Detenido y eliminado contenedor 'ace_proxy'"
fi

# Verificar y eliminar el archivo si existe
if [ -e "$archivo_a_eliminar" ]; then
    rm -f "$archivo_a_eliminar"
    echo "Eliminado archivo en '$archivo_a_eliminar'"
fi

# Reiniciar el sistema
reboot