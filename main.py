#!/usr/bin/env python3
import pypdf as pdf
import tkinter.filedialog
import tkinter.messagebox
import sys


from convert import convert_pdf

# read arguments
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    from file_chooser import choose_file
    file_name = choose_file()
    
if not file_name:
    print("no file selected")
    exit()

if not convert_pdf(file_name):
    exit()

print("done")

# show notification
# friendly_name = file_name.split("\\")[-1]
# tkinter.messagebox.showinfo("Done", f"Done rescaling PDF {friendly_name}")