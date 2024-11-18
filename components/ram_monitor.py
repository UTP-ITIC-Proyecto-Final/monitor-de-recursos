from psutil import virtual_memory, swap_memory

class RAM_Monitor:
    def __init__(self):
        self.ram = virtual_memory()
    
    def total(self):
        total_ram = self.ram.total / 1073741824
        return round(total_ram, 1) 
    
    def available(self):
        avail_ram = self.ram.available / 1073741824
        return round(avail_ram, 1)
    
    def used(self):
        used_ram = self.ram.used / 1073741824
        return round(used_ram, 1)
    
    def free(self):
        free_ram = self.ram.free / 1073741824
        return round(free_ram, 1)
    
    def percent(self):
        percent_ram = self.ram.percent
        return percent_ram

class SWAP_Monitor:
    def __init__(self):
        self.swap = swap_memory()
    
    def total(self):
        total_swap = self.swap.total / 1073741824
        return round(total_swap, 1)
    
    def used(self):
        used_swap = self.swap.used / 1073741824
        return round(used_swap, 1)
    
    def free(self):
        free_swap = self.swap.free / 1073741824
        return round(free_swap, 1)

if "__main__" == __name__:
    ram = RAM_Monitor()
    swap = SWAP_Monitor()
    
    print(virtual_memory().total / 1073741824)