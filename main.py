x = 0
y = 0

def on_forever():
    global x, y
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
   
basic.forever(on_forever)
