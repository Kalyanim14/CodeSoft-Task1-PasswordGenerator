import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    # Get the password length from the user
    try:
        length = int(entry_length.get())
        if length < 1:
            raise ValueError("Password length should be at least 1.")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
        return

    # Get the user-provided words
    words = entry_words.get().strip()
    
    # Ensure the password includes the provided words
    if words:
        if len(words) > length:
            messagebox.showerror("Input Error", "The provided words are longer than the specified length.")
            return
        # Combine the user-provided words with random characters
        password_base = words + random.choice(string.ascii_letters)
    else:
        password_base = ""
    
    # Fill the rest of the password with random characters
    remaining_length = length - len(password_base)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Add at least one lowercase, one uppercase, one number, and one symbol
    password = password_base
    if remaining_length > 3:
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        remaining_length -= 4  # We've added 4 characters already

    # Fill the remaining password length with random characters
    password += ''.join(random.choice(characters) for _ in range(remaining_length))
    
    # Shuffle the password to ensure random placement of user-provided words
    password = ''.join(random.sample(password, len(password)))
    
    # Display the generated password
    result_label.config(text=f"Generated Password: {password}")

    # Check the password strength
    check_password_strength(password)

# Function to check password strength
def check_password_strength(password):
    # Check password length
    if len(password) <= 4:
        strength_label.config(text="Your password is too weak", fg="red")
    elif 5 <= len(password) <= 7:
        strength_label.config(text="Weak", fg="orange")
    elif len(password) >= 8:
        strength_label.config(text="Perfect", fg="green")

# Set up the main GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")  # Set the window size

# Heading
heading = tk.Label(root, text="Password Generator", font=("Helvetica", 16))
heading.pack(pady=10)

# Input for password length
length_label = tk.Label(root, text="Password Length:", font=("Arial", 12))
length_label.pack(pady=5)
entry_length = tk.Entry(root, font=("Arial", 14), width=20)
entry_length.pack(pady=5)

# Input for interested words
words_label = tk.Label(root, text="Interested Words (Optional):", font=("Arial", 12))
words_label.pack(pady=5)
entry_words = tk.Entry(root, font=("Arial", 14), width=30)
entry_words.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=15)

# Label to display the generated password
result_label = tk.Label(root, text="Generated Password: ", font=("Arial", 12), fg="blue")
result_label.pack(pady=10)

# Label to display the password strength
strength_label = tk.Label(root, text="", font=("Arial", 12))
strength_label.pack(pady=5)

# Run the application
root.mainloop()
