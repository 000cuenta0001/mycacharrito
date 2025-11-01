#!/bin/bash

# Actualizar lista de paquetes
opkg update

# Actualizar todos los paquetes excepto los excluidos
for pkg in $(opkg list-upgradable | cut -f1 -d' '); do
    if [ "$pkg" != "zerotier" ] && [ "$pkg" != "libminiupnpc" ]; then
        echo "Actualizando $pkg ..."
        opkg upgrade "$pkg"
    else
        echo "Saltando $pkg ..."
    fi
done
