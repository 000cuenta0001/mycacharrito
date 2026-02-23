#!/bin/bash
DOCKER="/storage/.kodi/addons/service.system.docker/bin/docker"

# Eliminar contenedores específicos si existen
docker rm -f ace_proxy
docker rm -f wgcf

# Limpiar imágenes dangling (sin tag)
echo "Eliminando imágenes <none>..."
docker image prune -a -f

echo "Limpieza completada."

# Instalar acestream sin warp
docker run -d  --name acestream  --restart always -p 8621:8621  -p 6878:6878  roheji8181/aceserve:arm32