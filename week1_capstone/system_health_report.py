from datetime import datetime

print("=== System Health Report Generator ===")

device_name = input("Device name (example: LAPTOP or SERVER01): ").strip()

cpu = int(input("CPU usage % (0-100): "))
ram = int(input("RAM usage % (0-100): "))
disk_free = int(input("Free disk space (GB): "))

def status_percent(value):
    if value >= 90:
        return "CRITICAL"
    elif value >= 75:
        return "WARNING"
    else:
        return "OK"

def status_disk(gb_free):
    if gb_free < 10:
        return "CRITICAL"
    elif gb_free < 30:
        return "WARNING"
    else:
        return "OK"

cpu_status = status_percent(cpu)
ram_status = status_percent(ram)
disk_status = status_disk(disk_free)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = f"""
SYSTEM HEALTH REPORT
Time: {timestamp}
Device: {device_name}

CPU Usage: {cpu}%   Status: {cpu_status}
RAM Usage: {ram}%   Status: {ram_status}
Disk Free: {disk_free} GB   Status: {disk_status}
""".strip()

print("\n" + report)

filename = f"{device_name}_health_report.txt"

with open(filename, "w") as file:
    file.write(report)

print(f"\nSaved report to: {filename}")
print("\nHealth evaluation complete.")