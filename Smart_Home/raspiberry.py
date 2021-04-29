import RPi.GPIO as GPIO


def light(signal):
    if signal not in [0, 1]:
        print('输入不合法')
        return '失败'
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, signal)
    # GPIO.cleanup()
    print('已将电平设为：%s' % signal)
    return '成功'
