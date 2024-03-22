import sys
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel
import matplotlib.pyplot as plt
import numpy as np


class GridWidget(QWidget):
    def __init__(self, grid_rows: int, grid_columns: int):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.labels = []
        self.create_grid(grid_rows, grid_columns)
        self._colors = 'green'
        
        

    def create_grid(self, grid_rows, grid_columns):
        for row in range(grid_rows):
            for col in range(grid_columns):
                index = row * 8 + col
                label = QLabel(str("0"))
                label.setStyleSheet(f"background-color: green; color: white;")
                self.grid_layout.addWidget(label, row, col)
                self.labels.append(label)

        
    def update_grid(self, data: list[int]):
        pass

def generate_colormap(num_points):

    cmap = plt.cm.viridis
    
    colors = cmap(np.linspace(0, 1, num_points))

    return colors