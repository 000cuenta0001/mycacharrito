#!/bin/bash
DOCKER="/storage/.kodi/addons/service.system.docker/bin/docker"

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
if $DOCKER ps -a --format '{{.Names}}' | grep -q '^wgcfconf$'; then
    $DOCKER stop wgcfconf
    $DOCKER rm wgcfconf
    echo "6. Detenido y eliminado contenedor 'wgcfconf'"
fi

# Ejecutar el primer contenedor en segundo plano
container_id=$($DOCKER run -d --name wgcfconf --sysctl net.ipv6.conf.all.disable_ipv6=0 --privileged --cap-add net_admin -v /lib/modules:/lib/modules -v $(pwd)/wgcf:/wgcf neilpang/wgcf-docker:alpine -4)

# Esperar a que el contenedor termine (puede ajustar el tiempo según sus necesidades)
$DOCKER wait "$container_id"

# Al salir del contenedor, eliminar el contenedor
$DOCKER rm "$container_id"
echo "7. Ejecutado contenedor 'wgcfconf' y esperado a su término"

# Verificar y eliminar el contenedor wgcf si existe
if $DOCKER ps -a --format '{{.Names}}' | grep -q '^wgcf$'; then
    $DOCKER stop wgcf
    $DOCKER rm wgcf
    echo "8. Detenido y eliminado contenedor 'wgcf'"
fi

# Verificar y eliminar el contenedor ace_proxy si existe
if $DOCKER ps -a --format '{{.Names}}' | grep -q '^ace_proxy$'; then
    $DOCKER stop ace_proxy
    $DOCKER rm ace_proxy
    echo "9. Detenido y eliminado contenedor 'ace_proxy'"
fi

# Levantar contenedor final con configuración wgcf
$DOCKER run -d --name wgcf --privileged --cap-add net_admin --sysctl net.ipv6.conf.all.disable_ipv6=0 -v /lib/modules:/lib/modules -v $(pwd)/wgcf:/wgcf -p 8000:8000 -p 8621:8621 -p 6878:6878 --restart unless-stopped neilpang/wgcf-docker sh -c "sed -i -e '/^Address =/n; /^Address =/d' -e 's/AllowedIPs = 0.0.0.0\\/0/AllowedIPs = 0.0.0.0\\/1/' -e 's/AllowedIPs = ::\\/0/AllowedIPs = ::\\/1/' -e '/^DNS =/d' -e '/^MTU =/d' /wgcf/wgcf-profile.conf && cp /wgcf/wgcf-profile.conf /etc/wireguard/wgcf.conf && wg-quick up wgcf && tail -f /dev/null"
echo "10. Levantado contenedor final 'wgcf'"

# Levantar contenedor aceproxy
$DOCKER run -d --name ace_proxy --network container:wgcf --privileged --restart unless-stopped ef1f/raspberry_ace_proxy:latest
echo "11. Levantado contenedor 'ace_proxy'"
