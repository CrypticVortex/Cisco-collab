"""

In Cisco IOS XE router, which working as SIP gateway or similar.
This script creates SIP devices with extensions from CSV file
There's no GUI for this script, so you need to enter the path to the CSV file and the name of the config file.

    Args:
        data: A CSV file containing the following columns:
            * Phone Number
            * Display Name
            * MAC Address
            * Phone Type
        example file included in library


    """

import csv
import os


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


if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")
    config_filename = input("Enter config file name: ")
    # Get the user's Documents folder path
    user_documents_folder = os.path.join(os.environ['USERPROFILE'], 'Documents')

    # Create the Scripts folder if it doesn't exist
    scripts_folder_path = os.path.join(user_documents_folder, 'Python', 'Scripts')
    if not os.path.exists(scripts_folder_path):
        try:
            os.makedirs(scripts_folder_path)
        except Exception as e:
            print("Error creating scripts folder:", e)
            exit(1)

    # Adds .cfg extension if it's not present
    if not config_filename.endswith(".cfg"):
        config_filename += '.cfg'

    # Generate the router configuration
    router_config = generate_router_config(csv_file)

    # Save the router configuration to the user's Documents\Python\Scripts folder
    config_filepath = os.path.join(scripts_folder_path, config_filename)
    with open(config_filepath, "w") as f:
        f.write(router_config)
