from typing import Protocol

from PySide6.QtWidgets import QWidget


class Window(Protocol):
    def show(self) -> QWidget: ...
