from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    s = SlideShow()
    s.setFilenames(['a.png', 'b.png', 'c.png'])
    s.show()
    app.exec_()