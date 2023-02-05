import turtle as t

# Listando as cores desejadas no desenho
cores = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

# Setando cor de Background
t.bgcolor('black')

# Loop de desenho
for c in range(360):
    t.pencolor(cores[c%6])
    t.width(c//100 + 1)
    t.forward(c)
    t.left(59)
    
