# import fabric
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.centerbox import CenterBox
from stern.bar.modules import WorkspaceModule
from stern.bar.modules import TimeModule
from stern.bar.modules import BatteryModule


class StatusBar(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top", anchor="left top bottom", exclusivity="auto", **kwargs
        )

        self.children = CenterBox(
            orientation="v",
            start_children=WorkspaceModule(),
            center_children=BatteryModule(),
            end_children=TimeModule(),
        )
