import sys
from PyQt5.QtWidgets import QApplication, QWidget

class BouncyBallWindow(QWidget):
    
    def __init__(self):
        super(BouncyBallWindow, self).__init__()
        self.init_UI()
    
    def init_UI(self):
        # Set window dimensions to 600px by 400px
        self.resize(600, 400)
        

def main():
    app = QApplication(sys.argv)
    bbw = BouncyBallWindow()
    bbw.show()
    
    app.exec_()


if __name__ == '__main__':
    main()
