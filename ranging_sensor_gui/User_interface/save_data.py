from Library.serial_port import ranging_sensor_data
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton

class SaveWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
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
        pass

    def closeEvent(self, event):
        super().closeEvent(event)
    

