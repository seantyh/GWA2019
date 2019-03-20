import sys
sys.path.append("./")
# pylint:disable=no-name-in-module
from PySide2.QtWidgets import QApplication
from GWA2019.anmorph import AnmorphWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    anmorph = AnmorphWindow()
    anmorph.show()
    sys.exit(app.exec_())