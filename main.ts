namespace SpriteKind {
    export const nuvem = SpriteKind.create()
    export const inimigo = SpriteKind.create()
    export const vida_extra = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, Avião, 250, 0)
    music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    sprites.destroy(inimigo2, effects.fire, 100)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.vida_extra, function (sprite, otherSprite) {
    sprites.destroy(vidaextra, effects.trail, 100)
    info.changeLifeBy(1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(inimigo2, effects.fire, 100)
    info.changeScoreBy(1)
})
let Nuvem: Sprite = null
let vidaextra: Sprite = null
let inimigo2: Sprite = null
let projectile: Sprite = null
let Avião: Sprite = null
scene.setBackgroundColor(9)
Avião = sprites.create(img`
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
    `, SpriteKind.Player)
Avião.setStayInScreen(true)
controller.moveSprite(Avião)
info.setLife(3)
info.setScore(0)
game.onUpdateInterval(5000, function () {
    vidaextra = sprites.create(img`
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
        `, SpriteKind.vida_extra)
    vidaextra.setPosition(180, randint(10, 150))
    vidaextra.setVelocity(-100, 0)
})
game.onUpdateInterval(2000, function () {
    Nuvem = sprites.create(img`
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
        `, SpriteKind.nuvem)
    Nuvem.setPosition(180, randint(10, 120))
    Nuvem.setVelocity(-25, 0)
})
game.onUpdateInterval(2000, function () {
    inimigo2 = sprites.create(img`
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
        `, SpriteKind.Enemy)
    inimigo2.setPosition(180, randint(10, 150))
    inimigo2.setVelocity(-100, 0)
})
forever(function () {
	
})
game.onUpdateInterval(500, function () {
    Nuvem = sprites.create(img`
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
        `, SpriteKind.nuvem)
    Nuvem.setPosition(180, randint(10, 120))
    Nuvem.setVelocity(-100, 0)
})
