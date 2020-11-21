from main_window import *
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_main_window = QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(my_main_window)
    my_main_window.show()
    sys.exit(app.exec_())