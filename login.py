def login_check(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Login Failed"

test_data = [
    ("admin", "1234"),
    ("admin", "0000"),
    ("user", "1234"),
    ("user", "0000")
]

test_case_no = 1

for username, password in test_data:
    result = login_check(username, password)
    print(f"Test Case {test_case_no}: username={username}, password={password} -> {result}")
    test_case_no += 1
