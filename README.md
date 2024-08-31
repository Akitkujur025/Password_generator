# Password Generator

This is a simple Password Generator application built with Python using the `tkinter` library for the graphical user interface (GUI) and `ttkbootstrap` for modern theming. The application allows users to generate random passwords with customizable length, including options to include numbers and special characters.

## Features

- **Customizable Password Length:** Users can specify the minimum length of the generated password.
- **Include Numbers:** Option to include numeric digits in the password.
- **Include Special Characters:** Option to include special characters (e.g., `!@#$%^&*`) in the password.
- **Modern UI:** The application uses `ttkbootstrap` for a clean and modern interface.

## Requirements

- Python 3.x
- `ttkbootstrap` (Install via pip)

## Usage

1. Launch the application by running the `password_generator.py` script.
2. Enter the desired password length in the input field.
3. Check the boxes if you want to include numbers and/or special characters in the password.
4. Click the "Generate" button.
5. The generated password will be displayed on the screen.

## Files

- `password_generator.py`: The main script containing the GUI and password generation logic.
- `padlock_1.png`: An icon file for the application window.

## Customization

You can customize the appearance of the application by changing the theme. The available themes can be found in the `ttkbootstrap` documentation. To change the theme, modify the `themename` parameter in the `ttk.Window()` function.

Example:
```python
window = ttk.Window(themename='solar')
