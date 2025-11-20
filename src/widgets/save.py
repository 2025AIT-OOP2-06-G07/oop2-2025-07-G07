from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget,QLabel

from mod.save import save_with_timestamp
from mod.paths import DIR_OUT


class SaveWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__define_layout()

    def __define_layout(self) -> None:
        layout = QVBoxLayout()

        button1 = QPushButton("ボタン 1")
        button2 = QPushButton("ボタン 2")
        button3 = QPushButton("保存")

        button1.clicked.connect(self.__on_click_button)
        button2.clicked.connect(self.__on_click_button)
        button3.clicked.connect(self.__on_click_button3)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setLayout(layout)

    def __on_click_button(self) -> None:
        print("ボタンがクリックされました")

    def __on_click_button3(self) -> None:
        save_with_timestamp('transcribed_text', DIR_OUT)
        #print("保存されました")

