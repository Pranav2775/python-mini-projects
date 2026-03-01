import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Styled Stopwatch")
        self.setGeometry(600, 300, 450, 250)

        self.elapsed_time = 0  # milliseconds

        # Label
        self.label = QLabel("00:00:00:000")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Consolas", 35, QFont.Bold))
        self.label.setStyleSheet("""
            color: #00FF7F;
            background-color: #1E1E1E;
            border-radius: 10px;
            padding: 20px;
        """)

        # Buttons
        self.start_btn = QPushButton("Start")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")

        button_style = """
            QPushButton {
                background-color: #2D89EF;
                color: white;
                font-size: 16px;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1B5FA7;
            }
        """

        self.start_btn.setStyleSheet(button_style)
        self.stop_btn.setStyleSheet(button_style)
        self.reset_btn.setStyleSheet(button_style)

        # Layouts
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.stop_btn)
        hbox.addWidget(self.reset_btn)

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        # Window background
        self.setStyleSheet("background-color: #121212;")

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        # Button connections
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)

    def update_time(self):
        self.elapsed_time += 10  # update every 10 milliseconds

        hours = self.elapsed_time // 3600000
        minutes = (self.elapsed_time % 3600000) // 60000
        seconds = (self.elapsed_time % 60000) // 1000
        milliseconds = self.elapsed_time % 1000

        time_text = f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}"
        self.label.setText(time_text)

    def start(self):
        self.timer.start(10)  # 10 ms interval

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.label.setText("00:00:00:000")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Stopwatch()
    window.show()
    sys.exit(app.exec_())