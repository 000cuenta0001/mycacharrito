#!/bin/sh

if [ -f /storage/.kodi/addons/plugin.video.balandro/gdrando.txt ]
then
echo Existe archivo gdrando.txt
else 
echo No existe el archivo gdrando.txt y vamos a copiarlo a /storage/pruebas
cp -r /storage/.kodi/GDRANDO/.kodi /storage
echo Copiado OK
fi
