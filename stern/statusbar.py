import psutil

# import fabric
from fabric.widgets.button import Button
from fabric.widgets.label import Label
from fabric.widgets.datetime import DateTime
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.widgets.centerbox import CenterBox
from fabric.hyprland.widgets import WorkspaceButton, Workspaces


class StatusBar(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top", anchor="left top bottom", exclusivity="auto", **kwargs
        )

        self.battery = Button(child=Label(str(int(psutil.sensors_battery().percent))))

        self.workspaces = Workspaces(
            orientation="v",
            buttons_factory=lambda ws_id: WorkspaceButton(ws_id, label=str(ws_id)),
        )

        self.date_time = DateTime(
            formatters=("%H\n%M\n%S"),
        )

        self.children = CenterBox(
            orientation="v",
            start_children=self.workspaces,
            center_children=self.battery,
            end_children=self.date_time,
        )
