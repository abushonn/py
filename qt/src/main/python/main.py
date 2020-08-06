'''
Generated automatically by "fbs startproject"
'''
#!!! it's okey that PyCharm marks fbs_runtime with red.
from fbs_runtime.application_context.PyQt5 import ApplicationContext # it runs in venv - virtual environment
from PyQt5.QtWidgets import QMainWindow

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = QMainWindow()
    window.resize(250, 150)
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)