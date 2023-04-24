from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainApp(QMainWindow):
    def _init_(self):
        super()._init_()

        self.setWindowTitle('Main App')
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton('Click me!', self)
        self.button.setGeometry(50, 50, 100, 30)
        self.button.clicked.connect(self.handle_button_click)

    def handle_button_click(self):
        print('Button clicked!')

if _name_ == '_main_':
    app = QApplication([])
    main_app = MainApp()
    main_app.show()
    app.exec_()
