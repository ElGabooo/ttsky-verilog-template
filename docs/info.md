<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

Es un circuito de prueba combinacional para Tiny Tapeout. Los primeros cuatro bits de entrada se invierten mediante un NOT y las salidas están conectadas a un display. 

## How to test

1. Conectar las entradas dedicadas a un arreglo de interruptores (DIP switch).
2. Conectar las salidas dedicadas a un display de 7 segmentos de catodo comun.
3. Al modificar los primeros 4 interruptores, los segmentos correspondientes responderan de forma invertida.
4. Al encender los interruptores del 4 al 7, los segmentos restantes se iluminaran de forma directa.

## External hardware

Display de 7 segmentos 
