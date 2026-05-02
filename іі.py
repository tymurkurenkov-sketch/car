def login(username, password):
    correct_username = "admin"
    correct_password = "password123"

    try:
        assert username == correct_username and password == correct_password, "Невірне ім'я користувача або пароль"
        
        print("Вхід виконано успішно")
        
    except AssertionError as error:
        print(error)

login("admin", "password123")  # Виведе: Вхід виконано успішно
login("user", "12345")         # Виведе: Невірне ім'я користувача або пароль
