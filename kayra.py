import pyglet

user_input = ""

# Create a window with a boundary of 200x200 pixels
window = pyglet.window.Window(width=200, height=200)

# Create a label to display the user's input
label = pyglet.text.Label(text=user_input, x=10, y=180, width=window.width-20, multiline=True, anchor_x='left', anchor_y='top')

num_lines = 1

@window.event
def on_text(text):
    global user_input
    user_input += text
    label.text = user_input
    if label.content_width > window.width:
        window.width += 10
    if label.content_height > window.height:
        window.height += label.content_height + 8
    label.x = 10
    label.y = window.height - 10

@window.event
def on_key_press(symbol, modifiers):
    global user_input
    if symbol == pyglet.window.key.ENTER:
        label.color = (255, 0, 0, 255)
    if symbol == pyglet.window.key.DOWN:
        user_input += "\n"
        label.text = user_input
        label.x = 10
        label.y = window.height - 10
        label.width = window.width-20
        return
    if symbol == pyglet.window.key.BACKSPACE:
        user_input = user_input[:-1]
        label.text = user_input
    if symbol == pyglet.window.key.ESCAPE:
        pyglet.app.exit()

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
