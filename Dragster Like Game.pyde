# Identifying the Game states as fixed variables
game_state = "title"
player_x = 50 #position of player in X (it is fixed)
speed = 0
countdown = 3
travel_time = 0
false_start = False #the game will not start without pressing the start click (space)
particles = []

def setup():
    size(800, 400) #screen size
    textAlign(CENTER) #text allignment
    textSize(32) #text size

def draw(): #conditions for the game
    global game_state, player_x, speed, countdown, travel_time, false_start, particles #bringing in variables

    background(0) #black background
    
#first state of the game (start)
    if game_state == "title": 
        text("Press SPACE to Start", width / 2, height / 2) #text and its position at the center 
        if game_state == "title" and key == ' ': #pressing space to start count down
           game_state = "countdown"  #pressing space to start count down
        
#second state of the game is to count down
    elif game_state == "countdown": 
        text(str(int(countdown)), width / 2, height / 2) #text position and the text shown
        countdown -= 1 / frameRate #count down is calculated based on the screen frame
        if countdown <= 0: #if the count down reaches zero then start the next state
            game_state = "playing" #to start playing the game) (the states build on one another as we will see next)
 
#third state of the game is to play 
    elif game_state == "playing":
        rect(player_x, height / 2, 50, 20) #the player looks like a rectangle
        if keyPressed and key == ' ': #if we press space 
            if countdown > 0:
                false_start = True #game not started yet untill the count down is zero
                game_state = "result" #go to next state
            else:
                speed += 0.1 #game started and this is the speed of the rectangle
                player_x += speed #increasing the position in X to move to the right
                particles.append([player_x, height / 2 + 10, 255]) #particles that come out of the rectangle

        for p in particles[:]: #drawing particles
            fill(255, p[2]) #colour of the particle building on one another
            circle(p[0], p[1], 5) #particle shape
            p[1] -= 2 #particle 1 position X
            p[2] -= 5 #particle 2 position X (so it becomes a gradient)
            if p[2] <= 0: #in case of no move, no particles appear, remove particles
                particles.remove(p)
                
#fourth state of the game is the end of the game 
        if player_x > width:
            travel_time = (millis() - countdown * 1000) / 1000.0 #calculate the time used by the playet (rectangle) to travel
            game_state = "result"
    
    elif game_state == "result":
        text(travel_time, width / 2, height / 2 - 50) 
        text("Press R to Restart", width / 2, height / 2 + 50)
        if game_state == "result" and key == 'r': #restart
           game_state = "title"
           player_x = 50
           speed = 0
           countdown = 3
           false_start = False
           particles = []
