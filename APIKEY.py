def replace_api_key(file_path, old_key, new_key):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        replaced = False  # Flaga informująca, czy klucz API został podmieniony
        for line in lines:
            if old_key in line:
                line = line.replace(old_key, new_key)
                replaced = True
            file.write(line)

        return replaced

# Wczytanie klucza API
api_key = input("Wprowadź nowy klucz API: ")

# Podmiana klucza API w pliku
is_replaced = replace_api_key("data.txt", "STARY_KLUCZ_API", api_key)

if is_replaced:
    print("Klucz API został pomyślnie zaktualizowany w pliku.")
else:
    print("Nie znaleziono linii z kluczem API do podmiany.")

