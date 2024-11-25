from psutil import disk_partitions, disk_usage

class Disk_Monitor:
    def __init__(self):
        self.disk_part = disk_partitions(all=True)

    def partitions(self):
        partitions = {}
        
        for part in self.disk_part:
            partitions[part.mountpoint] = part.fstype
        
        return partitions

    def usage(self):
        usage_list = []
        
        for path in self.partitions():
            usage_list.append({
                "path": path,
                "total": round(disk_usage(path).total / 1073741824, 1),
                "free": round(disk_usage(path).free / 1073741824, 1),
                "used": round(disk_usage(path).used / 1073741824, 1)
            })

        return usage_list

if "__main__" == __name__:
    # print(disk_io_counters())
    # print(disk_usage("E:/"))
    # print(disk_partitions(all=True)[0].mountpoint)
    
    disk = Disk_Monitor()
    print(list(disk.partitions().keys()))
    for i in disk.usage():
        print(f"{i['path']} = {i['used']} GB / {i['total']} GB")