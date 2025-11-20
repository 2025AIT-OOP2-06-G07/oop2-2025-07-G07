from pathlib import Path

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from mod.transcribe import transcribe_from_audio


class TranscribeWidget(QWidget):
    # 文字起こし完了時にテキストを通知するシグナル
    text_transcribed = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.audio_path: Path | None = None
        self.__setup_ui()

    def __setup_ui(self) -> None:
        layout = QVBoxLayout()

        # ヘッダー（ステップ2）
        header_layout = QHBoxLayout()
        self.label_step = QLabel("2.")
        self.label_step.setFixedWidth(20)

        self.btn_transcribe = QPushButton("文字起こし")
        self.btn_transcribe.setEnabled(False)  # ファイルが来るまで無効
        self.btn_transcribe.clicked.connect(self.__execute_transcribe)

        header_layout.addWidget(self.label_step)
        header_layout.addWidget(self.btn_transcribe)
        header_layout.addStretch()

        # 結果表示エリア
        self.text_display = QTextEdit()
        self.text_display.setPlaceholderText("ここに文字起こし結果が表示されます")
        self.text_display.setMinimumHeight(100)

        layout.addLayout(header_layout)
        layout.addWidget(self.text_display)
        self.setLayout(layout)

    @Slot(Path)
    def set_audio_path(self, path: Path) -> None:
        """録音完了シグナルを受け取るスロット"""
        self.audio_path = path
        self.btn_transcribe.setEnabled(True)
        self.btn_transcribe.setText(f"文字起こし ({path.name})")

    def __execute_transcribe(self) -> None:
        if not self.audio_path:
            return

        self.text_display.setPlaceholderText("解析中...")
        self.btn_transcribe.setEnabled(False)
        QApplication.processEvents()

        try:
            text = transcribe_from_audio(self.audio_path)
            self.text_display.setText(text)
            
            # 保存ウィジェットへ通知
            self.text_transcribed.emit(text)
        
        except Exception as e:
            self.text_display.setText(f"エラーが発生しました: {e}")
        finally:
            self.btn_transcribe.setEnabled(True)