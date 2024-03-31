from Library.serial_port import ranging_sensor_data
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton, QMessageBox, QLabel, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal
from utils.utils import save_data_to_csv
from datasets.RangingSensor import RangingData

class SaveWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.ranging_data = []
        
        self.text_edit = QTextEdit()
        self.button_save = QPushButton("Save Data")
        self.clear_label = QPushButton("Clear")

        self.label_tag_label = QLabel("Label:")
        self.label_tag = QLineEdit()
        
        self.button_save.clicked.connect(self.on_save_button_clicked)
        self.clear_label.clicked.connect(self.on_cl_button_clicked)

        layout.addWidget(self.label_tag_label)
        layout.addWidget(self.label_tag)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button_save)
        layout.addWidget(self.clear_label)

        self.setLayout(layout)

        self.save_data_thread = SaveDataThread()
        self.save_data_thread.saved_data.connect(self.on_data_saved)

    def on_save_button_clicked(self):
        if not self.ranging_data:
            QMessageBox.warning(self, "Warning", "No data to save!")
            return
        if not self.label_tag.text():
            QMessageBox.warning(self, "Warning", "No label specified!")
            return
        self.save_data_thread.set_data(self.ranging_data)
        self.save_data_thread.set_label(self.label_tag.text())
        self.save_data_thread.start()

    def on_cl_button_clicked(self):
        self.ranging_data = []
        self.text_edit.clear()

    def closeEvent(self, event):
        super().closeEvent(event)
    
    def text_edit_update(self, data: list[int]) -> None:
        ranging_data = RangingData(ranging_values=data, label=self.label_tag.text())
        self.ranging_data.append(ranging_data)
        self.text_edit.append(str(ranging_data))

    def on_data_saved(self, message: str) -> None:
        self.text_edit.clear()
        self.text_edit.append(message)
        if self.save_data_thread.isRunning:
            self.save_data_thread.terminate()
        

class SaveDataThread(QThread):
    saved_data = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._data: RangingData
        self._label: str
        
    def run(self):
        for data in self._data:
            if data.label == '':
                data.label = self._label
        save_data_to_csv(data=self._data)
        self.saved_data.emit("data saved")

    def set_data(self, data: RangingData) -> None:
        self._data = data

    def set_label(self, label: str) -> None:
        self._label = label

    

