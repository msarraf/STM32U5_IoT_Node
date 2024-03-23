import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from User_interface.serial_port import SerialWigget
from User_interface.ranging_sensor_grid import GridWidget
from User_interface.save_data import SaveWidget


class MainWindow(QMainWindow):
    def __init__(self, port, baudrate):
        super().__init__()
        self.setWindowTitle("Ranging Sensor")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout(self.central_widget)

        rs_layout = self.ranging_sensor_layout(port=port, baudrate=baudrate)

        sd_layout = self.save_data_layout()

        self.main_layout.addLayout(rs_layout)
        self.main_layout.addLayout(sd_layout)


    def save_data_layout(self) -> QVBoxLayout:
        sd_layout = QVBoxLayout()
        save_data_window = SaveWidget()
        sd_layout.addWidget(save_data_window)
        return sd_layout

    def ranging_sensor_layout(self, port: str, baudrate: int) -> QVBoxLayout:
        ranging_sensor_layout = QVBoxLayout()
        grid_window = GridWidget(grid_rows=4, grid_columns=4)
        self.serial_port_window = SerialWigget(port=port, baudrate=baudrate, grid_upate_method=grid_window.update_grid)
        ranging_sensor_layout.addWidget(self.serial_port_window)
        ranging_sensor_layout.addWidget(grid_window)
        return ranging_sensor_layout

    def closeEvent(self, event):
        if self.serial_port_window.serial_reader_thread.isRunning:
            self.serial_port_window.serial_reader_thread.terminate()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow(port='COM4', baudrate=115200)
    main_window.show()

    sys.exit(app.exec_())
