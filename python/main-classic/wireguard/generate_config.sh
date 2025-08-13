#!/bin/bash

# Comprobación de argumentos
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <archivo_de_entrada> <archivo_de_salida>"
    exit 1
fi

archivo_entrada="$1"
archivo_salida="$2"

# Verifica que el archivo exista
if [ ! -f "$archivo_entrada" ]; then
    echo "Error: El archivo de entrada no existe: $archivo_entrada"
    exit 1
fi

# Extrae valores con awk, tolerando espacios
private_key="$(grep -E '^\s*PrivateKey\s*=' "$archivo_entrada" | head -n1 | cut -d '=' -f2- | sed 's/^[[:space:]]*//')"
address="$(grep -E '^\s*Address\s*=' "$archivo_entrada" | head -n1 | cut -d '=' -f2- | cut -d ',' -f1 | sed 's/^[[:space:]]*//')"
public_key="$(grep -E '^\s*PublicKey\s*=' "$archivo_entrada" | head -n1 | cut -d '=' -f2- | sed 's/^[[:space:]]*//')"

# Verifica si se extrajeron correctamente
if [[ -z "$private_key" || -z "$address" || -z "$public_key" ]]; then
    echo "Error: No se pudieron extraer los valores:"
    echo "PrivateKey: $private_key"
    echo "Address: $address"
    echo "PublicKey: $public_key"
    exit 1
fi

# Generar el nuevo archivo
cat <<EOF > "$archivo_salida"
[Interface]
PrivateKey = $private_key
Address = $address
[Peer]
PublicKey = $public_key
AllowedIPs = 0.0.0.0/1
AllowedIPs = ::/1
Endpoint = engage.cloudflareclient.com:2408
EOF

echo "✅ Archivo generado correctamente: $archivo_salida"
