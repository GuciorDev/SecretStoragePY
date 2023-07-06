import hashlib

# Read the contents of data.txt
with open("data.txt", "r") as file:
    lines = file.readlines()

# Iterate over the lines and encode the relevant fields
encoded_lines = []
for line in lines:
    if line.startswith("Name:"):
        name = line.split(": ")[1].strip()
        encoded_name = hashlib.sha256(name.encode()).hexdigest()
        encoded_lines.append("Name: {}\n".format(encoded_name))
    elif line.startswith("Surname:"):
        surname = line.split(": ")[1].strip()
        encoded_surname = hashlib.sha256(surname.encode()).hexdigest()
        encoded_lines.append("Surname: {}\n".format(encoded_surname))
    elif line.startswith("Email:"):
        email = line.split(": ")[1].strip()
        encoded_email = hashlib.sha256(email.encode()).hexdigest()
        encoded_lines.append("Email: {}\n".format(encoded_email))
    elif line.startswith("Field"):
        field_value = line.split(": ")[1].strip()
        encoded_field_value = hashlib.sha256(field_value.encode()).hexdigest()
        encoded_lines.append("Field {}: {}\n".format(line.split(": ")[0], encoded_field_value))
    else:
        encoded_lines.append(line)

# Save the encoded data back to data.txt
with open("data.txt", "w") as file:
    file.writelines(encoded_lines)

print("Data encoded successfully.")
