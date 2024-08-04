import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("WriteAlign")
root.configure(background="white")
root.minsize(700, 500)
essay_name_var = tk.StringVar()
thesis_var = tk.StringVar()
topic_sentence_1_var = tk.StringVar()
topic_sentence_2_var = tk.StringVar()
topic_sentence_3_var = tk.StringVar()
var_1 = tk.StringVar()
var_2 = tk.StringVar()
var_3 = tk.StringVar()
var_4 = tk.StringVar()
var_5 = tk.StringVar()
var_6 = tk.StringVar()
summary_var = tk.StringVar()


main_page = tk.Frame(root, background="white")
main_page.pack(side="top", fill='both', padx=150, pady=150)
main_page.columnconfigure(0, weight=1)
write_align_title = tk.Label(main_page, text="WriteAlign", font=("Times New Roman", 50, "bold"), background="white")
write_align_title.grid(row=0, column=0, pady=(0, 30))
template_var = tk.StringVar()
template_list = ["Simple Essay"]
select_template = ttk.Combobox(main_page, textvariable=template_var, values=template_list, state="readonly", font=("Times New Roman", 16), justify="center")
select_template.grid(row=1, column=0)
template_var.set(template_list[0])
finish_frame = tk.Frame()


# Templtae Frames
simple_essay_frame = tk.Frame(root)


def reset_variables(*args):
    essay_name_var.set("")
    thesis_var.set("")
    topic_sentence_1_var.set("")
    topic_sentence_2_var.set("")
    topic_sentence_3_var.set("")
    var_1.set("")
    var_2.set("")
    var_3.set("")
    var_4.set("")
    var_5.set("")
    var_6.set("")
    summary_var.set("")


def back_to_home():
    for child in root.winfo_children():
        child.pack_forget()
    main_page.pack(fill="both", side="top", padx=150, pady=150)


def simple_essay():
    simple_essay_frame = tk.Frame(root, background="white")
    simple_essay_frame.pack(side="top", pady=(100, 0), padx=10)
    simple_essay_frame.columnconfigure((0, 1), weight=1)

    back_button = tk.Button(simple_essay_frame, text="back", background="black", foreground="white", command=back_to_home)
    back_button.grid(row=0, column=0)

    simple_essay_title = tk.Label(simple_essay_frame, text="Simple Essay", background="white", foreground="black")
    simple_essay_title.grid(row=1, column=1, columnspan=2)


    simple_essay_name_label = tk.Label(simple_essay_frame, text="Essay Name", background="white", foreground="black")
    simple_essay_name_label.grid(row=2, column=1)

    simple_essay_name_entry = tk.Entry(simple_essay_frame, textvariable=essay_name_var)
    simple_essay_name_entry.grid(row=2, column=2, ipadx=80)

    simple_essay_thesis_label = tk.Label(simple_essay_frame, text="Thesis", background="white", foreground="black")
    simple_essay_thesis_label.grid(row=3, column=1)

    simple_essay_thesis_entry = tk.Entry(simple_essay_frame, textvariable=thesis_var)
    simple_essay_thesis_entry.grid(row=3, column=2, ipadx=80)

    topic_1_label = tk.Label(simple_essay_frame, text="Topic 1", background="white", foreground="black")
    topic_1_label.grid(row=4, column=1)

    topic_1_entry = tk.Entry(simple_essay_frame, textvariable=topic_sentence_1_var)
    topic_1_entry.grid(row=4, column=2, ipadx=80)

    support_1_label = tk.Label(simple_essay_frame, text="Support 1", background="white", foreground="black")
    support_1_label.grid(row=5, column=1)

    support_1_entry = tk.Entry(simple_essay_frame, textvariable=var_1)
    support_1_entry.grid(row=5, column=2, ipadx=80)

    support_2_label = tk.Label(simple_essay_frame, text="Support 2", background="white", foreground="black")
    support_2_label.grid(row=6, column=1)

    support_2_entry = tk.Entry(simple_essay_frame, textvariable=var_2)
    support_2_entry.grid(row=6, column=2, ipadx=80)

    topic_2_label = tk.Label(simple_essay_frame, text="Topic 2", background="white", foreground="black")
    topic_2_label.grid(row=7, column=1)

    topic_2_entry = tk.Entry(simple_essay_frame, textvariable=topic_sentence_2_var)
    topic_2_entry.grid(row=7, column=2, ipadx=80)

    support_3_label = tk.Label(simple_essay_frame, text="Support 1", background="white", foreground="black")
    support_3_label.grid(row=8, column=1)

    support_3_entry = tk.Entry(simple_essay_frame, textvariable=var_3)
    support_3_entry.grid(row=8, column=2, ipadx=80)

    support_4_label = tk.Label(simple_essay_frame, text="Support 2", background="white", foreground="black")
    support_4_label.grid(row=9, column=1)

    support_4_entry = tk.Entry(simple_essay_frame, textvariable=var_4)
    support_4_entry.grid(row=9, column=2, ipadx=80)

    topic_3_label = tk.Label(simple_essay_frame, text="Topic 3", background="white", foreground="black")
    topic_3_label.grid(row=10, column=1)

    topic_3_entry = tk.Entry(simple_essay_frame, textvariable=topic_sentence_3_var)
    topic_3_entry.grid(row=10, column=2, ipadx=80)

    support_5_label = tk.Label(simple_essay_frame, text="Support 1", background="white", foreground="black")
    support_5_label.grid(row=11, column=1)

    support_5_entry = tk.Entry(simple_essay_frame, textvariable=var_5)
    support_5_entry.grid(row=11, column=2, ipadx=80)

    support_6_label = tk.Label(simple_essay_frame, text="Support 2", background="white", foreground="black")
    support_6_label.grid(row=12, column=1)

    support_6_entry = tk.Entry(simple_essay_frame, textvariable=var_6)
    support_6_entry.grid(row=12, column=2, ipadx=80)







    finish_frame = tk.Frame(simple_essay_frame, background="white")
    finish_frame.grid(row=13, column=1, columnspan=2)

    prompt_generation_button = tk.Button(finish_frame, text="Prompt", background="white", foreground="black")
    prompt_generation_button.grid(row=0, column=0)

    outline_generation_button = tk.Button(finish_frame, text="Outline", background="white", foreground="black")
    outline_generation_button.grid(row=0, column=1)

    clear_button = tk.Button(finish_frame, text="Clear", background="black", foreground="white")
    clear_button.grid(row=1, column=0, columnspan=2, sticky="swen")
    clear_button.bind("<Double-Button-1>", reset_variables)





def make_selection():
    name = template_var.get()
    main_page.pack_forget()
    if name == "Simple Essay":
        simple_essay()

    else:
        main_page.pack(side="top", fill="both")


select_button = tk.Button(main_page, text="Write", background="white", foreground="black", font=("Times New Roman", 16), borderwidth=2, command=make_selection)
select_button.grid(row=2, column=0, pady=(10, 0), ipadx=50)

select_template.bind("<<ComboboxSelected>>",lambda e: main_page.focus())

root.mainloop()
    