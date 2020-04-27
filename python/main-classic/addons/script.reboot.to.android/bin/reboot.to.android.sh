#!/bin/sh

# Proximo reinicio en NAND/MMC.
if /usr/sbin/fw_printenv whereToBootFrom > /dev/null 2>&1; then /usr/sbin/fw_setenv whereToBootFrom internal; fi
/usr/sbin/fw_setenv bootfromnand 1
sleep 1

# Reiniciar el sistema.
reboot
