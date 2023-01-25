import turtle as t

# Setando a cor de Background
t.bgcolor('black')

# set the colormode to 255
t.colormode(255)

# Loop de cor azul
for i in range(15):
    t.color('blue')
    t.forward(2+2*i)
    t.right(90)
  
# Modo de cor setado em 1.0
t.colormode(1.0)
  
# Loop de cor Vermelha
for i in range(15):
    t.color('red')
    t.forward(40+4*i)
    t.right(90)
    
# último loop, de cor amarela
for i in range(12):
    t.color('yellow')
    t.forward(110+4*i)
    t.right(90)

# Fecha a janela do programa com um Clicl
t.exitonclick()
