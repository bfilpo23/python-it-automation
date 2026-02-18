while True:
    server_name = input("Enter server name (or type 'exit' to quit): ").strip()
    
    if server_name.lower() == "exit":
        print("Monitoring session ended.")
        break

    disk_free = int(input(f"Enter free disk space for {server_name} in GB: "))

    if disk_free < 10:
        status = "CRITICAL"
    elif disk_free < 30:
        status = "WARNING"
    else:
        status = "OK"

    print(f"[{status}] {server_name} has {disk_free}GB free.")
    print("-" * 40)
