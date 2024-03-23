from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from PyQt5.QtCore import Qt

class GridWidget(QWidget):
    def __init__(self, grid_rows: int, grid_columns: int):
        super().__init__()
        self.colors = generate_colormap(grid_columns * grid_rows)
        self.grid_rows = grid_rows
        self.grid_columns = grid_columns
        self.grid_size = 100
        self.grid_layout = QGridLayout(self)
        self.labels = []
        self.create_grid()
        
        
        
    def create_grid(self) -> None:
        self.setFixedSize(self.grid_size * self.grid_columns, self.grid_size * self. grid_rows)
        for row in range(self.grid_rows):
            for col in range(self.grid_columns):
                index = row * self.grid_rows + col
                label = QLabel(str("0"))
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(f"background-color: {self.colors[index]}; color: white;")
                self.grid_layout.addWidget(label, row, col)
                self.labels.append(label)

        
    def update_grid(self, data: list[int]) -> None:
        sorted_colors = self.sort_colors(data)
        if len(data) == self.grid_columns * self.grid_rows:
            for row in range(self.grid_rows):
                for col in range(self.grid_columns):
                    index = row * self.grid_rows + col
                    self.labels[index].setText(str(data[index]))
                    self.labels[index].setStyleSheet(f"background-color: {sorted_colors[index]}; color: white;")


    def sort_colors(self, data: list[int]) -> list[int]:
        sorted_data = sorted(data)
        sorted_colors = []
        for value in data:
            sorted_colors.append(self.colors[sorted_data.index(value)])
        return sorted_colors


def generate_colormap(num_points:int) -> list[hex]:

    cmap = plt.cm.viridis
    
    colors = [mcolors.to_hex(cmap(i / num_points)) for i in range(num_points)]

    return colors

