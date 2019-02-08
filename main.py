import sys
from PyQt5.QtWidgets import QApplication
import window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window.window()

    sys.exit(app.exec_())
    