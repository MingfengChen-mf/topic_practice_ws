import sys
from PyQt5.QtWidgets import QApplication, QLabel

def main():
    app=QApplication(sys.argv)
    label=QLabel()
    label.setText("Hello, PyQt5!")
    label.show()
    sys.exit(app.exec_())