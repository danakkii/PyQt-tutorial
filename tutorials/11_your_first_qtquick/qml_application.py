import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView

if __name__ == "main":
    app = QApplication()
    view = QQuickView()

    view.setSource("view.qml")
    view.show()
    sys.exit(app.exec())

    