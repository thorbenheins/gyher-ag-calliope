x = 0
y = 0
run = False

def push_led():
    global x, y
    if (run):
        led.plot(x, y)
        basic.pause(100)
        led.unplot(x, y)

        if (x < 5):
            x = x + 1

        if (x == 5):
            x = 0
            y = y + 1

        if (y == 5):
            y = 0


def run_led():
    global run
    run = True

def pause_led():
    global run
    run = False

input.on_button_event(Button.A, input.button_event_click(), run_led)
input.on_button_event(Button.B, input.button_event_click(), pause_led)

basic.forever(push_led)
