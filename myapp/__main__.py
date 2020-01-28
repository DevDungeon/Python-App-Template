"""
## Reference tutorials

- PyQt5: https://www.devdungeon.com/content/python3-qt5-pyqt5-tutorial
- Tkinter: https://www.devdungeon.com/content/gui-programming-python-tkinter
- PyInstaller: https://www.devdungeon.com/content/pyinstaller-tutorial
- Curses: https://www.devdungeon.com/content/curses-programming-python
"""


def main_gui():
    """
    A simple PyQt5 GUI application that loads a main window from a designer file and creates
    a system tray icon with a right-click menu and can generate notifications.

    :return:
    """
    import sys
    import pkg_resources
    import os
    from PyQt5.QtWidgets import QApplication
    from PyQt5 import uic

    app = QApplication(sys.argv)

    # Or load a UI designer file
    designer_filepath = pkg_resources.resource_filename(__name__, os.path.join("resources", "main_window.ui"))
    win2 = uic.loadUi(designer_filepath)
    win2.show()
    win2.myLabel.setText('Hello world!')

    # System tray icon
    from PyQt5.QtWidgets import QSystemTrayIcon
    from PyQt5.uic.properties import QtGui
    from PyQt5.QtWidgets import QAction, QMenu
    tray_icon = QSystemTrayIcon()
    icon_path = pkg_resources.resource_filename(__name__, os.path.join("resources", "devdungeon500x500.jpg"))
    tray_icon.setIcon(QtGui.QIcon(icon_path))
    tray_menu = QMenu()
    exit_action = QAction("Exit")
    exit_action.triggered.connect(sys.exit)
    tray_menu.addAction(exit_action)
    tray_icon.setContextMenu(tray_menu)  # Set right-click menu
    tray_icon.show()
    # Notifications
    tray_icon.showMessage("Hello!",
                          "App loaded",
                           QSystemTrayIcon.Information,
                           3000)

    sys.exit(app.exec_())



def main_cli():
    """
    A simple curses CLI app

    :return:
    """
    import pkg_resources
    import os
    import sys
    from signal import signal, SIGINT, SIGTERM
    import curses

    def shutdown(self):  # Reset curses to a decent state before exiting unexpectedly
        curses.curs_set(1)
        curses.echo()
        curses.endwin()
        sys.exit(0)

    # Print file from resources directory

    print()

    def main_wrapper(main_screen):
        signal(SIGINT, shutdown)
        signal(SIGTERM, shutdown)

        main_screen.clear()
        main_screen.addstr(2, 2, "It works! Press any key...")

        filepath = pkg_resources.resource_filename(__name__, os.path.join("resources", "test.txt"))
        main_screen.addstr(4, 3, "Contents of test.txt: " + open(filepath).read())

        main_screen.getch()  # Wait for any key press

    curses.wrapper(main_wrapper)


if __name__ == '__main__':
    """
    Default to the CLI main if run directly
    """
    main_cli()
