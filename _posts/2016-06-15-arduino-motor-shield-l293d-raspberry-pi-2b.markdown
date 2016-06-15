---
layout: post
title:  "Arduino Motor Shield L293D com o Raspberry Pi 2 B"
date:   2016-06-15 17:47:20
categories: tutorial
highlight: true
image: img/post/motor_shield.gif
author: Fernando Ferreira Passe
---

O Motor Shield é um shield feito para o Arduino que permite que você controle 4 motores DC, utilizando uma fonte externa ou do próprio Arduino, abaixo veremos como funciona esse placa, os componentes que a compõem e como eles funcionam.

A placa é composta por 3 CI's, sendo 2 deles o L293D(ponte H dupla) e o outro um 74HC595(registrador de deslocamento), não é a intenção deste tutorial entrar em detalhes a cerca do funcionamento interno do chip. Vamos começar pelo L293D, este é responsavel por fazer o controle dos motores, controlando o sentido(hórario e anti-horário), além de alimentar o motor, abaixo vemos uma imagem que descreve o funcionamento.

![Fig. 1 - Ponte H dupla L293D](img/post/l293d_pinos.png)
<small>Fig. 1 - Ponte H dupla L293D, disponível em: [Link](http://www.noveldevices.co.uk/ar-project-motor-control)</small>

O L293D pode ser alimentado com uma tensão de +4,5-36V (no pino 8) e para alimentação da sua lógica interna é necessário uma tensão de 4,5-5V (no pino 16). 

## Configurando o giro do Motor

Para mudar o giro do motor mudamos para HIGH(1) ou LOW(0), os pinos 2(input 1) e 7(input 2), para o motor conectado nos terminais 3 e 6, além disso devemos coloca o pin 1 (enable 1,2) em HIGH para ativar o motor. Já para o motor conectado nos pinos 11 e 14, utilizamos os pinos 10(input 3) e 15(input 4) para controlar o giro e para ativar o pino 9 (enable 3,4). Veja a tabela abaixo a direção do giro do motor de acordo com a configuração efetuada:

| Enable 1,2 ou 3,4 | Input 1 ou 3 | Input 2 ou 4 | Saída                              |
|-------------------|--------------|--------------|------------------------------------|
| 1                 | 0            | 0            | Motor não gira                     |
| 1                 | 0            | 1            | Motor gira no sentido horário      |
| 1                 | 1            | 0            | Motor gira no sentido anti-horário |
| 1                 | 1            | 1            | Motor não gira                     |


## Registrador de deslocamento 74HC595


![Fig. 2 - Registrador de deslocamente 74HC595](img/post/74hc595.png)
<small>Fig. 2 - Registrador de deslocamente 74HC595, disponível em: [Link](http://www.protostack.com/blog/2010/05/introduction-to-74hc595-shift-register-controlling-16-leds/)</small>

Este componente é utilizado para economizar portas no Arduino, no nosso caso no Raspberry, pois precisamos conectar 8 portas, o que seria demasiadamente exagerado, com este CI utilizaremos apenas 3 :). Para realizar a conexão com o Raspberry, vamos conectar os pinos 14 (SER), 12 (RCLK) e 11 (SRCLK). O pinos Qn, são conectados nos inputs do L293D, você poderá oberservar ao final desta postagem o esquema completo do shield para entender melhor. Passando corretamente os valores, para o 74HC595, podemos controlar cada motor, veja na tabela abaixo as configurações que devem ser passados:

| Valor | Motor |               Direção              |
|-------|-------|------------------------------------|
|   4   |   M1  | Motor gira no sentido horário      |
|   8   |   M1  | Motor gira no sentido anti-horário |
|   2   |   M2  | Motor gira no sentido horário      |
|   16  |   M2  | Motor gira no sentido anti-horário |
|   1   |   M3  | Motor gira no sentido horário      |
|   64  |   M3  | Motor gira no sentido anti-horário |
|   32  |   M4  | Motor gira no sentido horário      |
|  128  |   M4  | Motor gira no sentido anti-horário |

![Fig. 3 - Esquema motor Shield](img/post/esquema_motor_shield.jpg)

Utilizando o esquema acima você pode conectar facilmente o Raspberry ao motor Shield.

Referência: [RoboCar: Arduino Motor Shield L293D with Raspberry Pi B+ (part 1)](http://blog.janlipovsky.cz/2016/03/robocar-arduino-motor-shield-with-raspberry-pi-part1.html).
