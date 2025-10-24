#!/bin/bash
DOCKER="/storage/.kodi/addons/service.system.docker/bin/docker"

# Eliminar contenedores específicos si existen
echo "Eliminando contenedores ace_proxy y wgcf..."
docker rm -f ace_proxy wgcf 2>/dev/null  echo "No se encontraron los contenedores."

# Eliminar imagen específica
echo "Eliminando imagen ef1f/raspberry_ace_proxy..."
docker rmi -f futebas/acestream-engine-arm:3.2.7.6 2>/dev/null  echo "La imagen futebas/acestream-engine-arm:3.2.7.6 no existe."

# Limpiar imágenes dangling (sin tag)
echo "Eliminando imágenes <none>..."
docker image prune -f

echo "Limpieza completada."
# Definir el directorio de trabajo
workdirectory="/storage/.kodi"

# Cambiar al directorio de trabajo
cd "$workdirectory" || exit

echo "1. Cambiado al directorio de trabajo: $workdirectory"

# Verificar si el directorio wireguard existe, si no existe, crearlo
if [ ! -d "wireguard" ]; then
    mkdir wireguard
    echo "2. Creado directorio 'wireguard'"
fi

# Cambiar al directorio 'wireguard'
cd wireguard
echo "3. Cambiado al directorio 'wireguard'"

# Verificar si el directorio wgcf existe
if [ -d "wgcf" ]; then
    # Si existe, eliminarlo
    rm -rf wgcf
    echo "4. Eliminado directorio 'wgcf'"
fi

# Crear el directorio wgcf
mkdir wgcf
echo "5. Creado directorio 'wgcf'"

# Verificar y eliminar el contenedor wgcfconf si existe
#if $DOCKER ps -a --format '{{.Names}}' | grep -q '^wgcfconf$'; then
#    $DOCKER stop wgcfconf
#    $DOCKER rm -v wgcfconf
#    echo "6. Detenido y eliminado contenedor 'wgcfconf'"
#fi

# Ejecutar el primer contenedor en segundo plano
#container_id=$($DOCKER run -d --name wgcfconf --sysctl net.ipv6.conf.all.disable_ipv6=0 --privileged --cap-add net_admin -v /lib/modules:/lib/modules -v $(pwd)/wgcf:/wgcf neilpang/wgcf-docker:alpine -4)

# Esperar a que el contenedor termine (puede ajustar el tiempo según sus necesidades)
#$DOCKER wait "$container_id"

# Al salir del contenedor, eliminar el contenedor
#$DOCKER rm "$container_id"
#echo "7. Ejecutado contenedor 'wgcfconf' y esperado a su término"

# _____PASOS NUEVOS_____

# Descargar el binario wgcf
curl -L -o wgcfBin https://github.com/ViRb3/wgcf/releases/download/v2.2.27/wgcf_2.2.27_linux_armv7

# Dar permisos de ejecución
chmod +x wgcfBin

# Ejecutar wgcf register
./wgcfBin register --accept-tos

# Ejecutar wgcf generate
./wgcfBin generate

# Crear carpeta ./wgcf si no existe
mkdir -p ./wgcf

# Mover ficheros wgcf-* al subdirectorio ./wgcf
mv ./wgcf-* ./wgcf/

# Renombrar el perfil generado
mv ./wgcf/wgcf-profile.conf ./wgcf/wgcf-profile-origen.conf

# Dar permisos al script y ejecutarlo
chmod +x ./generate_config.sh
./generate_config.sh ./wgcf/wgcf-profile-origen.conf ./wgcf/wgcf-profile.conf

# _____PASOS NUEVOS_____


# Verificar y eliminar el contenedor wgcf si existe
if $DOCKER ps -a --format '{{.Names}}' | grep -q '^wgcf$'; then
    $DOCKER stop wgcf
    $DOCKER rm -v wgcf
    echo "8. Detenido y eliminado contenedor 'wgcf'"
fi

# Verificar y eliminar el contenedor ace_proxy si existe
if $DOCKER ps -a --format '{{.Names}}' | grep -q '^ace_proxy$'; then
    $DOCKER stop ace_proxy
    $DOCKER rm -v ace_proxy
    echo "9. Detenido y eliminado contenedor 'ace_proxy'"
fi

# Levantar contenedor final con configuración wgcf
$DOCKER run -d --name wgcf --privileged --cap-add net_admin --sysctl net.ipv6.conf.all.disable_ipv6=0 -v /lib/modules:/lib/modules -v $(pwd)/wgcf:/wgcf -p 8000:8000 -p 8621:8621 -p 6878:6878 --restart unless-stopped neilpang/wgcf-docker sh -c "sed -i -e '/^Address =/n; /^Address =/d' -e 's/AllowedIPs = 0.0.0.0\\/0/AllowedIPs = 0.0.0.0\\/1/' -e 's/AllowedIPs = ::\\/0/AllowedIPs = ::\\/1/' -e '/^DNS =/d' -e '/^MTU =/d' /wgcf/wgcf-profile.conf && cp /wgcf/wgcf-profile.conf /etc/wireguard/wgcf.conf && wg-quick up wgcf && tail -f /dev/null"
echo "10. Levantado contenedor final 'wgcf'"

# Levantar contenedor aceproxy
$DOCKER run -d --name ace_proxy --network container:wgcf --privileged --restart unless-stopped jopsis/acestream:arm32
echo "11. Levantado contenedor 'ace_proxy'"
