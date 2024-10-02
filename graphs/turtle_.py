# from turtle import *
from turtle import color, begin_fill, forward, left, pos, end_fill, done

color('purple', 'cyan')
begin_fill()
while True:
    forward(200)
    # left(177)
    # left(111) # more fine
    # left(250) # fine
    # left(220) # 18
    # left(200) # 9
    left(144) # - 5 кутів зірка
    if abs(pos()) < 1:
        break
end_fill()
done()
