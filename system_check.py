import psutil
import subprocess

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent, mem.total, mem.available

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent, disk.total, disk.free

def get_system_uptime():
    uptime_seconds = float(subprocess.check_output(['cat', '/proc/uptime']).split()[0])
    uptime_hours = uptime_seconds / 3600
    return round(uptime_hours, 2)

def get_cpu_temperature():
    try:
        temp_output = subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp']).decode()
        temp_celsius = int(temp_output) / 1000
        return temp_celsius
    except Exception as e:
        return "Unable to fetch temperature: " + str(e)

def main():
    print("Banana Pi M1 System Health Check\n")
    
    # CPU Usage
    print(f"CPU Usage: {get_cpu_usage()}%")
    
    # Memory Usage
    mem_percent, mem_total, mem_available = get_memory_usage()
    print(f"Memory Usage: {mem_percent}%")
    print(f"Total Memory: {mem_total / (1024 * 1024):.2f} MB")
    print(f"Available Memory: {mem_available / (1024 * 1024):.2f} MB")
    
    # Disk Usage
    disk_percent, disk_total, disk_free = get_disk_usage()
    print(f"Disk Usage: {disk_percent}%")
    print(f"Total Disk Space: {disk_total / (1024 * 1024 * 1024):.2f} GB")
    print(f"Free Disk Space: {disk_free / (1024 * 1024 * 1024):.2f} GB")
    
    # Uptime
    print(f"System Uptime: {get_system_uptime()} hours")
    
    # CPU Temperature
    print(f"CPU Temperature: {get_cpu_temperature()}°C")
    
if __name__ == "__main__":
    main()
