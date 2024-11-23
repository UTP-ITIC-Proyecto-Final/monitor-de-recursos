from psutil import disk_partitions, disk_usage, disk_io_counters



if "__main__" == __name__:
    # print(disk_io_counters())
    # print(disk_usage("E:/"))
    print(disk_partitions(all=True))