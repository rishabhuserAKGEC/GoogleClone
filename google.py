import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QComboBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.url_bar = QLineEdit()
        self.search_engines = QComboBox()
        self.search_engines.addItems([
            "Google",
            "Bing",
            "Yahoo",
            "DuckDuckGo"
        ])

        self.search_engines.currentTextChanged.connect(self.update_search_engine)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        layout = QVBoxLayout()
        layout.addWidget(self.search_engines)
        layout.addWidget(self.url_bar)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.search_engine = "https://www.google.com/search?q="
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        query = self.url_bar.text()
        url = self.search_engine + query
        self.browser.setUrl(QUrl(url))

    def update_search_engine(self, engine):
        if engine == "Google":
            self.search_engine = "https://www.google.com/search?q="
        elif engine == "Bing":
            self.search_engine = "https://www.bing.com/search?q="
        elif engine == "Yahoo":
            self.search_engine = "https://search.yahoo.com/search?p="
        elif engine == "DuckDuckGo":
            self.search_engine = "https://duckduckgo.com/?q="

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec_())
