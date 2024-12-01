import tkinter as tk
from utils.graphs import cpu_graph, ram_graph, swap_graph
from components.cpu_monitor import CPU_Monitor
from components.ram_monitor import RAM_Monitor, SWAP_Monitor

class ResourceMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resource Monitor")
        self.root.geometry("600x940")

        # Crear un Frame para los gráficos
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Inicializar los gráficos de CPU, RAM y SWAP en la ventana principal
        self.show_cpu_graph()
        self.show_ram_graph()
        self.show_swap_graph()

    def show_cpu_graph(self):
        self._show_graph(cpu_graph, CPU_Monitor().percent, 1000, "CPU Usage")

    def show_ram_graph(self):
        self._show_graph(ram_graph, RAM_Monitor.percent, 1000, "RAM Usage")

    def show_swap_graph(self):
        self._show_graph(swap_graph, SWAP_Monitor.percent, 1000, "SWAP Usage")

    def _show_graph(self, graph_function, usage_method, interval, title):
        # Crear un nuevo frame dentro del Frame principal para cada gráfico
        graph_frame = tk.Frame(self.frame)
        graph_frame.grid(row=len(self.frame.winfo_children()), column=0, pady=10, padx=10, sticky="nsew")

        # Llamar a la función del gráfico
        graph_function(usage_method, interval, graph_frame, title)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ResourceMonitorApp(root)

        root.mainloop()
    except KeyboardInterrupt:
        print("Leaving...")
        exit(0)