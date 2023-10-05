block_x = -1
block_y = -1 
# if those are -1 we will spawn a new block next intervall
next_block_x = -1
next_block_y = -1
#led.plot(0, 0)
tetris_highscore = 0

basic.show_leds("""
. . . . .
# # # # #
# # # # #
# # # # #
# # # # #
""")

def onEvery_rendering():
    global block_x, block_y, next_block_x, next_block_y, tetris_highscore
    
    if (next_block_x == -1 and next_block_y == -1): 
        next_block_x = randint(0, 4)
        next_block_y = 0
        if (led.point(next_block_x, next_block_y)):
            music.play_tone(Note.D, 2000)
            # count + highscore
            basic.show_number(tetris_highscore)
            control.wait_for_event(EventBusSource.MICROBIT_ID_BUTTON_AB, ButtonEvent.CLICK)
            basic.clear_screen()
            # stop the other things
        else:
            tetris_highscore = tetris_highscore + 1
    else:
        led.unplot(block_x, block_y)
        pass#music.play_tone(Note.C5, 10)
    led.plot(next_block_x, next_block_y)
    block_x = next_block_x
    block_y = next_block_y

loops.every_interval(100, onEvery_rendering)


##### Vertical Movement

def onEvery_moveDownOrSpawn():
    global block_x, block_y, next_block_x, next_block_y
    potential_block_y = next_block_y + 1
    # check we are not in one of these cases:
    # - out of the display (potential_block_y == 5)
    # - just before a new block should be spawned (next_block_y == -1)
    # - there is already a fixed block in the vertical direction we would move the block to (led.point(next_block_x, potential_block_y))
    if (not potential_block_y == 5 and not next_block_y == -1 and not led.point(next_block_x, potential_block_y)):
        next_block_y = potential_block_y
    else: 
        #next interval should spawn new block
        next_block_y = -1
        next_block_x = -1
        music.play_tone(Note.D5, 10)

loops.every_interval(1000, onEvery_moveDownOrSpawn)

##### Button Event Handlers

def on_button_event_a():
    global block_x, next_block_x;
    potential_block_x = -1
    if (block_x == 0): 
        potential_block_x = 4
    else:
        potential_block_x = block_x - 1
    
    if (not led.point(potential_block_x, block_y)):
        next_block_x = potential_block_x
    else: 
        music.play_tone(Note.A5, 10)

input.on_button_event(Button.A, input.button_event_click(), on_button_event_a)

def on_button_event_b():
    global block_x, next_block_x;
    potential_block_x = -1
    if (block_x == 4):
        potential_block_x = 0
    else:
        potential_block_x = block_x + 1
    
    if (not led.point(potential_block_x, block_y)):
        next_block_x = potential_block_x
    else:
        music.play_tone(Note.A5, 10)

input.on_button_event(Button.B, input.button_event_click(), on_button_event_b)
input.on_button_event(Button.AB, input.button_event_click(), on_button_event_b)