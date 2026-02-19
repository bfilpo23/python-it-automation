servers = ["WEB01", "DB01", "APP01"]

for server in servers:
    disk_free = int(input(f"Enter free disk space for {server} in GB: "))

    if disk_free < 10:
        status = "CRITICAL"
    elif disk_free < 30:
        status = "WARNING"
    else:
        status = "OK"

    print(f"[{status}] {server} has {disk_free}GB free.")
    print("-" * 40)
