from Library.serial_port import ranging_sensor_data
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton
from dataclasses import dataclass

@dataclass
class RangingData:
    ranging_values: list[int]
    label: str

class SaveWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.ranging_data = []
        
        self.text_edit = QTextEdit()
        self.button_save = QPushButton("Save Data")
        self.clear_label = QPushButton("Clear")

        self.button_save.clicked.connect(self.on_save_button_clicked)
        self.clear_label.clicked.connect(self.on_cl_button_clicked)


        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_save)
        layout.addWidget(self.clear_label)

        self.setLayout(layout)

    def on_save_button_clicked(self):
        pass

    def on_cl_button_clicked(self):
        self.ranging_data = []
        self.text_edit.clear()

    def closeEvent(self, event):
        super().closeEvent(event)
    
    def text_edit_update(self, data: list[int]) -> None:
        ranging_data = RangingData(ranging_values=data, label='Empty')
        self.ranging_data.append(ranging_data)
        self.text_edit.append(str(ranging_data))
    

