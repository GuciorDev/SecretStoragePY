import json
from tkinter import *
from tkinter import filedialog, messagebox
import random
import tkinter as tk
import sys

# Define the lists to store API entries, remove buttons, and frames
api_entries = []
remove_api_buttons = []
api_frames = []

label_color = "#FFFFFF"  # White
entry_bg = "#2B2B2B"  # Dark gray
button_bg = "#3CB371"  # Lime green
button_fg = "#FFFFFF"  # White

MAX_ATTEMPTS = 3

def password_is_correct():
    entered_password = password_entry.get()
    return entered_password == "1234"

def on_validation_window_close():
    global attempts
    attempts = 0
    sys.exit()

def validate_password():
    global attempts
    if not password_entry.winfo_exists():
        sys.exit()

    if password_is_correct():
        main_window()
    else:
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            error_label.config(text="Incorrect password. Maximum attempts reached.")
            validate_button.config(state=tk.DISABLED)
            sys.exit()
        else:
            error_label.config(text="Incorrect password. Attempts remaining: {}".format(MAX_ATTEMPTS - attempts))

def on_password_window_close():
    sys.exit()

def set_tab_order(window):
    # Set tab navigation order
    window.focus_set()

    # Set focus traversal keys to allow tab and shift+tab navigation
    window.bind('<Tab>', lambda e: window.focus_next())
    window.bind('<Shift-Tab>', lambda e: window.focus_prev())

    # Set default button for Enter key
    window.bind('<Return>', lambda e: button_save.invoke())

def main_window():
    # Create your main window and add the necessary configuration and widgets
    # ...

    validation_window.destroy()
    set_tab_order(main_window)  # Call set_tab_order to enable tab and enter navigation
    main_window.protocol("WM_DELETE_WINDOW", sys.exit)  # Close app when main window is closed
    main_window.mainloop()

validation_window = tk.Tk()
password_entry = tk.Entry(validation_window, show="*")
password_entry.pack()
validate_button = tk.Button(validation_window, text="Validate", command=validate_password)
validate_button.pack()
error_label = tk.Label(validation_window, fg="red")
error_label.pack()

attempts = 0

validation_window.protocol("WM_DELETE_WINDOW", on_validation_window_close)
validation_window.mainloop()

def save_details():
    name = entry_name.get()
    surname = entry_surname.get()
    email = entry_email.get()
    field_values = [entry.get() for label, entry, remove_button in field_entries]

    # Create a dictionary to store the data
    data = {
        "Name": name,
        "Surname": surname,
        "Email": email,
        "Custom Fields": {f"Field {random.randint(0, 10) + 1}": value for value in field_values}
    }

    # Open a file dialog to select the save location
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])

    if file_path:
        # Save the data as a JSON file
        with open(file_path, "w") as file:
            json.dump(data, file)

        # Clear the input fields
        entry_name.delete(0, END)
        entry_surname.delete(0, END)
        entry_email.delete(0, END)

        # Clear dynamic fields and remove buttons
        for label, entry, remove_button in field_entries:
            label.destroy()
            entry.destroy()
            remove_button.destroy()
        field_entries.clear()

        messagebox.showinfo("Information", "Data saved successfully.")

        # Adjust the position of the Save button
        button_save.grid(row=4, column=0, columnspan=2, pady=10, sticky=N)
        button_load.grid(row=4, column=1, columnspan=2, pady=10, sticky=N)
def load_details():
    global entry_name, entry_surname, entry_email, field_entries

    # Open a file dialog to select the JSON file
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])

    if file_path:
        try:
            # Load the data from the JSON file
            with open(file_path, "r") as file:
                data = json.load(file)

            # Update the entry fields with the loaded data
            entry_name.delete(0, END)
            entry_name.insert(0, data.get("Name", ""))

            entry_surname.delete(0, END)
            entry_surname.insert(0, data.get("Surname", ""))

            entry_email.delete(0, END)
            entry_email.insert(0, data.get("Email", ""))

            # Clear dynamic fields and remove buttons
            for label, entry, remove_button in field_entries:
                label.destroy()
                entry.destroy()
                remove_button.destroy()
            field_entries.clear()

            # Load custom fields
            custom_fields = data.get("Custom Fields", {})
            for field_name, value in custom_fields.items():
                # Create the field label
                label_field_name = Label(details_frame, text=field_name + ":", bg="#222222", fg=label_color, anchor=W)
                label_field_name.grid(row=len(field_entries) + 4, column=0, sticky=W, pady=5)

                # Create the field entry
                field_entry = Entry(details_frame, bg=entry_bg, fg=label_color)
                field_entry.grid(row=len(field_entries) + 4, column=1, sticky=W, pady=5)
                field_entry.insert(0, value)

                # Create the "X" button for removing the field
                remove_button = Button(details_frame, text="-", bg="red", command=lambda: remove_fields(label_field_name, field_entry, remove_button))
                remove_button.grid(row=len(field_entries) + 4, column=2, sticky=W)

                # Append the label, entry, and remove button to the field_entries list
                field_entries.append((label_field_name, field_entry, remove_button))

        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON file.")


def add_field():
    field_name = entry_field_name.get().strip()
    if field_name:
        # Create the field label
        label_field_name = Label(details_frame, text=field_name + ":", bg="#222222", fg=label_color, anchor=W)
        label_field_name.grid(row=len(field_entries) + 4, column=0, sticky=W, pady=5)

        # Create the field entry
        field_entry = Entry(details_frame, bg=entry_bg, fg=label_color)
        field_entry.grid(row=len(field_entries) + 4, column=1, sticky=W, pady=5)

        # Create the "X" button for removing the field
        remove_button = Button(details_frame, text="-", bg="red", command=lambda: remove_fields(label_field_name, field_entry, remove_button))
        remove_button.grid(row=len(field_entries) + 4, column=2, sticky=W)

        # Append the label, entry, and remove button to the field_entries list
        field_entries.append((label_field_name, field_entry, remove_button))

        # Clear the entry field
        entry_field_name.delete(0, END)

        # Adjust the position of the Save button
        button_save.grid(row=len(field_entries) + 6, column=0, columnspan=3, pady=10, sticky=N)

def remove_fields(label, entry, remove_button):
    # Display confirmation messagebox
    confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to delete this field?", icon="warning")
    if confirmation == "yes":
        # Destroy the label, entry, and remove button
        label.destroy()
        entry.destroy()
        remove_button.destroy()

        # Remove the field entries from the list
        field_entries.remove((label, entry, remove_button))

        # Adjust the position of the Save button
        button_save.grid(row=len(field_entries) + 6, column=0, columnspan=3, pady=10, sticky=N)

def remove_api_field(api_entry_frame):
    # Display confirmation messagebox
    confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to delete this API field?", icon="warning")
    if confirmation == "yes":
        # Find the index of the API entry frame
        index = api_frames.index(api_entry_frame)

        api_entry_frame.destroy()
        api_entries.pop(index)
        remove_api_buttons.pop(index)
        api_frames.pop(index)

        for i in range(index, len(api_frames)):
            api_frames[i].pack_configure(anchor=W, pady=5)

def add_api_field():
    api_name = entry_api.get().strip()
    if api_name:
        # Create a new API field entry
        api_entry_frame = Frame(api_frame, bg="#222222")
        api_entry_frame.pack(anchor=W, pady=5)

        # Create labels for "API Name" and "API Key"
        label_api_name = Label(api_entry_frame, text="API Name:", bg="#222222", fg=label_color)
        label_api_name.pack(side=LEFT)

        label_api_key = Label(api_entry_frame, text="API Key:", bg="#222222", fg=label_color)
        label_api_key.pack(side=LEFT, padx=10)

        # Create entry fields for "API Name" and "API Key"
        entry_api_name = Entry(api_entry_frame, bg=entry_bg, fg=label_color)
        entry_api_name.pack(side=LEFT)

        entry_api_key = Entry(api_entry_frame, bg=entry_bg, fg=label_color)
        entry_api_key.pack(side=LEFT, padx=10)

        # Create a "X" button to remove the API field
        button_remove_api = Button(api_entry_frame, text="-", bg="red", command=lambda frame=api_entry_frame: remove_api_field(frame))
        button_remove_api.pack(side=LEFT)

        # Append the API entry widgets, remove button, and frame to the respective lists
        api_entries.append((entry_api_name, entry_api_key))
        remove_api_buttons.append(button_remove_api)
        api_frames.append(api_entry_frame)

        # Clear the API entry field
        entry_api.delete(0, END)



# Create the main window
window = Tk()
window.configure(bg="#222222")
window.title("Details")

# Create a frame for "Details"
details_frame = Frame(window, bg="#222222")
details_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)

# Create labels and entry fields for "Name", "Surname", and "Email"
label_name = Label(details_frame, text="Name:", bg="#222222", fg=label_color, anchor=W)
label_name.grid(row=0, column=0, sticky=W, pady=5)
entry_name = Entry(details_frame, bg=entry_bg, fg=label_color)
entry_name.grid(row=0, column=1, sticky=W, pady=5)

label_surname = Label(details_frame, text="Surname:", bg="#222222", fg=label_color, anchor=W)
label_surname.grid(row=1, column=0, sticky=W, pady=5)
entry_surname = Entry(details_frame, bg=entry_bg, fg=label_color)
entry_surname.grid(row=1, column=1, sticky=W, pady=5)

label_email = Label(details_frame, text="Email:", bg="#222222", fg=label_color, anchor=W)
label_email.grid(row=2, column=0, sticky=W, pady=5)
entry_email = Entry(details_frame, bg=entry_bg, fg=label_color)
entry_email.grid(row=2, column=1, sticky=W, pady=5)

# Create a field entry for custom fields
label_custom_fields = Label(details_frame, text="Custom Fields:", bg="#222222", fg=label_color, anchor=W)
label_custom_fields.grid(row=3, column=0, sticky=W, pady=5)

entry_field_name = Entry(details_frame, bg=entry_bg, fg=label_color)
entry_field_name.grid(row=3, column=1, sticky=W, pady=5)

button_add_field = Button(details_frame, text="+", command=add_field, bg=button_bg, fg=button_fg)
button_add_field.grid(row=3, column=2, sticky=W)

# Create a list to store the field entries
field_entries = []

# Create initial field entry
add_field()

# Create a frame for "APIs"
api_frame = Frame(window, bg="#222222")
api_frame.grid(row=0, column=1, rowspan=6, padx=10, pady=10, sticky=N)

# Create title for "APIs"
label_api_title = Label(api_frame, text="APIs", bg="#222222", fg=label_color, font=("Arial", 16, "bold"))
label_api_title.pack(anchor=NW, pady=5)

# Create a frame for "New API's" field
api_entry_frame = Frame(api_frame, bg="#222222")
api_entry_frame.pack(anchor=W, pady=5)

# Create a list to store API entry widgets
apis = []

# Create initial API field entry
entry_api = Entry(api_entry_frame, bg=entry_bg, fg=label_color)
entry_api.pack(side=LEFT)

button_add_api = Button(api_entry_frame, text="+", command=add_api_field, bg=button_bg, fg=button_fg)
button_add_api.pack(side=LEFT)

# Create a frame to hold the buttons
button_frame = Frame(window, bg="#222222")
button_frame.grid(row=5, column=0, columnspan=2, pady=10)
# Create buttons to save and load data
button_save = Button(button_frame, text="Save", bg=button_bg, fg=button_fg, command=save_details)
button_save.grid(row=0, column=0, padx=5, pady=10, sticky=W)

button_load = Button(button_frame, text="Load", bg=button_bg, fg=button_fg, command=load_details)
button_load.grid(row=0, column=1, padx=5, pady=10, sticky=W)


# Start the main event loop
window.mainloop()
