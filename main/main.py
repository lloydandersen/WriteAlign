import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("WriteAlign")
root.configure(background="white")
root.minsize(700, 500)

main_page = tk.Frame(root, background="white")
main_page.pack(side="top", fill='both', padx=150, pady=150)
main_page.columnconfigure(0, weight=1)
write_align_title = tk.Label(main_page, text="WriteAlign", font=("Times New Roman", 50, "bold"), background="white")
write_align_title.grid(row=0, column=0, pady=(0, 30))
template_var = tk.StringVar()
template_list = ["Simple Essay"]
select_template = ttk.Combobox(main_page, textvariable=template_var, values=template_list, state="readonly", font=("Times New Roman", 16), justify="center")
select_template.grid(row=1, column=0)

select_button = tk.Button(main_page, text="Write", background="white", foreground="black", font=("Times New Roman", 16), borderwidth=2)
select_button.grid(row=2, column=0, pady=(10, 0), ipadx=50)

root.mainloop()
    