import turtle as t

# Setando cor do Background
t.bgcolor('black')

# Setanco cor da Caneta
t.color('red')

#  inicia o Bloco de desenho
t.begin_fill()

# Largura da caneta
t.pensize(3)

# Desenho do coração
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(138)
t.end_fill()

# Fecha o console do projeto com um click
t.exitonclick()
