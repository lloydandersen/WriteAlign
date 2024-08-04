import tkinter as tk
from tkinter import ttk
from docx import Document

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

file_name_var = tk.StringVar()


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


# Template Frames
simple_essay_frame = tk.Frame(root)

label_font = ("Times New Roman", 16)
entry_font = ("Times New Roman", 12)


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

def test_variables(*args):
    essay_name_var.set("The Amazon Rainforest")
    thesis_var.set("The Amazon Rainforest is important to humankind.")
    topic_sentence_1_var.set("The Amazon Rainforest is important for climate stability.")
    topic_sentence_2_var.set("The Amazon Rainforest provides a home for a diverse species.")
    topic_sentence_3_var.set("The Amazon Rainforest is beautiful and important for human wellbeing.")
    var_1.set("The Amazon Rainforest stores 2 billion metric tons of carbon annually.")
    var_2.set("The Amazon stores 200 billion metric tons of carbon in total.")
    var_3.set("The Amazon Rainforest has over ten of thousands of plant, animal and fungi species.")
    var_4.set("The Amazon has many unknown species and potential for new foods, medicines and products.")
    var_5.set("The Amazon Rainforest is home to over 30 million people.")
    var_6.set("The Amazon Rainforest is visited by one million people each year due to its beauty.")
    summary_var.set("The Amazon Rainforest is important for humankind and the entire planet.")


def generate_simple_essay_prompt():
    file = open(f"{file_name_var.get()}.txt", "w")
    file.write(f"""Write me a five-paragraph essay.
The essay shall be constructed with an introduction paragraph, three body paragraphs and a concluding paragraph.

The title of the paper is {essay_name_var.get()}.

The thesis of the paper is {thesis_var.get()}.

The introduction paragraph shall utilize the body paragraphs for a coherent essay.
 
The body paragraphs should be written as follows:

The first body paragraph's topic sentence is "{topic_sentence_1_var.get()}"
It will have two supporting ideas as follows: 
1. {var_1.get()}
2. {var_2.get()}

The second body paragraph's topic sentence is "{topic_sentence_2_var.get()}"
It will have two supporting ideas as follows: 
1. {var_3.get()}
2. {var_4.get()}

The third body paragraph's topic sentence is "{topic_sentence_3_var.get()}"
It will have two supporting ideas as follows: 
1. {var_5.get()}
2. {var_6.get()}

The concluding paragraph shall summarize the body paragraphs.
The concluding paragraph shall emphasize the following statement: {summary_var.get()}
    """)
    file.close()


def generate_simple_essay_outline():
    document = Document()
    document.add_heading(f"{essay_name_var.get()}", 0)

    document.add_heading("Introduction", level=1)
    document.add_heading(f"-{thesis_var.get()}", level=2)

    document.add_heading("Body Paragraph 1", level=1)
    document.add_heading(f"-{topic_sentence_1_var.get()}", level=2)
    document.add_paragraph(f"-{var_1.get()}")
    document.add_paragraph(f"-{var_2.get()}")

    document.add_heading("Body Paragraph 2", level=1)
    document.add_heading(f"-{topic_sentence_2_var.get()}", level=2)
    document.add_paragraph(f"-{var_3.get()}")
    document.add_paragraph(f"-{var_4.get()}")

    document.add_heading("Body Paragraph 3", level=1)
    document.add_heading(f"-{topic_sentence_3_var.get()}", level=2)
    document.add_paragraph(f"-{var_5.get()}")
    document.add_paragraph(f"-{var_6.get()}")

    document.add_heading("Conclusion", level=1)
    document.add_heading(f"-{summary_var.get()}", level=2)


    document.save(f"{file_name_var.get()}.docx")



def simple_essay_prompt():
    top = tk.Toplevel(background="white")

    file_name_label = tk.Label(top, text="File Name", background="white")
    file_name_label.grid(row=0, column=0)

    file_name_entry = tk.Entry(top, textvariable=file_name_var)
    file_name_entry.grid(row=0, column=1)

    file_type_label = tk.Label(top, text=".txt", background="white")
    file_type_label.grid(row=0, column=2)

    create_button = tk.Button(top, text="Create", background="white", command=generate_simple_essay_prompt)
    create_button.grid(row=1, column=0, columnspan=3, sticky="swen")


def simple_essay_outline():
    top = tk.Toplevel(background="white")

    file_name_label = tk.Label(top, text="File Name", background="white")
    file_name_label.grid(row=0, column=0)

    file_name_entry = tk.Entry(top, textvariable=file_name_var)
    file_name_entry.grid(row=0, column=1)

    file_type_label = tk.Label(top, text=".docx", background="white")
    file_type_label.grid(row=0, column=2)

    create_button = tk.Button(top, text="Create", background="white", command=generate_simple_essay_outline)
    create_button.grid(row=1, column=0, columnspan=3, sticky="swen")



def back_to_home():
    for child in root.winfo_children():
        child.pack_forget()
    main_page.pack(fill="both", side="top", padx=150, pady=150)


def simple_essay():
    simple_essay_frame = tk.Frame(root, background="white")
    simple_essay_frame.pack(side="top", pady=(10, 10), padx=10)
    simple_essay_frame.columnconfigure((0, 1), weight=1)

    back_button = tk.Button(simple_essay_frame, text="back", background="black", foreground="white", command=back_to_home)
    back_button.grid(row=0, column=0)

    simple_essay_title = tk.Label(simple_essay_frame, text="Simple Essay", background="white", foreground="black", font=("Times New Roman", 30, "bold"))
    simple_essay_title.grid(row=1, column=1, columnspan=2, pady=(0, 30))


    simple_essay_name_label = tk.Label(simple_essay_frame, text="Essay Name", background="white", foreground="black", font=label_font)
    simple_essay_name_label.grid(row=2, column=1, pady=(0, 5), padx=(0, 5))

    simple_essay_name_entry = tk.Entry(simple_essay_frame, textvariable=essay_name_var,  relief="solid", font=entry_font)
    simple_essay_name_entry.grid(row=2, column=2, ipadx=80)

    simple_essay_thesis_label = tk.Label(simple_essay_frame, text="Thesis", background="white", foreground="black", font=label_font)
    simple_essay_thesis_label.grid(row=3, column=1, pady=(0, 5))

    simple_essay_thesis_entry = tk.Entry(simple_essay_frame, textvariable=thesis_var, relief="solid", font=entry_font)
    simple_essay_thesis_entry.grid(row=3, column=2, ipadx=80)

    topic_1_label = tk.Label(simple_essay_frame, text="Topic 1", background="white", foreground="black", font=label_font)
    topic_1_label.grid(row=4, column=1, pady=(0, 5))

    topic_1_entry = tk.Entry(simple_essay_frame, textvariable=topic_sentence_1_var, relief="solid", font=entry_font)
    topic_1_entry.grid(row=4, column=2, ipadx=80)

    support_1_label = tk.Label(simple_essay_frame, text="Support 1", background="white", foreground="black", font=label_font)
    support_1_label.grid(row=5, column=1, pady=(0, 5))

    support_1_entry = tk.Entry(simple_essay_frame, textvariable=var_1, relief="solid", font=entry_font)
    support_1_entry.grid(row=5, column=2, ipadx=80)

    support_2_label = tk.Label(simple_essay_frame, text="Support 2", background="white", foreground="black", font=label_font)
    support_2_label.grid(row=6, column=1, pady=(0, 5))

    support_2_entry = tk.Entry(simple_essay_frame, textvariable=var_2, relief="solid", font=entry_font)
    support_2_entry.grid(row=6, column=2, ipadx=80)

    topic_2_label = tk.Label(simple_essay_frame, text="Topic 2", background="white", foreground="black", font=label_font)
    topic_2_label.grid(row=7, column=1, pady=(0, 5))

    topic_2_entry = tk.Entry(simple_essay_frame, textvariable=topic_sentence_2_var, relief="solid", font=entry_font)
    topic_2_entry.grid(row=7, column=2, ipadx=80)

    support_3_label = tk.Label(simple_essay_frame, text="Support 1", background="white", foreground="black", font=label_font)
    support_3_label.grid(row=8, column=1, pady=(0, 5))

    support_3_entry = tk.Entry(simple_essay_frame, textvariable=var_3, relief="solid", font=entry_font)
    support_3_entry.grid(row=8, column=2, ipadx=80)

    support_4_label = tk.Label(simple_essay_frame, text="Support 2", background="white", foreground="black", font=label_font)
    support_4_label.grid(row=9, column=1, pady=(0, 5))

    support_4_entry = tk.Entry(simple_essay_frame, textvariable=var_4, relief="solid", font=entry_font)
    support_4_entry.grid(row=9, column=2, ipadx=80)

    topic_3_label = tk.Label(simple_essay_frame, text="Topic 3", background="white", foreground="black", font=label_font)
    topic_3_label.grid(row=10, column=1, pady=(0, 5))

    topic_3_entry = tk.Entry(simple_essay_frame, textvariable=topic_sentence_3_var, relief="solid", font=entry_font)
    topic_3_entry.grid(row=10, column=2, ipadx=80)

    support_5_label = tk.Label(simple_essay_frame, text="Support 1", background="white", foreground="black", font=label_font)
    support_5_label.grid(row=11, column=1, pady=(0, 5))

    support_5_entry = tk.Entry(simple_essay_frame, textvariable=var_5, relief="solid", font=entry_font)
    support_5_entry.grid(row=11, column=2, ipadx=80)

    support_6_label = tk.Label(simple_essay_frame, text="Support 2", background="white", foreground="black", font=label_font)
    support_6_label.grid(row=12, column=1, pady=(0, 5))

    support_6_entry = tk.Entry(simple_essay_frame, textvariable=var_6, relief="solid", font=entry_font)
    support_6_entry.grid(row=12, column=2, ipadx=80)


    finish_frame = tk.Frame(simple_essay_frame, background="white")
    finish_frame.grid(row=13, column=1, columnspan=2)

    prompt_generation_button = tk.Button(finish_frame, text="Prompt", background="white", foreground="black", command=simple_essay_prompt)
    prompt_generation_button.grid(row=0, column=0, ipadx=20, ipady=10)

    outline_generation_button = tk.Button(finish_frame, text="Outline", background="white", foreground="black", command=simple_essay_outline)
    outline_generation_button.grid(row=0, column=1, ipadx=20, ipady=10)

    clear_button = tk.Button(finish_frame, text="Clear", background="black", foreground="white")
    clear_button.grid(row=1, column=0, columnspan=2, sticky="swen")
    clear_button.bind("<Double-Button-1>", reset_variables)
    clear_button.bind("<Button-3>", test_variables)





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
    