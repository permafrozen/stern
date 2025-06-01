import fabric
from fabric import Application
from fabric.widgets.label import Label
from fabric.widgets.window import Window

window = Window(
    child=Label("Hello World"),
    all_visible=True
)

app = Application("stern", window )
app.run()
