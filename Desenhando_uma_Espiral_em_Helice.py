import turtle as t

# Setando a resolução da tela de apresentação
# Setando a velocidade de apresentação do projeto
janela_de_carregamento = t.Screen()
janela_de_carregamento.setup(900, 700)
t.speed(7)

# Setando cor de fundo
t.bgcolor('black')

# Setando cor das linhas do desenho
t.pencolor('yellow')

# Loop onde é definido a posição dos circulos
for i in range(100):
    t.circle(5*i)
    t.circle(-5*i)
    t.left(i)

# Fecha a janela de apresentação com um click 
t.exitonclick()
