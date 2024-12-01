from psutil import virtual_memory, swap_memory

class RAM_Monitor:
    def total():
        total_ram = virtual_memory().total / 1073741824
        return round(total_ram, 1)
    
    def available():
        avail_ram = virtual_memory().available / 1073741824
        return round(avail_ram, 1)
    
    def used():
        used_ram = virtual_memory().used / 1073741824
        return round(used_ram, 1)
    
    def free():
        free_ram = virtual_memory().free / 1073741824
        return round(free_ram, 1)
    
    def percent():
        return virtual_memory().percent

class SWAP_Monitor:
    def total():
        total_swap = swap_memory().total / 1073741824
        return round(total_swap, 1)
    
    def used():
        used_swap = swap_memory().used / 1073741824
        return round(used_swap, 1)
    
    def free():
        free_swap = swap_memory().free / 1073741824
        return round(free_swap, 1)
    
    def percent():
        return swap_memory().percent