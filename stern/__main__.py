import loguru
from fabric import Application
from fabric.utils.helpers import get_relative_path
from stern.bar.statusbar import StatusBar


def main():
    bar = StatusBar()
    app = Application("bar", bar)
    # app.set_stylesheet_from_file(get_relative_path("bar/style.css"))
    app.run()


if __name__ == "__main__":
    main()
