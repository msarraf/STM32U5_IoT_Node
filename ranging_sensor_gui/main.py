import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal

class SerialReaderThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, serial_port):
        super().__init__()
        self.serial_port = serial_port
        self.is_running = True

    def run(self):
        while self.is_running:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline().decode().strip()
                self.data_received.emit(data)

    def stop(self):
        self.is_running = False

class MainWindow(QMainWindow):
    def __init__(self, serial_port):
        super().__init__()
        self.setWindowTitle("Serial Monitor")

        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.serial_reader_thread = SerialReaderThread(serial_port)
        self.serial_reader_thread.data_received.connect(self.on_data_received)
        self.serial_reader_thread.start()

    def on_data_received(self, data):
        self.text_edit.append(data)

    def closeEvent(self, event):
        self.serial_reader_thread.stop()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    serial_port = serial.Serial('COM4', baudrate=115200)

    main_window = MainWindow(serial_port)
    main_window.show()

    sys.exit(app.exec_())
