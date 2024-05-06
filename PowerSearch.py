from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QIcon
import webbrowser
import pyperclip
from PIL import Image
from PySide6.QtCore import QSize, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Power Search")
        self.setGeometry(100, 100, 600, 200)

        # Load night mode icon image
        self.night_mode_image = Image.open("Images\\night-mode.png")
        self.night_mode_image = self.night_mode_image.resize((20, 20))

        # Create dark mode button
        self.button_dark_mode = QPushButton(QIcon(self.night_mode_image.toqpixmap()), "")
        self.button_dark_mode.clicked.connect(self.switch_dark_mode)
        
        # Initialize night mode flag
        self.night_mode = True

        # Set default mode based on night_mode flag
        if self.night_mode:
            self.setStyleSheet("""
                QMainWindow::window-frame {background-color: #555555;}  /* Add this line to style the window header */
                QMainWindow {background-color: #333333; color: white;}
                QPushButton {color: #555555;}
                QPushButton:hover {background-color: #444444; color: white;}
                QPushButton:pressed {background-color: #555555;}
                QTableWidget {background-color: #333333; color: #444444; selection-background-color: #444444;}
                QTableCornerButton::section { background-color:#444444; }
                QHeaderView {background-color: #333333; color: #444444; selection-background-color: #444444;}
                QTableWidget::item {color: white; border: 1px solid #444444; background-color: #555555;}
                QTableWidget::item:selected {background-color: #444444;}
                QTableWidget::item:hover {background-color: #444444;}
                QLabel {color: white; background-color: #555555}
            """)

        self.initUI()
    def initUI(self):
        self.label = QLabel("Clipboard Text: ")

        self.button_profile = QPushButton("Debank")
        self.button_profile.clicked.connect(self.open_webpage)
        self.button_profile.setToolTip("Open address in DeBank")  # Add tooltip

        self.button_history = QPushButton("Open Debank History")
        self.button_history.clicked.connect(self.open_debank_history)
        self.button_history.setToolTip("Open tx history in DeBank")  # Add tooltip

        self.button_scanner = QPushButton("Open Scanner")
        self.button_scanner.clicked.connect(self.open_scanner)
        self.button_scanner.setToolTip("Open in zip scan.pulsechain")  # Add tooltip

        self.button_l1quidity = QPushButton("Open L1quidity")
        self.button_l1quidity.clicked.connect(self.open_l1quidity)
        self.button_l1quidity.setToolTip("Open in zip scan.pulsechain")  # Add tooltip

        self.button_pulsex = QPushButton("Open PulseX")
        self.button_pulsex.clicked.connect(self.pulsex)

        # Load refresh icon image
        image = Image.open("Images\\refresh.png")
        image = image.resize((20, 20))
        self.button_refresh = QPushButton(QIcon(image.toqpixmap()), "")
        self.button_refresh.clicked.connect(self.refresh)
        self.button_refresh.setToolTip("Refresh your clipboard")  # Add tooltip


        # Load night mode icon image
        night_mode_image = Image.open("Images\\night-mode.png")
        night_mode_image = night_mode_image.resize((20, 20))
        
        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.button_profile)
        buttons_layout.addWidget(self.button_history)
        buttons_layout.addWidget(self.button_scanner)
        buttons_layout.addWidget(self.button_l1quidity)
        buttons_layout.addWidget(self.button_pulsex)
        buttons_layout.addWidget(self.button_refresh)
        buttons_layout.addWidget(self.button_dark_mode)

        layout.addLayout(buttons_layout)

        # Create table widget for history
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(1)
        self.table_widget.setHorizontalHeaderLabels(["History"])

        layout.addWidget(self.table_widget)

        # Create frame and set layout
        frame = QFrame()
        frame.setLayout(layout)

        self.setCentralWidget(frame)

        # Update label every 100 milliseconds
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.timer.start(100)

        # Initialize clipboard history list
        self.clipboard_history = []

    def open_webpage(self):
        highlighted_text = pyperclip.paste()
        url = f"https://debank.com/profile/{highlighted_text}"
        webbrowser.open(url)

    def open_debank_history(self):
        highlighted_text = pyperclip.paste()
        url = f"https://debank.com/profile/{highlighted_text}/history"
        webbrowser.open(url)

    def open_scanner(self):
        highlighted_text = pyperclip.paste()
        url = f"http://127.0.0.1:3694/#/address/{highlighted_text}"
        webbrowser.open(url)

    def open_l1quidity(self):
        url = "https://l1quidity.vercel.app/"
        webbrowser.open(url)

    def pulsex(self):
        highlighted_text = pyperclip.paste()
        self.label.setText(f"PulseX: http://127.0.0.1:3691/#/?outputCurrency={highlighted_text}")

    def refresh(self):
        self.update_label()

    def switch_dark_mode(self):
        if self.night_mode:
            self.setStyleSheet("")
            self.button_dark_mode.setIcon(QIcon(self.night_mode_image.toqpixmap()))
            self.night_mode = False
        else:
            self.setStyleSheet("""
                QMainWindow::window-frame {background-color: #555555;}  /* Add this line to style the window header */
                QMainWindow {background-color: #333333; color: white;}
                QPushButton {color: #555555;}
                QPushButton:hover {background-color: #444444; color: white;}
                QPushButton:pressed {background-color: #555555;}
                QTableWidget {background-color: #333333; color: #444444; selection-background-color: #444444;}
                QTableCornerButton::section { background-color:#444444; }
                QHeaderView {background-color: #333333; color: #444444; selection-background-color: #444444;}
                QTableWidget::item {color: white; border: 1px solid #444444; background-color: #555555;}
                QTableWidget::item:selected {background-color: #444444;}
                QTableWidget::item:hover {background-color: #444444;}
                QLabel {color: white; background-color: #555555}
            """)
            self.button_dark_mode.setIcon(QIcon(self.night_mode_image.toqpixmap()))
            self.night_mode = True

    def update_label(self):
        highlighted_text = pyperclip.paste()
        self.label.setText(f"Clipboard Text: {highlighted_text}")

        # Add clipboard text to history list
        if highlighted_text not in self.clipboard_history:
            self.clipboard_history.append(highlighted_text)

        # Update table widget with clipboard history
        self.table_widget.setRowCount(len(self.clipboard_history))
        for i, text in enumerate(self.clipboard_history):
            item = QTableWidgetItem(text)
            self.table_widget.setItem(i, 0, item)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()