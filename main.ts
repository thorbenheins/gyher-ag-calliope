let block_x = -1
let block_y = -1
//  if those are -1 we will spawn a new block next intervall
let next_block_x = -1
let next_block_y = -1
// led.plot(0, 0)
// basic.show_leds("""
//  # # # #
//  # # # #
//  # # # #
//  # # # #
//  # # # #
// """)
loops.everyInterval(100, function onEvery_rendering() {
    
    if (next_block_x == -1 && next_block_y == -1) {
        next_block_x = randint(0, 4)
        next_block_y = 0
        if (led.point(next_block_x, next_block_y)) {
            music.playTone(Note.D, 2000)
            //  count + highscore
            basic.showString("hi!")
        }
        
    } else {
        //  stop the other things
        led.unplot(block_x, block_y)
        
    }
    
    // music.play_tone(Note.C5, 10)
    led.plot(next_block_x, next_block_y)
    block_x = next_block_x
    block_y = next_block_y
})
// #### Vertical Movement
loops.everyInterval(1000, function onEvery_moveDownOrSpawn() {
    
    let potential_block_y = next_block_y + 1
    //  check we are not in one of these cases:
    //  - out of the display (potential_block_y == 5)
    //  - just before a new block should be spawned (next_block_y == -1)
    //  - there is already a fixed block in the vertical direction we would move the block to (led.point(next_block_x, potential_block_y))
    if (!(potential_block_y == 5) && !(next_block_y == -1) && !led.point(next_block_x, potential_block_y)) {
        next_block_y = potential_block_y
    } else {
        // next interval should spawn new block
        next_block_y = -1
        next_block_x = -1
        music.playTone(Note.D5, 10)
    }
    
})
// #### Button Event Handlers
input.onButtonEvent(Button.A, input.buttonEventClick(), function on_button_event_a() {
    
    let potential_block_x = -1
    if (block_x == 0) {
        potential_block_x = 4
    } else {
        potential_block_x = block_x - 1
    }
    
    if (!led.point(potential_block_x, block_y)) {
        next_block_x = potential_block_x
    } else {
        music.playTone(Note.A5, 10)
    }
    
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function on_button_event_b() {
    
    let potential_block_x = -1
    if (block_x == 4) {
        potential_block_x = 0
    } else {
        potential_block_x = block_x + 1
    }
    
    if (!led.point(potential_block_x, block_y)) {
        next_block_x = potential_block_x
    } else {
        music.playTone(Note.A5, 10)
    }
    
})
