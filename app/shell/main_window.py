from PyQt6.QtWidgets import QMainWindow, QTabWidget
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super()._init__()
        self.setWindowTitle("Notes")

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.menu = self.menuBar().addMenu("Features")
        self.actions = {}

    def add_feature(self, name: str, factory):
        act = QAction(name, self)
        act.triggered.connect(lambda: self.open_tab(name, factory()))
        self.menu.addAction(act)
        self.actions[name] = act

    def open_tab(self, title, widget):
        idx = self.tabs.addTab(widget, title)
        self.tabs.setCurrentIndex(idx)
