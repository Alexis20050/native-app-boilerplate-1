from PyQt6.QtWidgets import (
    QLabel,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QStackedWidget,
    QListWidgetItem,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notes with Sidebar")

        # Central container
        container = QWidget()
        layout = QHBoxLayout(container)
        self.setCentralWidget(container)

        # Sidebar (list of features)
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)
        layout.addWidget(self.sidebar)

        # Main area (stack of pages)
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Map feature names to widgets
        self.features = {}

        # Handle sidebar selection
        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)

    def add_feature(self, name: str, factory):
        # Create widget for feature
        widget = factory()
        self.features[name] = widget

        # Add to sidebar
        item = QListWidgetItem(name)
        self.sidebar.addItem(item)

        # Add to stacked widget
        self.stack.addWidget(widget)
