from psutil import cpu_count, cpu_freq, cpu_percent, cpu_stats, cpu_times, cpu_times_percent
from subprocess import check_output

class CPU_Monitor:
    def __init__(self):
        self.cpu_threads = cpu_count()
        self.cpu_freq = cpu_freq()
        self.cpu_percent = cpu_percent()
        self.cpu_stats = cpu_stats()
        self.cpu_times = cpu_times()
        self.cpu_times_percent = cpu_times_percent()
    
    def cores(self):
        cores = int(check_output("wmic cpu get NumberOfCores").decode("utf-8").strip().replace("NumberOfCores  \r\r\n", ""))
        threads = self.cpu_threads
        return {
            "núcleos": cores,
            "hilos": threads
        }

    def frequency(self):
        current = self.cpu_freq.current / 1000
        min = self.cpu_freq.min / 1000
        max = self.cpu_freq.max / 1000
        
        return {
            "current": current,
            "min": min,
            "max": max
        }

if "__main__" == __name__:
    cpu = CPU_Monitor()
    
    print(cpu.cores())
    # print(cpu_freq())