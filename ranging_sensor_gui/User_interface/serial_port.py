from PyQt5.QtCore import QThread, pyqtSignal
from Library.serial_port import ranging_sensor_data
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from functools import partial
from Settings.GUI_settings import ERROR_ESTATES, ERROR_MESSAGE
from typing import Union
import serial.tools.list_ports

class SerialWigget(QWidget):
    def __init__(self, port: str, baudrate: int, grid_upate_method):
        super().__init__()
        self.grid_widget_update = grid_upate_method
        main_layout = QVBoxLayout()
        serial_info_layout = QVBoxLayout()
        serial_config_layout = QHBoxLayout()

        self.serial_port_label = QLabel("Serial Port:")
        self.serial_port_entry = QLineEdit()
        self.serial_port_entry.setText(port)
        self.baud_rate_label = QLabel("Baud Rate:")
        self.baud_rate_entry = QLineEdit()
        self.baud_rate_entry.setText(str(baudrate))

        serial_config_layout.addWidget(self.serial_port_label)
        serial_config_layout.addWidget(self.serial_port_entry)
        serial_config_layout.addWidget(self.baud_rate_label)
        serial_config_layout.addWidget(self.baud_rate_entry)
        
        self.text_edit = QTextEdit()
        self.button_connect = QPushButton("Serial connect")
        self.clear_buffer = QPushButton("Clear")

        self.button_connect.clicked.connect(self.on_connect_button_clicked)
        self.clear_buffer.clicked.connect(self.on_clear_button_clicked)


        serial_info_layout.addWidget(self.text_edit)
        serial_info_layout.addWidget(self.button_connect)
        serial_info_layout.addWidget(self.clear_buffer)

        main_layout.addLayout(serial_config_layout)
        main_layout.addLayout(serial_info_layout)

        self.setLayout(main_layout)

        self.serial_reader_thread = SerialReaderThread(port=port, baudrate=baudrate)
        self.serial_reader_thread.data_received.connect(self.on_data_received)
        

    def on_connect_button_clicked(self):
        if not self.serial_reader_thread.is_running:
            
            self.serial_reader_thread.is_running = True
            self.serial_reader_thread.set_port(self.serial_port_entry.text())
            self.serial_reader_thread.set_baudrate(int(self.baud_rate_entry.text()))

            self.serial_reader_thread.start()
            self.button_connect.setStyleSheet("background-color: green; color: white;")
        
        else:
            self.serial_reader_thread.stop()
            self.button_connect.setStyleSheet("background-color: red; color: white;")

    def on_clear_button_clicked(self):
        self.text_edit.clear()


    def on_data_received(self, data: str) -> None:
        self.text_edit.append(data)
        if data != ERROR_MESSAGE.SERIAL_ERROR_MESSSAGE:
            data_list = str_to_list(data)
            if data_list != ERROR_ESTATES.SERIAL_ERROR:
                self.grid_widget_update(data_list)
        else:
            self.serial_reader_thread.stop()
            self.button_connect.setStyleSheet("background-color: red; color: white;")

    def closeEvent(self, event):
        self.serial_reader_thread.stop()
        super().closeEvent(event)
    

class SerialReaderThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, port: str, baudrate: int):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_port = partial(ranging_sensor_data, port=port, baudrate=baudrate)
        self.is_running = False

    def run(self):
        while self.is_running:
            data = self.serial_port()
            self.data_received.emit(data)


    def stop(self):
        self.is_running = False

    def set_port(self, port: str):
        self.port = port
        self.serial_port = partial(ranging_sensor_data, port=port, baudrate=self.baudrate)

    def set_baudrate(self, baudrate: int):
        self.baudrate = baudrate
        self.serial_port = partial(ranging_sensor_data, port=self.port, baudrate=baudrate)


def str_to_list(data: str) -> Union[list[int],ERROR_ESTATES.SERIAL_ERROR]:
    splited_data = data.split()
    if len(splited_data) >0:
        ranging_sensor_data = splited_data[::2]
        ranging_sensor_data = [value.replace('None', '0') for value in ranging_sensor_data]
        ranging_sensor_data = [int(value) for value in ranging_sensor_data]
        return ranging_sensor_data
    else:
        return ERROR_ESTATES.SERIAL_ERROR
