import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class AnimatedPlot(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        
        self.x = np.linspace(0, 2 * np.pi, 100)
        self.line, = self.ax.plot([], [])
        
        self.ani = FuncAnimation(self.figure, self.update_plot, frames=np.arange(0, 2 * np.pi, 0.1), blit=True)

    def update_plot(self, frame):
        self.line.set_data(self.x, np.sin(self.x + frame))
        self.ax.relim()
        self.ax.autoscale_view()
        return self.line,

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        self.animated_plots = [AnimatedPlot(self) for _ in range(3)]
        self.slider = QSlider()
        
        self.slider.valueChanged.connect(self.slider_changed)
        
        for animated_plot in self.animated_plots:
            self.layout.addWidget(animated_plot)
        
        self.layout.addWidget(self.slider)
        
    def slider_changed(self, value):
        for animated_plot in self.animated_plots:
            animated_plot.ani.event_source.interval = 1000 // value

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
