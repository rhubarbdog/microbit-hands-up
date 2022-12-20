from microbit import *
import radio
import machine

radio.on()
display.show(Image.SQUARE)
while not button_a.is_pressed() and not button_b.is_pressed():
    sleep(50)

display.show('?')

id = machine.unique_id()

radio.send(str(id))

while True:
    message = radio.receive()
    if message is None:
        sleep(10)
    else:
        if message == str(id):
            display.show(Image.HAPPY)
            break

radio.off()
