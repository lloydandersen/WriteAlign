from docx import Document


# text functions
def page_title():
    title = input("What shall we call the paper? ")
    return title

def author_name(tog):
    if type(tog) == type("str"):
        name = input("What is the author's Name? ")
    elif type(tog) == type(5):
        name = input(f"What is the author's {tog}'s Name? ")
    else:
        name = "Error. Wrong Type!"
    return name


def author_names():
    # edit: Add input try/except Block.
    num_authors = int(input("How many authors are there? "))

    name_list = list()
    count = 0
    
    while num_authors > 0:
        count += 1
        name = author_name(count)
        name_list.append(name)

        num_authors -= 1

    
    return name_list

def section(tog):
    if type(tog) == type("str"):
        section_name = input("What shall we call this section")
    elif type(tog) == type(5):
        section_name = input(f"What shall we call section {tog} ")
    else:
        section_name = "Error. Must be an integer."

    return section_name


def sections():
    # edit: add try/except block
    num_sections = int(input("How many sections do you want? "))
    if type(num_sections) == type(5):
        pass
    else:
        return "error. Must be an interger"
    section_list = list()
    count = 0

    while num_sections > 0:
        count += 1
        section_name = section(count)
        section_list.append(section_name)
        num_sections -= 1

    return section_list


def add_note():
    note = input("note: ")
    return note


print(sections())