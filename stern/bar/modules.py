import psutil

from fabric.hyprland.widgets import WorkspaceButton, Workspaces
from fabric.widgets.datetime import DateTime
from fabric.widgets.button import Button
from fabric.widgets.label import Label


class BatteryModule(Button):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs, child=Label(str(int(psutil.sensors_battery().percent)))
        )


class TimeModule(DateTime):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, formatters=("%H\n%M\n%S"))


class WorkspaceModule(Workspaces):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            orientation="v",
            buttons_factory=lambda ws_id: WorkspaceButton(ws_id, label=str(ws_id)),
        )
