def treat_user_input_data(user_input) -> list:
    user_data = list(user_input.split(","))

    if len(user_data) != 7:
        raise ValueError(
            "Número incorreto de valores digitados, 7 valores são esperados."
        )

    if user_data[0] == "Lisbon":
        user_data[0] = 0
    elif user_data[0] == "Oporto":
        user_data[0] = 1
    elif user_data[0] == "Other":
        user_data[0] = 2
    else:
        raise ValueError(
            "Valor inválido para a região. Use 'Lisbon', 'Oporto' ou 'Other'."
        )

    user_data = [float(i) for i in user_data]

    return user_data
