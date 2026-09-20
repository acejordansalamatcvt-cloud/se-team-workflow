def login(username, password):
    if username == "admin" and password == "password":
        return "Login successful"
    return "Invalid username or password"


print(login("admin", "password"))