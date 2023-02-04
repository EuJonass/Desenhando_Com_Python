from turtle import *

# Setando cor presente no desenho e a velocidade de execução
color('red', 'yellow')
begin_fill()
speed(10)

# loop do desenho
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

# Fechando a janela com um click
exitonclick()
