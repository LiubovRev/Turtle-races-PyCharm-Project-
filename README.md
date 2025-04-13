Turtle Race Game
Overview

The Turtle Race Game is a fun and interactive Python game where you can bet on which turtle will win a race. The turtles race across the screen, and you have the opportunity to place a bet on one of them. The game determines the winner randomly, and you are notified if your bet was correct.
Features

    User Bet: The user can bet on the color of the turtle they think will win the race.

    Random Race Simulation: The turtles move forward randomly until one crosses the finish line.

    Race Outcome: The game notifies the user whether their bet was correct or not based on the winning turtle's color.

Requirements

    Python 3.x

    turtle module (This is included with Python by default.)

How to Run

    Make sure you have Python installed. If not, download and install it from the official Python website.

    Copy the provided Python code into a file named turtle_race_game.py.

    Run the game by executing the script in your terminal or command prompt:

python turtle_race_game.py

    The game will open a graphical window, and you will be prompted to bet on a turtle by typing its color (e.g., red, orange, yellow, green, blue, purple).

    Once you place your bet, the race will begin, and the turtles will race towards the finish line. The winner will be announced based on the outcome of the race.

Code Overview
Main Components:

    User Input: The game prompts the user to enter a bet for which turtle will win (one of the six colors).

    Turtle Setup: Each turtle is created, assigned a color, and placed at the starting line.

    Race Mechanism: Each turtle moves forward randomly at each step. The race continues until one turtle crosses the finish line.

    Winner Determination: Once a turtle crosses the finish line, the game checks if it matches the user's bet and announces the outcome.

Key Functions:

    screen.textinput(): Prompts the user to input their bet (the color of the turtle).

    random.randint(): Determines how far each turtle will move at each step of the race.

    turtle.forward(): Moves the turtles forward by a random distance.

    turtle.xcor(): Checks the turtle's horizontal position to determine if it has crossed the finish line.

Colors Used for Turtles:

    Red

    Orange

    Yellow

    Green

    Blue

    Purple

Game Flow:

    The user inputs their bet (the color of the turtle they think will win).

    The turtles are created and placed at the starting positions.

    The race begins, with each turtle moving a random distance.

    Once a turtle crosses the finish line, the game announces whether the user's bet was correct or not.
