from turtle import *

def main():
    hangman_turtle = Turtle()
    hangman_turtle.pensize(10)
    hangman_turtle.left(90)
    hangman_turtle.forward(200)

    writer_turtle = Turtle()
    writer_turtle.hideturtle()
    writer_turtle.pencolor("red")

    input_turtle = Turtle()
    screen = input_turtle.getscreen()
    letter = screen.textinput("Enter a letter", "Letter:")

    writer_turtle.penup()
    writer_turtle.goto(-200, -200)
    writer_turtle.pendown()
    writer_turtle.write(f"_ _ {letter.upper()} _ _ T",  font=("Arial", 38, "normal"))


    done()


if __name__ == '__main__':
    main()
