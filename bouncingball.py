import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class BouncyBallWindow(QWidget):
    
    def __init__(self):
        super(BouncyBallWindow, self).__init__()
        self.init_UI()
        
        # Ball properties
        self.diameter = 30
        self.x = 0 # x-coordinate
        self.y = 0 # y-coordinate
    
    def init_UI(self):
        # Set window dimensions to 600px by 400px
        self.resize(600, 400)
        
        # Set window background color
        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
                     
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw(painter)
    
    def draw(self, painter):
        painter.setPen(Qt.red)
        painter.setBrush(Qt.red)
        painter.drawEllipse(self.x, self.y, self.diameter, self.diameter)
        painter.end()


def main():
    app = QApplication(sys.argv)
    bbw = BouncyBallWindow()
    bbw.show()
    
    app.exec_()


if __name__ == '__main__':
    main()
