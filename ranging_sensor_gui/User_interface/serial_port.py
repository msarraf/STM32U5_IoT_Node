from PyQt5.QtCore import QThread, pyqtSignal
from Library.serial_port import ranging_sensor_data
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton
from functools import partial
from Settings.GUI_settings import ERROR_ESTATES
from typing import Union

class SerialWigget(QWidget):
    def __init__(self, port: str, baudrate: int, grid_upate_method):
        super().__init__()
        self.grid_widget_update = grid_upate_method
        layout = QVBoxLayout()
        
        self.text_edit = QTextEdit()
        self.button_connect = QPushButton("Serial connect")
        self.clear_buffer = QPushButton("Clear")

        self.button_connect.clicked.connect(self.on_connect_button_clicked)
        self.clear_buffer.clicked.connect(self.on_clear_button_clicked)


        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_connect)
        layout.addWidget(self.clear_buffer)

        self.setLayout(layout)

        self.serial_reader_thread = SerialReaderThread(port=port, baudrate=baudrate)
        self.serial_reader_thread.data_received.connect(self.on_data_received)
        

    def on_connect_button_clicked(self):
        if not self.serial_reader_thread.is_running:
            
            self.serial_reader_thread.is_running = True
            self.serial_reader_thread.start()
            self.button_connect.setStyleSheet("background-color: green; color: white;")
        
        else:
            self.serial_reader_thread.stop()
            self.button_connect.setStyleSheet("background-color: red; color: white;")

    def on_clear_button_clicked(self):
        self.text_edit.clear()


    def on_data_received(self, data: str) -> None:
        self.text_edit.append(data)
        data_list = str_to_list(data)
        if data_list != ERROR_ESTATES.SERIAL_ERROR:
            self.grid_widget_update(data_list)

    def closeEvent(self, event):
        self.serial_reader_thread.stop()
        super().closeEvent(event)
    

class SerialReaderThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, port: str, baudrate: int):
        super().__init__()
        self.serial_port = partial(ranging_sensor_data, port=port, baudrate=baudrate)
        self.is_running = False

    def run(self):
        while self.is_running:
            data = self.serial_port()
            self.data_received.emit(data)

    def stop(self):
        self.is_running = False

def str_to_list(data: str) -> Union[list[int],ERROR_ESTATES.SERIAL_ERROR]:
    splited_data = data.split()
    if len(splited_data) >0:
        ranging_sensor_data = splited_data[::2]
        ranging_sensor_data = [value.replace('None', '0') for value in ranging_sensor_data]
        ranging_sensor_data = [int(value) for value in ranging_sensor_data]
        return ranging_sensor_data
    else:
        return ERROR_ESTATES.SERIAL_ERROR

