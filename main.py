from fabric import Application
from fabric.utils.helpers import get_relative_path
from stern.statusbar import StatusBar

if __name__ == "__main__":
    bar = StatusBar()
    app = Application("bar", bar)
    app.set_stylesheet_from_file(get_relative_path("stern/style.css"))
    app.run()
