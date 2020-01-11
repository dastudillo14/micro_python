Instalación de MicroPython para ESP8266 ESP32
-Preferible en una distribución de GNU/LINUX
-Microcontrolador ESP8266 o ESP32
-Python instalado

1.)Descargar micropython acuerdo a Microcontrolador--
http://micropython.org/download

2.)Instalar ESPTOOL en Python

sudo pip install esptool

3.)Conectar Microcontrolador mediante USB y saber en que puerto está conectado
desde el terminal podemos escribir /dev/ttyUSB y presionar tab para ver alternativas.

4.)Abrimos terminal donde este descargado el archivo .bin del paso 1.

5.)Una vez instaldo el ESPTOOL, escribimos en el terminal para flashear el firmware por defecto del MicroControlador

esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

6.)Una vez terminado el proceso instalamos el firmware descargado, se detalla la ruta y nombre del archivo descargado y el nombre del chip(opcional).

	esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20190125-v1.10.bin







