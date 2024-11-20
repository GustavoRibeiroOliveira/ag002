import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

from utils import treat_user_input_data

file_name = "data_set.csv"
data_set = pd.read_csv(file_name)

data_set["Channel"] = data_set["Channel"].replace({"HoReCa": 0, "Retail": 1})
data_set["Region"] = data_set["Region"].replace(
    {"Lisbon": 0, "Oporto": 1, "Other": 2}
)

new_columns_order = [
    "Region",
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicatessen",
    "Channel",
]
data_set = data_set.reindex(columns=new_columns_order)

data = data_set.iloc[:, :-1]
results = data_set["Channel"]
data_train, data_test, results_train, results_test = train_test_split(
    data, results, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier(random_state=42)

model.fit(data_train.values, results_train)
y_pred = model.predict(data_test)

print("Relatório de classificação:")
print(classification_report(results_test, y_pred))


def classify_user_input() -> bool:
    print(
        "\nInsira os dados para classificação na seguinte ordem: Region, Fresh, Milk, Grocery, Frozen, "
        "Detergents_Paper, Delicatessen \nOu caso queira parar a execução, basta entrar com o valor 0"
    )
    user_input = input("Digite os valores separados por vírgula: ").strip()
    if user_input[0] == "0":
        return False
    try:
        user_data = treat_user_input_data(user_input)

        prediction = model.predict([user_data])
        channel = "HoReCa" if prediction[0] == 0 else "Retail"
        print(f"O canal de vendas classificado é: {channel}")
    except Exception as e:
        print(f"Erro ao processar os dados: {e}")
    return True


is_to_continue = True
while is_to_continue:
    is_to_continue = classify_user_input()
