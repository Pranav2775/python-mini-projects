import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 300, 400, 150)

        # Create label
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        # Set font
        font = QFont("Arial", 40, QFont.Bold)
        self.label.setFont(font)

        # Set style
        self.label.setStyleSheet("""
            background-color: black;
            color: lime;
        """)

        # HBox Layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        self.setLayout(hbox)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString("hh:mm:ss AP")
        self.label.setText(time_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec_())