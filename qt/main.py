from PyQt5.QtWidgets import QApplication, QLabel

def hello_qt(a_message):
    app = QApplication([])
    label = QLabel(a_message)
    label.show()

    app.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hello_qt('Hello, Qt')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
