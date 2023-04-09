import turtle as t

# Selecionamos a espessura da caneta
t.width(20)

# Setando a cor de background
t.bgcolor('black')

# Fazendo a parte vermelha da logo
t.up()
t.goto(0,0)
t.down()
t.color("red")
t.left(180)
t.circle(50, 270)
t.forward(120)
t.left(180)
t.circle(50, 90)

# Desenhando a parte azul 
t.up()
t.goto(-5, 13)
t.down()
t.color("light blue")
t.left(180)
t.circle(50, 270)
t.forward(120)
t.left(180)
t.circle(50, 90)

# Desenhando a parte branca do logo
t.up()
t.goto(-5, 5)
t.down()
t.color("white")
t.left(180)
t.circle(50, 270)
t.forward(120)
t.left(180)
t.circle(50, 90)

# Fecha a tela de apresentação com um click
t.exitonclick()
