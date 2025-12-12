@namespace
class SpriteKind:
    nuvem = SpriteKind.create()
    inimigo = SpriteKind.create()
    vida_extra = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . 8 8 8 8 8 8 8 8 8 8 8 8
            . . . . 6 6 6 6 6 6 6 6 6 6 6 6
            . . 6 6 6 6 6 6 6 6 6 6 6 6 6 6
            9 9 9 1 9 1 9 9 9 1 9 1 9 9 1 9
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
            9 1 9 1 9 9 9 1 9 9 9 9 9 1 9 1
            . . 6 6 6 6 6 6 6 6 6 6 6 6 6 6
            . . . 6 6 6 6 6 6 6 6 6 6 6 6 6
            . . . 8 8 8 8 8 8 8 8 8 8 8 8 8
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        Avião,
        250,
        0)
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(inimigo2, effects.fire, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(vidaextra, effects.trail, 100)
    info.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.vida_extra, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(inimigo2, effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

Nuvem: Sprite = None
vidaextra: Sprite = None
inimigo2: Sprite = None
projectile: Sprite = None
Avião: Sprite = None
scene.set_background_color(9)
Avião = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . f f f . . . . . . . . . . .
        . f 2 1 f f f . . . . . . . . .
        . f 2 2 2 2 f f f . . . . . . .
        . f 2 2 2 1 9 9 f f f . . . . .
        . f 2 2 2 1 9 9 9 9 f f f . . .
        . f 2 1 1 1 9 9 9 9 9 9 f f f .
        . f 2 1 1 1 9 9 9 9 9 9 f f f .
        . f 2 2 2 1 1 1 1 1 f f f . . .
        . f 2 2 2 1 1 1 f f f . . . . .
        . f 2 2 2 2 f f f . . . . . . .
        . f 2 1 f f f . . . . . . . . .
        . . f f f . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        """),
    SpriteKind.player)
Avião.set_stay_in_screen(True)
controller.move_sprite(Avião)
info.set_life(3)
info.set_score(0)

def on_update_interval():
    global vidaextra
    vidaextra = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . f f f . . f f f . . . .
            . . . f 2 2 2 f f 2 2 2 f . . .
            . . f 2 1 1 2 2 2 2 2 2 2 f . .
            . f 2 1 1 1 2 2 2 2 2 2 2 2 f .
            . f 2 1 1 2 2 2 2 2 2 2 2 2 f .
            . f 2 2 2 2 2 2 2 2 2 2 2 2 f .
            . f 2 2 2 2 2 2 2 2 2 2 2 2 f .
            . f 2 2 2 2 2 2 2 2 2 2 2 2 f .
            . . f 2 2 2 2 2 2 2 2 2 1 f . .
            . . . f 2 2 2 2 2 2 2 1 f . . .
            . . . . f 2 2 2 2 2 1 f . . . .
            . . . . . f 2 2 2 2 f . . . . .
            . . . . . . f 2 2 f . . . . . .
            . . . . . . . f f . . . . . . .
            """),
        SpriteKind.vida_extra)
    vidaextra.set_position(180, randint(10, 150))
    vidaextra.set_velocity(-100, 0)
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    global Nuvem
    Nuvem = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . f f f . . . . .
            . . . . . f f f f 9 9 f f . . .
            . . . . f f 9 9 9 9 9 9 f f f .
            . . f f f 9 9 9 1 1 1 1 1 1 f .
            . . f 9 9 9 1 1 1 1 1 1 1 1 f f
            . f f 9 9 1 1 1 1 1 1 1 1 9 f f
            . . f 9 1 1 1 1 1 1 1 1 9 9 f .
            . . f f f 1 1 1 1 1 1 9 9 f f .
            . . . . f f f f f f f f f f . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.nuvem)
    Nuvem.set_position(180, randint(10, 120))
    Nuvem.set_velocity(-25, 0)
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    global inimigo2
    inimigo2 = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . f f f f f f f f f . f f
            . . . f f 1 1 f f f f f f d f f
            . . f f 1 1 1 f f f f f f d f f
            . f f 1 f 1 1 f f f f f f d f f
            . f f f f f f 1 f f f f f d f f
            . f f f f 1 1 2 f f f f f d f f
            . f f f 1 2 2 2 f f f f f d f f
            . f f 2 2 2 2 2 f f f f f d f f
            . f f 2 1 1 1 1 f f f f f d f f
            . . f f f f f f f f f f f d f f
            . . . f f f f f f f f f f d f f
            . . . . f f f f f f f f f . f f
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.enemy)
    inimigo2.set_position(180, randint(10, 150))
    inimigo2.set_velocity(-100, 0)
game.on_update_interval(2000, on_update_interval3)

def on_forever():
    pass
forever(on_forever)

def on_update_interval4():
    global Nuvem
    Nuvem = sprites.create(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . f f f . . . . .
            . . . . . f f f f 9 9 f f . . .
            . . . . f f 9 9 9 9 9 9 f f f .
            . . f f f 9 9 9 1 1 1 1 1 1 f .
            . . f 9 9 9 1 1 1 1 1 1 1 1 f f
            . f f 9 9 1 1 1 1 1 1 1 1 9 f f
            . . f 9 1 1 1 1 1 1 1 1 9 9 f .
            . . f f f 1 1 1 1 1 1 9 9 f f .
            . . . . f f f f f f f f f f . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            """),
        SpriteKind.nuvem)
    Nuvem.set_position(180, randint(10, 120))
    Nuvem.set_velocity(-100, 0)
game.on_update_interval(500, on_update_interval4)
