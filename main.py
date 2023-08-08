import json
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def encontrarDuplicado(jsonFile):
    mapper = {}
    for user in jsonFile:
        if user["Email"] in mapper:
            mapper[user["Email"]] = mapper[user["Email"]] + 1
        else:
            mapper[user["Email"]] = 1
    valor_max = max(mapper.values())
    if valor_max <= 1:
        valor_max = 2

    duplicados = [
        k for k, v in mapper.items() if v == valor_max
    ]
    return duplicados

def encontrarSinNombreNiRol(jsonFile):
    listado = []
    for file in jsonFile:
        if file["Rol"] != "" and file["Nombre"] == "":
            listado.append(file["Email"])
    return listado

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open("archivoDeUsuarios.json", "r")
    jsonFile = json.loads(file.read())
    file.close()
    print(encontrarDuplicado(jsonFile))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
