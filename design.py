from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Password Manager")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        self.initUI()

    def initUI(self):
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_label = QtWidgets.QLabel("Welcome to Password Manager")
        self.title_label.setFont(QtGui.QFont("Arial", 24))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.add_account_button = QtWidgets.QPushButton("Add Account")
        self.add_account_button.setFont(QtGui.QFont("Arial", 14))
        self.layout.addWidget(self.add_account_button)

        self.view_accounts_button = QtWidgets.QPushButton("View Accounts")
        self.view_accounts_button.setFont(QtGui.QFont("Arial", 14))
        self.layout.addWidget(self.view_accounts_button)

        self.exit_button = QtWidgets.QPushButton("Exit")
        self.exit_button.setFont(QtGui.QFont("Arial", 14))
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

    def show_status(self, message):
        self.status_bar.showMessage(message)

def run_app():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())