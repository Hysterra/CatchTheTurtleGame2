import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 20, 'normal')
score = 0
game_over = False

# turtle list
turtle_list = []

# score turtle
score_turtle = turtle.Turtle()  # turtle oluştur

#countdown turtle
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    score_turtle.hideturtle()  # sakla
    score_turtle.penup()  # kalemi kaldır
    score_turtle.color("dark blue")  # renk
    # score_turtle.goto(x=0,y=300) #yukarı taşıyorsun

    top_height = screen.window_height()  # ölçmeden direkt ekran ne kadar büyükse otomatik kullanmak için
    y = top_height * 0.45
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score : 0", move=False, align="center", font=FONT)  # ekrana score yaz

grid_size = 10

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x,y):  #t.onclick(handle_click) ile birlikte bastığımız turtle'ın koordinatlarını almış olduk
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score : {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.color("green")
    t.shapesize(2, 2)
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


###### kare alan yerine dikdörtgen vs yapılabilsin diye ordinat ve apsis diye ayrıldı
y_cordinates = [-20, -10, 0, 10, 20]
x_cordinates = [-20, -10, 0, 10, 20]

def setup_turtles():
    for y in y_cordinates:
        for x in x_cordinates:
            make_turtle(x, y)

def hide_turtles():  # turtleları gizleme fonksiyonu
    for t in turtle_list:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()  # random kütüphanesinde, turtle listten birini rastgele seç özelliği ve göster
        screen.ontimer(show_turtles_randomly,500)



def countdown(time):
    global game_over
    countdown_turtle.hideturtle()  # sakla
    countdown_turtle.penup()  # kalemi kaldır
    #countdown_turtle.color("Black")  # renk
    # score_turtle.goto(x=0,y=300) #yukarı taşıyorsun

    top_height = screen.window_height()  # ölçmeden direkt ekran ne kadar büyükse otomatik kullanmak için
    y = top_height * 0.45
    countdown_turtle.setpos(0, y-30)
    countdown_turtle.clear()

    if time > 0:

        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time : {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1), 1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg=f"Game over!", move=False, align="center", font=FONT)

def start_game_up():

    turtle.tracer(0)  # takip etmeyi bırakıyoruz

    setup_score_turtle()
    setup_turtles()
    hide_turtles()  # gizledi
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)  # takip ediyoruz


start_game_up()
turtle.mainloop()
