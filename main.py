numero = 0

def on_button_pressed_a():
    global numero
    numero = 0
    while numero <= 10:
        basic.show_number(numero)
        basic.pause(1000)
        numero += 1
    basic.show_string("FIM")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global numero
    numero = 10
    while numero >= 0:
        basic.show_number(numero)
        basic.pause(1000)
        numero += -1
    basic.show_string("FIM")
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
