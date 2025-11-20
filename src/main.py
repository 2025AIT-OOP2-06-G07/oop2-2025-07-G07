import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from TranscribeWidget import TranscribeWidget
from mod.paths import DIR_OUT


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__define_layout()

    def __define_layout(self) -> None:
        self.setWindowTitle("title")
        self.resize(400, 300)

        layout = QVBoxLayout()
        
        self.transcribe_widget = TranscribeWidget()
        layout.addWidget(self.transcribe_widget)

        test_audio_path = DIR_OUT
        
        if test_audio_path.exists():
            self.transcribe_widget.set_audio_path(test_audio_path)
            print(f"デバッグ: {test_audio_path} をセットしました。")
        else:
            print(f"デバッグ: {test_audio_path} が見つかりません。録音ファイルが必要です。")

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()

    win.show()
    app.exec()
    sys.exit()