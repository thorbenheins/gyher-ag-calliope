let x = 0
let y = 0
basic.forever(function () {
    led.plot(x, y)
    basic.pause(100)
    led.unplot(x, y)
    if (x < 4) {
        x = x + 1
    } else if (x == 4) {
        x = 0
        y = y + 1
    }
    if (y == 5) {
        y = 0
    }
})
