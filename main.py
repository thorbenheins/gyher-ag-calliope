block_x = randint(0, 4)
block_y = 0
next_block_x = block_x
next_block_y = block_y


def onEvery_interval():
    global block_x, block_y, next_block_x, next_block_y
    led.unplot(block_x, block_y)
    led.plot(next_block_x, next_block_y)
    block_x = next_block_x
    block_y = next_block_y

loops.every_interval(100, onEvery_interval)

def on_button_event_a():
    global block_x, next_block_x;
    if (block_x == 0): 
        next_block_x = 4
    else:
        next_block_x = block_x - 1
input.on_button_event(Button.A, input.button_event_click(), on_button_event_a)