#OPen foiel and then edit the file and save again
# we want to inject a string in the file and then save the file
# inject the string at a certain point in the file
""" Deception code we want to inject:

# transform table for the sensitive information
    sensitive_info = {
        "username": "skdhdkf",
        "password": "fhjruews",
        "email": "fjdfhfd",
        "phone": "dfhvxb",
        "address": "dfhjdf",
        "name": "dfhjdf",
        "id": "dfhjdf",
        "card": "dfhjdf",
        "number": "dfhjdf",
        "account": "dfhjdf",
        "bank": "dfhjdf",
        "cvv": "dfhjdf",
        "pin": "dfhjdf",
        "code": "dfhjdf"
    }  
    # Mask sensitive information
    def mask_sensitive_info(filename):
        with open(filename, "r+") as f:
            text = f.read()
            for key, value in sensitive_info.items():
                text = re.sub(key, value, text)
            f.seek(0)
            f.write(text)
            f.truncate()
    mask_sensitive_info(filename)
 """
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

# Root window settings
root = tk.Tk()
root.title('Deception Injector')
root.resizable(False, False)
root.geometry('550x250')

# Text editor
text = tk.Text(root, width=40, height=10)
text.grid(column=0, row=0, padx=10, pady=10)

# Open file
def open_file():
    file = fd.askopenfilename(
        initialdir='C:/', # This is the directory where the file is located
        title='Select a file',
        filetypes=(('Text files', '*.py*'), ('all files', '*.*'))
    )
    if file:
        with open(file, 'r') as f:
            text.insert(1.0, f.read())

# Save file
def save_file():
    file = fd.asksaveasfilename(
        initialdir='C:/', # This is the directory where the file is located
        title='Select a file',
        filetypes=(('Text files', '*.py*'), ('all files', '*.*'))
    )
    if file:
        with open(file, 'w') as f:
            f.write(text.get(1.0, tk.END))

# Inject function
def inject():
    text.insert(28.0, '# transform table for the sensitive information\n')
    text.insert(29.0, '    sensitive_info = {\n')
    text.insert(30.0, '        "username": "skdhdkf",\n')
    text.insert(31.0, '        "password": "fhjruews",\n')
    text.insert(32.0, '        "email": "fjdfhfd",\n')
    text.insert(33.0, '        "phone": "dfhvxb",\n')
    text.insert(34.0, '    }  \n')
    text.insert(35.0, '    # Mask sensitive information\n')
    text.insert(36.0, '    def mask_sensitive_info(filename):\n')
    text.insert(37.0, '        with open(filename, "r+") as f:\n')
    text.insert(38.0, '            text = f.read()\n')
    text.insert(39.0, '            for key, value in sensitive_info.items():\n')
    text.insert(40.0, '                text = re.sub(key, value, text)\n')
    text.insert(41.0, '            f.seek(0)\n')
    text.insert(42.0, '            f.write(text)\n')
    text.insert(43.0, '            f.truncate()\n')
  # lookup in txt the line conatining "    def onPress(key):" and insert the code after that line
    start_index = text.search("onPress(key):", "1.0", stopindex=tk.END)
    if start_index:
        text.insert(start_index+"+13c\n", "\n        mask_sensitive_info(filename)\n")
# Buttons
open_button = ttk.Button(root, text='Open', command=open_file)
open_button.grid(column=0, row=1, padx=10, pady=10)

save_button = ttk.Button(root, text='Save', command=save_file)
save_button.grid(column=1, row=1, padx=10, pady=10)

inject_button = ttk.Button(root, text='Inject', command=inject)
inject_button.grid(column=2, row=1, padx=10, pady=10)

root.mainloop()



""" The challenge of creating a tool to handle the injection of any arbitrary keylogger programmed in python with a payload that will change the behavior of the keylogger would be to ensure that the tool is able to adapt to the specific variables and functions used in each keylogger. This would require the tool to have the ability to recognize and parse the relevant information from the keylogger code, as well as the ability to modify the behavior of the keylogger based on the desired payload. Additionally, the tool would need to be able to handle any errors or exceptions that may arise during the injection process, ensuring that it can handle keyloggers of any complexity or structure. Overall, the challenge would be to create a flexible and adaptable tool that can handle the wide range of keyloggers that may be encountered in practice. """
""" Finally, there may be challenges in naming variables and functions in a way that is both descriptive and intuitive, as well as in keeping track of the various components of the tool and payload as they are developed and integrated. Overall, creating a tool to handle the injection of an arbitrary keylogger with a payload that changes its behavior would require a strong understanding of python programming and a strong attention to detail in order to ensure that the tool and payload function correctly and effectively. """
""" One possible solution to this challenge would be to create a generic injection tool that is able to handle any keylogger, regardless of its specific implementation. This tool would need to be able to identify the keylogger's code and extract the relevant information, such as the names of variables and functions, in order to properly inject the payload.
To do this, the tool could use techniques such as code analysis or reflection to extract the necessary information. It could also use a database or configuration file to store the names of variables and functions for each keylogger, allowing it to easily adapt to different implementations. """


""" 
To design a tool in Python to patch a Python program, you can follow these steps:

Define the purpose and scope of the tool: Clearly define the purpose of the tool and the specific changes or additions that it should be able to make to a Python program.

Write the patch instructions: Create a set of patch instructions that can be applied to the source code of a Python program to make the desired changes or additions. These instructions should be written in a format that can be easily parsed and applied by the tool.

Design the user interface: Decide on the user interface for the tool, including how users will input the patch instructions and the source code of the program, and how the tool will output the patched program.

Write the code for the tool: Write the code for the tool using Python, including functions to parse and apply the patch instructions, handle user input and output, and any other necessary functionality.

Test the tool: Thoroughly test the tool to ensure that it is functioning as expected and that it is able to correctly apply the patch instructions to the source code of a Python program.

Document the tool: Create detailed documentation for the tool, including instructions on how to use it and any known limitations or issues.

Release the tool: Once the tool is fully tested and documented, release it for others to use.
"""



