from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class ButtonWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__define_layout()

    def __define_layout(self) -> None:
        layout = QVBoxLayout()

        button1 = QPushButton("ボタン 1")
        button2 = QPushButton("文字起こし")
        button3 = QPushButton("ボタン 3")

        button1.clicked.connect(self.__on_click_button)
        button2.clicked.connect(self.__on_click_button)
        button3.clicked.connect(self.__on_click_button)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        self.setLayout(layout)

    def __on_click_button(self) -> None:
        print("ボタンがクリックされました")
