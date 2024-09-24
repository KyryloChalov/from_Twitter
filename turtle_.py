from turtle import *
# from turtle import color, begin_fill, forward, left, pos, end_fill, done

color('purple', 'cyan')
begin_fill()
while True:
    forward(200)
    left(144)
    if abs(pos()) < 1:
        break
end_fill()
done()
