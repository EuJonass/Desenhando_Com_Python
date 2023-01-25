import turtle as t

# Setando a velocidade e a cor de fundo do programa
t.speed(999)
t.bgcolor('black')

# Loop com cores e medidas do quadrado
for i in range (20):
    for colours in ('red', 'magenta', 'blue', 'cyan', 'green', 'yellow'):
        t.color(colours)
        t.pensize(1.25)
        t.left(3)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)
        t.forward(200)
        t.left(90)

# Fecha a janela do projeto com um click
t.exitonclick()
