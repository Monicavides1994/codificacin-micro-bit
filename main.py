def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P0, 90)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(4000)
    pins.servo_write_pin(AnalogPin.P0, 180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P1, 90)
    music.play(music.builtin_playable_sound_effect(soundExpression.twinkle),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(4000)
    pins.servo_write_pin(AnalogPin.P1, 180)
input.on_button_pressed(Button.B, on_button_pressed_b)

pins.servo_write_pin(AnalogPin.P0, 180)
pins.servo_write_pin(AnalogPin.P0, 180)