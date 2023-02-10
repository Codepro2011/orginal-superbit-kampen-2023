bitbot.led_rainbow()
bitbot.led_rotate()
bitbot.rotatems(BBRobotDirection.LEFT, 60, 1500)
bitbot.goms(BBDirection.FORWARD, 60, 600)
bitbot.rotatems(BBRobotDirection.LEFT, 60, 1200)
bitbot.goms(BBDirection.FORWARD, 60, 1000)
bitbot.rotatems(BBRobotDirection.LEFT, 60, 250)
bitbot.goms(BBDirection.FORWARD, 60, 1000)
bitbot.rotatems(BBRobotDirection.LEFT, 60, 250)
bitbot.goms(BBDirection.FORWARD, 60, 1000)
bitbot.rotatems(BBRobotDirection.LEFT, 60, 250)
bitbot.goms(BBDirection.FORWARD, 60, 1000)
bitbot.rotatems(BBRobotDirection.LEFT, 60, 250)
bitbot.goms(BBDirection.FORWARD, 60, 1400)

def on_forever():
    pass
basic.forever(on_forever)
