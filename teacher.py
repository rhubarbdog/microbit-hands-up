from microbit import *
import radio
import time

radio.on()
begin = time.ticks_ms()
end = time.ticks_ms()
received = []
count = 0 

while not button_a.is_pressed() and not button_b.is_pressed():
    display.scroll(str(count), wait = False, loop = True)

    if count > 999:
        digits = 4
    elif count > 99:
        digits = 3
    elif count > 9:
        digits = 2
    else:
        digits = 1
        
    while time.ticks_diff(end, begin) < (digits * 1600) - 150:
        message = radio.receive()

        if message is None:
            sleep(10)
        else:
            received.append(message)
            count += 1

        if button_a.is_pressed() or button_b.is_pressed():
            break
        
        end = time.ticks_ms()

    begin = end
    end = time.ticks_ms()
    
display.show('?')
while button_a.is_pressed() or button_b.is_pressed():
    sleep(50)

while received != []:

    if button_a.is_pressed() or button_b.is_pressed():
        display.show('-')
        radio.send(received[0])
        received = received[1:]

        while button_a.is_pressed() or button_b.is_pressed():
            sleep(50)

display.clear()
