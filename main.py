from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
import tkinter as tk

def restart_game():
    restart_window.destroy()
    screen.clear()
    main()

def ask_restart():
    global restart_window
    restart_window = tk.Tk()
    restart_window.title("Game Over")
    restart_window.geometry("200x100")

    screen_width = restart_window.winfo_screenwidth()
    screen_height = restart_window.winfo_screenheight()
    window_width = 200
    window_height = 100

    position_top = int((screen_height / 2) - (window_height / 2))
    position_left = int((screen_width / 2) - (window_width / 2))

    restart_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    label = tk.Label(restart_window, text="Game Over!", font=("Arial", 12))
    label.pack(pady=10)

    restart_button = tk.Button(restart_window, text="RESTART", command=restart_game)
    restart_button.pack()

    restart_window.mainloop()

def main():
    global screen, snake, food, scoreboard, game_is_on
    screen=Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("SNAKE GAME")
    screen.tracer(0)

    snake=Snake()
    food=Food()
    scoreboard=Scoreboard()

    screen.listen()
    screen.onkey(snake.up,"w")
    screen.onkey(snake.down,"s")
    screen.onkey(snake.left,"a")
    screen.onkey(snake.right,"d")

    game_is_on=True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()


        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()


        #Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
            game_is_on=False
            scoreboard.game_over()
            ask_restart()


        #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) <10:
                game_is_on=False
                scoreboard.game_over()
                ask_restart()



    screen.exitonclick()
main()
