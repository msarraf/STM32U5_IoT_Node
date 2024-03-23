import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from User_interface.serial_port import SerialWigget
from User_interface.ranging_sensor_grid import GridWidget


class MainWindow(QMainWindow):
    def __init__(self, port, baudrate):
        super().__init__()
        self.setWindowTitle("Ranging Sensor")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.grid_window = GridWidget(grid_rows=4, grid_columns=4)
        self.serial_port_window = SerialWigget(port=port, baudrate=baudrate, grid_upate_method=self.grid_window.update_grid)
        

        self.layout.addWidget(self.serial_port_window)
        self.layout.addWidget(self.grid_window)

    def closeEvent(self, event):
        if self.serial_port_window.serial_reader_thread.isRunning:
            self.serial_port_window.serial_reader_thread.terminate()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow(port='COM4', baudrate=115200)
    main_window.show()

    sys.exit(app.exec_())
