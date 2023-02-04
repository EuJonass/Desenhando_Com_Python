import turtle as t
 
# Setando posição da rosa e deixando ela alinhada
t.penup()
t.left (90)
t.fd(150)
t.pendown()
t.right (90)

# Setando a cor do Background
t.bgcolor('light gray')
 
# Desenhando a rosa 
t.fillcolor ("red")
t.begin_fill()
t.circle (10,180)
t.circle (25,110)
t.left (50)
t.circle (60,45)
t.circle (20,170)
t.right (24)
t.fd (30)
t.left (10)
t.circle (30,110)
t.fd (20)
t.left (40)
t.circle (90,70)
t.circle (30,150)
t.right (30)
t.fd (15)
t.circle (80,90)
t.left (15)
t.fd (45)
t.right (165)
t.fd (20)
t.left (155)
t.circle (150,80)
t.left (50)
t.circle (150,90)
t.end_fill()
 

# Desenhando as pétalas de separação
t.left (150)
t.circle (-90,70)
t.left (20)
t.circle (75,105)
t.setheading (60)
t.circle (80,98)
t.circle (-90,40)


# Alinhando a posição para ser desenhado o caule
t.left (180)
t.circle (90,40)
t.circle (-80,98)
t.setheading (-83)


# Desenhando a primeira folha e a parte reta do caule
t.fd (30)
t.left (90)
t.fd (25)
t.left (45)
t.fillcolor ("green")
t.begin_fill()
t.circle (-80,90)
t.right (90)
t.circle (-80,90)
t.end_fill()
t.right (135)
t.fd (60)
t.left (180)
t.fd (85)
t.left (90)
t.fd (80)

# Desenhando a segunda folha e a parte final do caule
t.right (90)
t.right (45)
t.fillcolor ("green")
t.begin_fill()
t.circle (80,90)
t.left (90)
t.circle (80,90)
t.end_fill()
t.left (135)
t.fd (60)
t.left (180)
t.fd (60)
t.right (90)
t.circle (200,60)

# Fechando a janela do desenho com um click
t.exitonclick()
