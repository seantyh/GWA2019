import os
import sys
sys.path.append("./")
# pylint:disable=no-name-in-module
from PySide2.QtWidgets import QApplication
from GWA2019.anmorph import AnmorphWindow

if __name__ == "__main__":
    if len(sys.argv) >= 2:        
        app = QApplication(sys.argv)
        data_path = sys.argv[1]
        if not os.path.exists(data_path):
            print("Cannot find ", data_path)
            exit()
        anmorph = AnmorphWindow(sys.argv[1])
        anmorph.show()
        sys.exit(app.exec_())
    else:
        print(sys.argv)
        exit()
    