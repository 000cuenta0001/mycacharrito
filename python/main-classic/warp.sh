#!/bin/bash

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
if docker ps -a --format '{{.Names}}' | grep -q '^wgcfconf$'; then
    docker stop wgcfconf
    docker rm wgcfconf
    echo "6. Detenido y eliminado contenedor 'wgcfconf'"
fi

# Ejecutar el primer contenedor en segundo plano
container_id=$(docker run -d --name wgcfconf --sysctl net.ipv6.conf.all.disable_ipv6=0 --privileged --cap-add net_admin -v /lib/modules:/lib/modules -v $(pwd)/wgcf:/wgcf neilpang/wgcf-docker:alpine -4)

# Esperar a que el contenedor termine (puede ajustar el tiempo según sus necesidades)
docker wait "$container_id"

# Al salir del contenedor, eliminar el contenedor
docker rm "$container_id"
echo "7. Ejecutado contenedor 'wgcfconf' y esperado a su término"

# Verificar y eliminar el contenedor wgcf si existe
if docker ps -a --format '{{.Names}}' | grep -q '^wgcf$'; then
    docker stop wgcf
    docker rm wgcf
    echo "8. Detenido y eliminado contenedor 'wgcf'"
fi

# Verificar y eliminar el contenedor ace_proxy si existe
if docker ps -a --format '{{.Names}}' | grep -q '^ace_proxy$'; then
    docker stop ace_proxy
    docker rm ace_proxy
    echo "9. Detenido y eliminado contenedor 'ace_proxy'"
fi

# Levantar contenedor final con configuración wgcf
docker run -d --name wgcf --privileged --cap-add net_admin --sysctl net.ipv6.conf.all.disable_ipv6=0 -v /lib/modules:/lib/modules -v $(pwd)/wgcf:/wgcf -p 8000:8000 -p 8621:8621 -p 6878:6878 neilpang/wgcf-docker sh -c "sed -i -e '/^Address =/n; /^Address =/d' -e 's/AllowedIPs = 0.0.0.0\\/0/AllowedIPs = 0.0.0.0\\/1/' -e 's/AllowedIPs = ::\\/0/AllowedIPs = ::\\/1/' -e '/^DNS =/d' -e '/^MTU =/d' /wgcf/wgcf-profile.conf && cp /wgcf/wgcf-profile.conf /etc/wireguard/wgcf.conf && wg-quick up wgcf && tail -f /dev/null"
echo "10. Levantado contenedor final 'wgcf'"

# Levantar contenedor aceproxy
docker run -d --name ace_proxy --network container:wgcf --privileged --restart unless-stopped ef1f/raspberry_ace_proxy:latest
echo "11. Levantado contenedor 'ace_proxy'"
