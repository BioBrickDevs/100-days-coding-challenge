import turtle
import paddle
import keyboard
import pynput

LEFT_PADDLE_CORD = (-350, 0)
RIGHT_PADDLE_CORD = (350, 0)
import time


def on_press(key):  # `key` can be `Key` (which doesn't have `char`) or `KeyCode` (which have `char`)
    global listen

    print(str(key) == "'1'", str(key))
    if str(key) == "'w'":
        l_paddle.up()
        print("jeesus")
    # if key == Key.esc:
    if str(key) == 'Key.esc':
        listen = not listen

    if listen:
        # if hasattr(key, 'char') and key.char == '1': # there is no `Key.1` and `1`
        if str(key) == "'w'":
            l_paddle.up()

            label_var.set(label_var.get() + '1')
            print('1!')


listen = False

listener = pynput.keyboard.Listener(on_press=on_press)

# listener.start()
# listener.wait()
screen = turtle.Screen()
screen.setup(width=800, height=600, starty=200)
screen.bgcolor("black")
screen.tracer(0)



r_paddle = paddle.Paddle(center)
l_paddle = paddle.Paddle(LEFT_PADDLE_CORD)
def testi(self):
    print("toimii")

screen.getcanvas().bind('<Up>', l_paddle.up)
# screen.onkeypress(l_paddle.up, "wk")
# screen.onkeypress(l_paddle.down, 's')
# screen.onkeypress(r_paddle.up, "Up")
# screen.onkeypress(r_paddle.down, "Down")
# l_paddle.screen.listen()
# r_paddle.screen.listen()


# Collect events until released
if __name__ == '__main__':
    while True:
        time.sleep(0.1)
        screen.update()

screen.exitonclick()

listener.stop()

# Collect events until released
