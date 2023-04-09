import turtle as t

raio = 120
t.bgcolor("light blue")

# Definindo posição dos ângulos
t.setheading(-150)
t.penup()

# Criando a parte vermelha da logo
t.color("red")
t.begin_fill()
t.forward(raio)
t.pendown()
t.right(90)  # Setando o ângulo de 90 graus
t.circle(-raio, 120)
t.forward(raio * 3 ** .5)
t.left(120)
t.circle(2 * raio, 120)
t.left(60)
t.forward(raio * 3 ** .5)
t.end_fill()

# ------------- Parte Verde -------------
t.left(180)
t.color("green")
t.begin_fill()
t.forward(raio * 3 ** .5)
t.left(120)
t.circle(2 * raio, 120)
t.left(60)
t.forward(raio * 3 ** .5)
t.left(180)
t.circle(-raio, 120)
t.end_fill()

# ------------- Parte Amarela -------------
t.left(180)
t.circle(raio, 120)
t.color("yellow")
t.begin_fill()
t.circle(raio, 120)
t.right(180)
t.forward(raio * 3 ** .5)
t.right(60)
t.circle(-2 * raio, 120)
t.right(120)
t.forward(raio * 3 ** .5)
t.end_fill()

# ------------- Parte Azul -------------
t.penup()
t.left(98)
t.forward(raio / 20)
t.setheading(60)
t.color("blue")
t.pendown()
t.begin_fill()
t.circle(115, 350)
t.end_fill()
t.hideturtle()

# Fecha a tela de apresentação com um click
t.exitonclick()
