import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools

def cpu_graph(cpu_usage_method, interval, frame, title):
    fig, ax = plt.subplots(figsize=[6,3])
    ax.set_title(f'{title} Over Time')
    ax.set_ylabel(f'{title} (%)')
    ax.set_ylim(0, 100)
    ax.get_xaxis().set_visible(False)

    x_data = []
    y_data = []
    counter = itertools.count()

    max_points = 10

    def update(frame):
        x_data.append(next(counter))
        y_data.append(cpu_usage_method())

        if len(x_data) > max_points:
            x_data.pop(0)
            y_data.pop(0)

        ax.clear()
        ax.stackplot(x_data, y_data, colors=['#2b8de3'])
        ax.grid()
        ax.set_title(f'{title} Over Time')
        ax.set_ylabel(f'{title} (%)')
        ax.set_ylim(0, 100)
        ax.set_xlim(min(x_data), max(x_data))

    ani = FuncAnimation(fig, update, interval=interval, cache_frame_data=False)

    # Incrustar la gráfica en el frame de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def ram_graph(ram_usage_method, interval, frame, title):
    fig, ax = plt.subplots(figsize=[6,3])
    ax.set_title(f'{title} Over Time')
    ax.set_ylabel(f'{title} (%)')
    ax.set_ylim(0, 100)
    ax.get_xaxis().set_visible(False)

    x_data = []
    y_data = []
    counter = itertools.count()

    max_points = 10

    def update(frame):
        x_data.append(next(counter))
        y_data.append(ram_usage_method())

        if len(x_data) > max_points:
            x_data.pop(0)
            y_data.pop(0)

        ax.clear()
        ax.stackplot(x_data, y_data, colors=['#2b8de3'])
        ax.grid()
        ax.set_title(f'{title} Over Time')
        ax.set_ylabel(f'{title} (%)')
        ax.set_ylim(0, 100)
        ax.set_xlim(min(x_data), max(x_data))

    ani = FuncAnimation(fig, update, interval=interval, cache_frame_data=False)

    # Incrustar la gráfica en el frame de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def swap_graph(swap_usage_method, interval, frame, title):
    fig, ax = plt.subplots(figsize=[6,3])
    ax.set_title(f'{title} Over Time')
    ax.set_ylabel(f'{title} (%)')
    ax.set_ylim(0, 100)
    ax.get_xaxis().set_visible(False)

    x_data = []
    y_data = []
    counter = itertools.count()

    max_points = 10

    def update(frame):
        x_data.append(next(counter))
        y_data.append(swap_usage_method())

        if len(x_data) > max_points:
            x_data.pop(0)
            y_data.pop(0)

        ax.clear()
        ax.stackplot(x_data, y_data, colors=['#2b8de3'])
        ax.grid()
        ax.set_title(f'{title} Over Time')
        ax.set_ylabel(f'{title} (%)')
        ax.set_ylim(0, 100)
        ax.set_xlim(min(x_data), max(x_data))

    ani = FuncAnimation(fig, update, interval=interval, cache_frame_data=False)

    # Incrustar la gráfica en el frame de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)