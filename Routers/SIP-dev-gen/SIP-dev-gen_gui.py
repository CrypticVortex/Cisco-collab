"""
This script can be used to generate SIP devices for Cisco IOS XE router.
This script has GUI for better usage.

    Args:
        data: A CSV file containing the following columns:
            * Phone Number
            * Display Name
            * MAC Address
            * Phone Type
        example file included in library


    """

import os
import tkinter as tk
from tkinter import filedialog
import csv


def generate_router_config(data):
    row_number = 2
    cm_conf = ""

    with open(data, "r") as i:
        reader = csv.reader(i)
        next(reader)

        for row in reader:
            if row_number != 1:
                cm_conf += f"""\
voice register dn {row_number - 1}
  number {row[0]}
  name {row[1]}
  call-forward b2bua busy 2000
  call-forward b2bua noan 2000 timeout 20
!
voice register pool {row_number - 1}
  id mac {row[2]}
  type {row[3]}
  number 1 dn {row[0]}
!
"""

            row_number += 1

    return cm_conf


def run_script(csv_file, config_filename):
    user_documents_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')
    scripts_folder_path = os.path.join(user_documents_folder, 'Python', 'Scripts')

    try:
        os.makedirs(scripts_folder_path, exist_ok=True)
    except Exception as e:
        error_message = "Error creating scripts folder: {}".format(e)
        print(error_message)
        return error_message

    router_config = generate_router_config(csv_file)

    if not config_filename:
        return "Error: Config file name cannot be empty"
    # adds .cfg extension if not present
    if not config_filename.endswith(".cfg"):
        config_filename += '.cfg'

    config_filepath = os.path.join(scripts_folder_path, config_filename)

    try:
        os.makedirs(os.path.dirname(config_filepath), exist_ok=True)
        with open(config_filepath, "w") as f:
            f.write(router_config)
        result_message = "Router configuration saved to {}".format(os.path.normpath(config_filepath))
        print(result_message)
        return result_message
    except Exception as e:
        error_message = "Error writing configuration file: {}".format(e)
        print(error_message)
        return error_message


def browse_file(entry_var):
    file_path = filedialog.askopenfilename()
    entry_var.delete(0, tk.END)
    entry_var.insert(0, file_path)


def execute_script():
    csv_file = csv_entry.get()
    config_filename = config_entry.get()
    result_text.set(run_script(csv_file, config_filename))


# Create the main window
window = tk.Tk()
window.title("Configuration Generator")

# Create and place widgets
csv_label = tk.Label(window, text="CSV File:")
csv_label.grid(row=0, column=0, pady=10)

csv_entry = tk.Entry(window, width=50)
csv_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(window, text="Browse", command=lambda: browse_file(csv_entry))
browse_button.grid(row=0, column=2, pady=10)

config_label = tk.Label(window, text="Config File Name:")
config_label.grid(row=1, column=0, pady=10)

config_entry = tk.Entry(window, width=50)
config_entry.grid(row=1, column=1, padx=10, pady=10)

execute_button = tk.Button(window, text="Generate", command=execute_script)
execute_button.grid(row=2, column=0, columnspan=3, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
window.mainloop()
