import turtle as t

# Requerindo o nome ao Usuário
name = str(input('Digite seu primeiro nome:'))


# Setando a cor de Background
t.bgcolor('yellow')

# Apontando para baixo e removendo a caneta
t.right(90)
t.penup()

# Selecionado
fonte1 = ("Comic Sans", 35, "italic")
t.write("Bem Vindo !", False, "center", fonte1)
t.forward(40)

fonte2 = ("Comic Sans", 30, "bold")
t.write(name, False, "center", fonte2)
t.forward(45)

fonte3 = ("Comic Sans", 31, "normal")
t.write("Como vai ?", False, "center", fonte3)


# Fecha a janela do projeto com um click
t.exitonclick()
