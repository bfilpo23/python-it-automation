username = input("Username: ")
role = input("Role (admin/user): ").strip().lower()

if role == "admin":
    print(f"Access granted: {username} has admin permissions.")
else:
    print(f"Access limited: {username} has standard user permissions.")
