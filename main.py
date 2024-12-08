def on_a_pressed():
    bubble.toss_bubble()
    bubble.load_bubble()
    music.play(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    bubble.tilt_angle(bubble.Choice.RIGHT)
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_hit_wall(sprite, location):
    bubble.stick_to_wall(sprite, location)
scene.on_hit_wall(SpriteKind.bubble, on_hit_wall)

def on_left_repeated():
    bubble.tilt_angle(bubble.Choice.LEFT)
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

bubble.create_board()
bubble.load_bubble()
mySprite = sprites.create(io2_images.joy, SpriteKind.player)
mySprite.top = 102