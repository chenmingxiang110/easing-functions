import numpy as np

def EaseInSine(t):
    return 1-np.sin((1-t)*np.pi/2)

def EaseOutSine(t):
    return np.sin(t*np.pi/2)

def EaseInOutSine(t):
    return 0.5-0.5*np.sin((1-t*2)*np.pi/2)

def EaseInQuad(t):
    return t**2

def EaseOutQuad(t):
    return 1-EaseInQuad(1-t)

def EaseInOutQuad(t):
    return (t<0.5) * 0.5 * EaseInQuad(t * 2) + (t>=0.5) * 0.5 * (EaseOutQuad((t-0.5)*2) + 1)

def EaseInCubic(t):
    return t**3

def EaseOutCubic(t):
    return 1-EaseInCubic(1-t)

def EaseInOutCubic(t):
    return (t<0.5) * 0.5 * EaseInCubic(t * 2) + (t>=0.5) * 0.5 * (EaseOutCubic((t-0.5)*2) + 1)

def EaseInQuart(t):
    return t**4

def EaseOutQuart(t):
    return 1-EaseInQuart(1-t)

def EaseInOutQuart(t):
    return (t<0.5) * 0.5 * EaseInQuart(t * 2) + (t>=0.5) * 0.5 * (EaseOutQuart((t-0.5)*2) + 1)

def EaseInQuint(t):
    return t**5

def EaseOutQuint(t):
    return 1-EaseInQuint(1-t)

def EaseInOutQuint(t):
    return (t<0.5) * 0.5 * EaseInQuint(t * 2) + (t>=0.5) * 0.5 * (EaseOutQuint((t-0.5)*2) + 1)

def EaseInExpo(t):
    return (2**(t*10)-1)/1023

def EaseOutExpo(t):
    return 1-EaseInExpo(1-t)

def EaseInOutExpo(t):
    return (t<0.5) * 0.5 * EaseInExpo(t * 2) + (t>=0.5) * 0.5 * (EaseOutExpo((t-0.5)*2) + 1)

def EaseInCirc(t):
    return 1-np.sqrt(1-t**2)

def EaseOutCirc(t):
    return 1-EaseInCirc(1-t)

def EaseInOutCirc(t):
    return (t<0.5) * 0.5 * EaseInCirc((t<0.5) * t * 2) + (t>=0.5) * 0.5 * (EaseOutCirc((t>=0.5) * (t-0.5)*2) + 1)

def EaseInBack(t):
    return t**2 * (np.e*t-np.e+1)

def EaseOutBack(t):
    return 1-EaseInBack(1-t)

def EaseInOutBack(t):
    return (t<0.5) * 0.5 * EaseInBack(t * 2) + (t>=0.5) * 0.5 * (EaseOutBack((t-0.5)*2) + 1)

def EaseInElastic(t):
    return EaseInExpo(t) * np.sin(t * np.pi * 6.5) / np.sin(np.pi * 6.5)

def EaseOutElastic(t):
    return 1-EaseInElastic(1-t)

def EaseInOutElastic(t):
    v1 = (t<0.46503) * 0.5 * EaseInElastic(t * 2)
    v2 = (t>0.53497) * 0.5 * (EaseOutElastic((t-0.5)*2) + 1)
    # 确保一阶导数连续
    v3 = ((0.46503<=t) & (t<=0.53497)) * (13.047404544869156 * t - 6.023702272434578)
    return v1+v2+v3

def EaseInBounce(t):
    def _poly(_t):
        return 1-((_t-0.5)*2)**2
    v1 = (t<0.125) * _poly(t/0.125) * 0.015625
    v2 = ((0.125<=t) & (t<0.375)) * _poly((t-0.125)/0.25) * 0.0625
    v3 = ((0.375<=t) & (t<0.750)) * _poly((t-0.375)/0.375) * 0.25
    v4 = (0.750<=t) * _poly((t-0.75)/0.5) * 1
    return v1+v2+v3+v4

def EaseOutBounce(t):
    return 1-EaseInBounce(1-t)

def EaseInOutBounce(t):
    return (t<0.5) * 0.5 * EaseInBounce(t * 2) + (t>=0.5) * 0.5 * (EaseOutBounce((t-0.5)*2) + 1)