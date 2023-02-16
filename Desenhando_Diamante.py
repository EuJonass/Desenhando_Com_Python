import turtle as t

# Setando cor da caneta e cor de fundo
t.color('yellow')
t.bgcolor('black')

# Desenhando o triângulo maior
t.left(60)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(150)

# Desenhando as linhas de divisória do triângulo maior
t.forward(174)
t.backward(174)
t.left(16.5)
t.forward(180)
t.backward(180)
t.right(31.5)
t.forward(180)
t.right(75)

# Desenhando os quatro triâgulos superiores
# Desenhando o primeiro triângulo superior
t.forward(53)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)

# Desenhando o segundo triângulo superior
t.right(120)
t.forward(50)
t.left(120)
t.forward(50)

# Desenhando o terceiro triângulo superior				
t.right(120)
t.forward(50)
t.left(120)
t.forward(50)

# Desenhando o quarto triângulo superior 
t.right(120)
t.forward(50)
t.left(120)
t.forward(50)
t.left(180)
t.forward(50)

# Desenhando a linha superior do diamante
t.left(300)
t.forward(160)

# Fechando a janela de apresentação com um click
t.exitonclick()
