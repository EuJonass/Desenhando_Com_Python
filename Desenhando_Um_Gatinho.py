import turtle as t
import math as m

# Setando configurações gerais
t.bgcolor('yellow')
t.color('black')
t.speed(4.5)
t.pensize(6.5)


def moverCaneta(t, x, y):
  t.penup()
  t.setposition(x, y)
  t.pendown()

def moverCanetaY(t, y):
  t.penup()
  t.sety(y)
  t.pendown()

def posicaoCirculo(x, y, radius, angle):
  radians = m.radians(angle)
  return [x + (radius*m.sin(radians)),
            y + (radius*m.cos(radians))]


# Desenhando o contorno do rosto
moverCanetaY(t, -150)
t.circle(150)


# Desenhando o Nariz
moverCanetaY(t, -20 + (-15))
t.circle(20)


# Desenhando a Boca
moverCaneta(t, -100, -20 + (-15))
t.right(90)
t.circle(50, 180)
t.left(180)
t.circle(50, 180)


# Desenhando o olho Direito
moverCaneta(t, 30, 40)
t.right(180)
t.circle(30, -180)


# Desenhando o olho Esquerdo
moverCaneta(t, -30, 40)
t.circle(30, 180)


# Desenhando a Língua
moverCaneta(t, -20, -60 + (-15))
t.circle(20, 180)


# Desenhando a orelha Direita
posicaoA = posicaoCirculo(0, 0, 150, 25)
moverCaneta(t, posicaoA[0], posicaoA[1])

posicaoB = posicaoCirculo(0, 0, 150 + 85, 25 + 22)
t.setposition(posicaoB[0], posicaoB[1])

posicaoC = posicaoCirculo(0, 0, 150, 25 + 22 * 2)
t.setposition(posicaoC[0], posicaoC[1])


# Desenhando a orelha Esquerda
posicaoA = posicaoCirculo(0, 0, 150, -25)
moverCaneta(t, posicaoA[0], posicaoA[1])

posicaoB = posicaoCirculo(0, 0, 150 + 85, -25 + -22)
t.setposition(posicaoB[0], posicaoB[1])

posicaoC = posicaoCirculo(0, 0, 150, -25 + -22 * 2)
t.setposition(posicaoC[0], posicaoC[1])


# Desenhando os Bigodes
moverCaneta(t, 50, -15)
t.setheading(0)
t.forward(180)

moverCaneta(t, 50, 0)
t.left(5)
t.forward(180)

moverCaneta(t, -50, -15)
t.setheading(180)
t.forward(180)

moverCaneta(t, -50, 0)
t.left(-5)
t.forward(180)


# Fecha a janela de apresentação com um click
t.exitonclick()
