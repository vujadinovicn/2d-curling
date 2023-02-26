import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QSlider, QApplication, QWidget, QPushButton


class Slider(QWidget):
    """Widget for choosing velocity via slider."""
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.resize(350,150)
        self.button = QPushButton("START", self)  #button for getting and returning a value
        self.button.move(20,20)
        self.button.clicked.connect(self.on_click)  #action listener
        layout.addWidget(self.button)
        self.label = QLabel("7m/s")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        self.setWindowIcon(QIcon('data/logo.jpg'))

        self.slider = QSlider(Qt.Horizontal)  #making slider
        self.slider.setMinimum(5)
        self.slider.setMaximum(9)
        self.slider.setValue(7)  #initial value
        self.velocity = 7
        self.clicked = False
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(1)

        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.change_value)
        self.setLayout(layout)
        self.setWindowTitle("Set velocity")

    def change_value(self):
        vel = self.slider.value()
        self.label.setText(str(vel)+"m/s")

    def on_click(self):
        """
        Sets the attribute to chosen velocity and closes the window after.
        """
        self.velocity = self.slider.value()  #changes the value on click
        self.clicked = True
        self.close()  #closes right after it

def display():
    """
    Creates slider's widget
    :return: (int) wanted velocity
    """
    app = QApplication(sys.argv)
    f = Slider()
    f.show()
    app.exec_()
    return f.velocity
