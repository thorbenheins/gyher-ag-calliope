let block_x = randint(0, 4)
let block_y = 0
let next_block_x = block_x
let next_block_y = block_y
loops.everyInterval(100, function onEvery_interval() {
    
    led.unplot(block_x, block_y)
    led.plot(next_block_x, next_block_y)
    block_x = next_block_x
    block_y = next_block_y
})
input.onButtonEvent(Button.A, input.buttonEventClick(), function on_button_event_a() {
    
    if (block_x == 0) {
        next_block_x = 4
    } else {
        next_block_x = block_x - 1
    }
    
})
