import turtle as t

# Setando algumas configurações gerais
t.bgcolor('black')
t.speed(9.5)
t.penup()
t.color('black')


# Definindo a curvatura dos desenhos
def caixa_curvada(t, lados):
    for x in range(lados):
        t.circle(90, extent=90)
        t.forward(120)

    t.circle(90, extent=90)


# Definindo o desenho das cobras
def cobra(t, cor):
    
    # Separando as cobras
    t.backward(16)
    t.left(90)
    t.forward(16)
    t.right(90)
    
    # Preenchendo as cobras com as cores definidas
    t.fillcolor(cor)

    # Desenhando as cobras
    t.begin_fill()
    t.forward(64)
    caixa_curvada(t, 2)
    t.forward(44)
    t.left(90)
    t.forward(152)
    t.right(90)
    t.forward(16)
    t.right(90)
    t.forward(204)
    caixa_curvada(t, 1)
    t.forward(44)
    t.left(90)
    t.forward(60)
    t.circle(-90, extent=90)
    t.forward(64)
    t.end_fill()
    
    # Desenhando os olhos das cobras
    t.backward(86)
    t.left(90)
    t.forward(224)
    t.dot(48, 'white')
    t.backward(224)
    t.right(90)
    t.forward(86)
    

# Chamando as funçoes e definindo as cores
cobra(t, '#3774A8')

# Invertendo os desenhos em 180 graus
t.left(180)

cobra(t, '#F6D646')

# Fecha a janela de apresentação com um Click
t.exitonclick()
