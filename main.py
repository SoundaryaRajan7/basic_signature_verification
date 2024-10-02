import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
import cv2
from numpy import result_type
from signature import match


# Mach Threshold
THRESHOLD = 80


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  # add this





def checkSimilarity(window, path1, path2):
    result = match(path1=path1, path2=path2)
    if(result <= THRESHOLD):
        messagebox.showerror("Failure: Signatures Do Not Match",
                             "Signatures are "+str(result)+f" % similar!!")
        pass
    else:
        messagebox.showinfo("Success: Signatures Match",
                            "Signatures are "+str(result)+f" % similar!!")
    return True


root = tk.Tk()
root.title("Signature Matching")
root.geometry("500x500")  # 300x200
root.configure(bg="#EDBB99")
uname_label = tk.Label(root, text="Compare Two Signatures:", font=10,bg= '#FAE5D3')
uname_label.place(x=90, y=50)

img1_message = tk.Label(root, text="Signature 1",bg="#FAE5D3",font=10)
img1_message.place(x=10, y=120)

image1_path_entry = tk.Entry(root, font=10)
image1_path_entry.place(x=150, y=120)

img1_browse_button = tk.Button(
    root, text="Browse", font=10,bg='#D1F2EB', command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=370, y=110)

image2_path_entry = tk.Entry(root, font=10)
image2_path_entry.place(x=150, y=240)

img2_message = tk.Label(root, text="Signature 2",bg="#FAE5D3",font=10)
img2_message.place(x=10, y=240)


img2_browse_button = tk.Button(
    root, text="Browse", font=10,bg='#D1F2EB', command=lambda: browsefunc(ent=image2_path_entry))
img2_browse_button.place(x=370, y=235)

compare_button = tk.Button(
    root, text="Compare", font=10,fg='white',bg='#BA4A00', command=lambda: checkSimilarity(window=root,
                                                                   path1=image1_path_entry.get(),
                                                                   path2=image2_path_entry.get(),))

compare_button.place(x=200, y=320)
root.mainloop()
