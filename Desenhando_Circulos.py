import turtle as t
from random import randint

# Seleciona a cor de fundo, a velocidade, a largura da linha e o modo de cor
t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
t.colormode(255)

# Loop onde será escolhida a cor do novo circulo e sua nova posição
for i in range(100):
    color = (randint(0, 255),
            randint(0, 255),
            randint(0, 255))
    t.pencolor(color)
    t.circle(i*2)
    t.left(90)

# A janela onde o desenho apareceu é fechado com um click
t.exitonclick()
