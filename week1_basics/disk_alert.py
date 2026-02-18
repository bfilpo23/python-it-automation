disk_free = int(input("Enter free disk space in GB: "))

if disk_free < 10:
    print("CRITICAL: Disk space dangerously low!")
elif disk_free < 30:
    print("WARNING: Disk space getting low.")
else:
    print("OK: Disk space is healthy.")
