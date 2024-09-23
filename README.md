# Dragster Like Game
 
Dragster-like Game
This repository contains a Dragster-like Game developed as part of the Game Development 1 course at the University of California, Santa Cruz. This game simulates a simplified version of the classic Dragster (Atari 2600) game, excluding the gear-shifting mechanic. The player accelerates by holding a key, with a countdown timer before the race begins, and particles added for extra visual effects.

Acknowledgments
This project was developed as an assignment for the Game Development 1 course (GAME 235) at the University of California, Santa Cruz. The code was developed with the help of Mohamed Samy. Additionally, we used ChatGPT to assist in structuring and refining parts of the project.

Overview
The Dragster-like Game includes a countdown timer, acceleration mechanics, and a result screen. Players start the game by pressing a key, accelerate by holding a key, and finish by crossing the screen or false-starting before the countdown finishes. The game also includes particle effects for extra visual appeal.

Some of the Game Features
•	A title screen is displayed where a specific key starts the countdown timer.
•	A countdown timer is implemented, with a false start triggered by pressing the accelerator during the countdown.
•	A specific key moves the player forward.
•	The player accelerates the longer the key is held down.
•	A results screen appears after either crossing the finish line or triggering a false start.
•	The total travel time from the end of the countdown to crossing the finish line is displayed.
•	A specific key allows the game to restart from the results screen.
•	Particle effects are added for visual enhancement. (

Installation
1.	Download and install Processing.
2.	Enable Python Mode:
o	Open Processing.
o	Go to the Mode drop-down menu at the top right.
o	Select Python mode from the list.
3.	Clone or download this repository to your local machine.
4.	Open the dragster_game.pde file in Processing.

Usage
Controls
•	Press SPACE: Starts the countdown timer and accelerates the player after the countdown.
•	Press R: Restarts the game from the results screen.
Running the Program
1.	Launch Processing.
2.	Open the dragster_game.pde file from this repository.
3.	Click the Run button in Processing to start the game.
4.	On the title screen, press SPACE to start the countdown.
5.	Once the countdown reaches zero, hold SPACE to accelerate the player (a moving rectangle).
6.	Cross the finish line or experience a false start if you press SPACE too early.
7.	After the race, the results screen will show your travel time.
8.	Press R to restart the game.

Game Features
•	Title Screen: Displayed before the countdown, press SPACE to start the countdown.
•	Countdown Timer: A timer during which pressing SPACE will result in a false start.
•	Acceleration: The player accelerates the longer they hold down the SPACE key.
•	Particle Effects: Particles are generated from the player's car as they accelerate.
•	Results Screen: Displays the player's travel time, with an option to restart the game by pressing R.

Example Code Snippet
```python
Copy code
# Identifying the Game states as fixed variables
game_state = "title"
player_x = 50  # Player starting position
speed = 0
countdown = 3
travel_time = 0
false_start = False
particles = []

def setup():
    size(800, 400)  # Screen size
    textAlign(CENTER)
    textSize(32)

def draw():
    global game_state, player_x, speed, countdown, travel_time, false_start, particles

    background(0)  # Black background

    # Title screen state
    if game_state == "title":
        text("Press SPACE to Start", width / 2, height / 2)
        if game_state == "title" and key == ' ':
            game_state = "countdown"

    # Countdown state
    elif game_state == "countdown":
        text(str(int(countdown)), width / 2, height / 2)
        countdown -= 1 / frameRate
        if countdown <= 0:
            game_state = "playing"

    # Playing state
    elif game_state == "playing":
        rect(player_x, height / 2, 50, 20)  # Draw player as a rectangle
        if keyPressed and key == ' ':
            if countdown > 0:
                false_start = True
                game_state = "result"
            else:
                speed += 0.1  # Player accelerates
                player_x += speed
                particles.append([player_x, height / 2 + 10, 255])  # Particle effect

        # Draw particles
        for p in particles[:]:
            fill(255, p[2])
            circle(p[0], p[1], 5)
            p[1] -= 2
            p[2] -= 5
            if p[2] <= 0:
                particles.remove(p)

        # End game when player crosses the finish line
        if player_x > width:
            travel_time = (millis() - countdown * 1000) / 1000.0
            game_state = "result"

    # Results screen state
    elif game_state == "result":
        text(travel_time, width / 2, height / 2 - 50)
        text("Press R to Restart", width / 2, height / 2 + 50)
        if game_state == "result" and key == 'r':
            game_state = "title"
            player_x = 50
            speed = 0
            countdown = 3
            false_start = False
            particles = []

