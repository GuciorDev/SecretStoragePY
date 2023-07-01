# SecretStoragePY

**Secret Storage** is a simple desktop application built using Python's Tkinter library that allows you to securely store and manage your sensitive data, such as names, surnames, email addresses, and custom fields. The app provides the ability to save the data to a JSON file and load it back when needed.

## Features

- Secure password protection to access the app.
- Store and manage personal information, including name, surname, email, and custom fields.
- Save data to a JSON file for easy backup and portability.
- Load data from a previously saved JSON file.
- Add and remove custom fields as needed.
- Store and manage API credentials, including API names and corresponding API keys.

## Getting Started

To run the **Secret Storage** app on your local machine, follow these steps:

1. Clone or download this repository to your computer.

2. Make sure you have Python installed on your machine.

3. Install the required dependencies. Open a terminal or command prompt, navigate to the project's directory, and run the following command:

```bash
pip install tk
```

4. Run the app by executing the `secret_storage.py` file:

```bash
python secret_storage.py
```

5. The app will open a validation window asking for a password. The default password is `1234`. You can change this password in the code if needed.

6. Upon entering the correct password, the main window will open, allowing you to store and manage your sensitive data.

## How to Use

1. **Password Validation:**
   - Enter the password in the validation window to access the main app window. If you enter the incorrect password three times, the app will close.

2. **Storing Details:**
   - Enter your name, surname, and email in the respective fields on the left side of the main window.
   - Use the "Custom Fields" section to add any additional information you want to store. Enter the field name and click the "+" button to add the field. The field can be removed by clicking the corresponding "X" button next to it.

3. **Saving Data:**
   - Click the "Save" button at the bottom of the main window to save the entered details, including custom fields, to a JSON file. You will be prompted to choose a location to save the file.

4. **Loading Data:**
   - To load previously saved data, click the "Load" button at the bottom of the main window. Choose the JSON file that contains the data you want to load. The previously saved data will replace the current entries.

5. **APIs:**
   - The right side of the main window allows you to store API credentials.
   - Enter the API name and API key in the provided entry fields and click the "+" button to add the API details. The added APIs can be removed by clicking the corresponding "X" button.

## Contributing

If you would like to contribute to this project, feel free to submit issues, suggestions, or pull requests. Your contributions are highly appreciated.

## License

This project is licensed under the MIT License. You can find the license information in the [LICENSE](LICENSE) file.

## Acknowledgments

The **Secret Storage** app was created as a demonstration and learning exercise, and it is not intended for production use. Special thanks to the Python community and the Tkinter library for providing the necessary tools to create this application.
