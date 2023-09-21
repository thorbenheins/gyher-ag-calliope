let x = 0
let y = 0
let run = false
input.onButtonEvent(Button.A, input.buttonEventClick(), function run_led() {
    
    run = true
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function pause_led() {
    
    run = false
})
basic.forever(function push_led() {
    
    if (run) {
        led.plot(x, y)
        basic.pause(100)
        led.unplot(x, y)
        if (x < 5) {
            x = x + 1
        }
        
        if (x == 5) {
            x = 0
            y = y + 1
        }
        
        if (y == 5) {
            y = 0
        }
        
    }
    
})
