import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


def main():
    """Main entry point for the QtQuick application."""
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    
    # Get the path to main.qml (in the ui/ directory relative to project root)
    project_root = Path(__file__).parent.parent
    qml_file = project_root / "ui" / "main.qml"
    
    # Load the QML file
    engine.load(qml_file)
    
    # Check if the root object was created successfully
    if not engine.rootObjects():
        print("Error: Failed to load QML file", file=sys.stderr)
        sys.exit(-1)
    
    # Run the application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

