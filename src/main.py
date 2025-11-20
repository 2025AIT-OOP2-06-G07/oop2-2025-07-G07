import sys

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from widgets.save import SaveWidget


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__define_layout()

    def __define_layout(self) -> None:
        self.setWindowTitle("title")

        layout = QVBoxLayout()
        self.button_widget = SaveWidget()
        layout.addWidget(self.button_widget)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()

    win.show()
    app.exec()

    del win
    sys.exit()
