
# Phone-generator
This script can be used to generate SIP devices for Cisco IOS XE router.
This script has GUI for better usage.

   You need a CSV file containing the following columns:<br />
            * phone_number<br />
            * display_name<br />
            * mac_address<br />
            * phone_type<br /><br />
      example file is included in library.

# Usage
## GUI
Simple GUI, where you can browse for the path to a CSV file and enter the conf file name. The script adds the .cfg extension to the file and saves it to C:\Users&lt;username>\Documents\Python\Scripts.

If there is no folder called Python, the program creates the path to scripts.

![image](https://github.com/CodeWhisperer69/Cisco-collab/assets/150474858/b3715b62-ef2a-431d-a6a5-56d95d9095d8)

## No GUI
Functionality is same as GUI version. 

![image](https://github.com/CodeWhisperer69/Cisco-collab/assets/150474858/a9a335e6-4788-4f56-a0e0-42cdd71cdd90)

## executable
Is .exe from GUI version.
