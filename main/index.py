import os
from tkinter import *
from tkinter import ttk

from main.templates.PY.controller import controllerCheckCMD
from main.templates.PY.model import modelsCheckCMD
from main.templates.PY.policy import policiesCheckCMD

root = Tk()
root.geometry("500x800")
root.title("Abdulkadir LEVENT Laravel Module Generator")
frame = Frame(root, borderwidth=4)
frame.pack(fill=BOTH, expand=1)

model_check_val = BooleanVar()
model_check_val.set(False)
resource_check_val = BooleanVar()
resource_check_val.set(False)
request_check_val = BooleanVar()
request_check_val.set(False)
policies_check_val = BooleanVar()
policies_check_val.set(False)
controller_check_val = BooleanVar()
controller_check_val.set(False)
migrate_check_val = BooleanVar()
migrate_check_val.set(False)


def createTabCMD():
    print('createTabCMD')
    deletetab()
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6 = ttk.Frame(tabControl)

    if model_check_val.get():
        add_tab('Models')
    else:
        tab1.forget()
    if resource_check_val.get():
        add_tab('Resources')
    else:
        tab2.forget()
    if request_check_val.get():
        add_tab('Request')
    else:
        tab3.forget()
    if policies_check_val.get():
        add_tab('Policies')
    else:
        tab4.forget()
    if controller_check_val.get():
        add_tab('Controller')
    else:
        tab5.forget()
    if migrate_check_val.get():
        add_tab('Migrate')
    else:
        tab6.forget()
    tabControl.pack(expand=1, fill="both")


def add_tab(tab_name):
    # Eğer aynı isimde bir tab varsa sil
    tabs = tabControl.tabs()
    for tab in tabs:
        if tabControl.tab(tab, option="text") == tab_name:
            tabControl.forget(tab)

    # Yeni bir tab ekle
    tab = ttk.Frame(tabControl)
    tabControl.add(tab, text=tab_name)


def deletetab():
    for item in tabControl.winfo_children():
        if str(item) == (tabControl.select()):
            item.destroy()
            return


def remove_folder(folder_name):
    if os.path.exists(folder_name):
        for file in os.listdir(folder_name):
            os.remove(os.path.join(folder_name, file))
        os.rmdir(folder_name)
        print(f'Removed {folder_name} directory')
    else:
        print(f'{folder_name} directory does not exist')


tabControl = ttk.Notebook(root)

modul_name = Label(frame, text="Modul adı", font=18)
modul_name.place(x=10, y=10)

modul_name_var = StringVar()
modul_name_input = Entry(frame, textvariable=modul_name_var, font=10, width=30)
modul_name_input.place(x=120, y=10)
modul_name_var.set("Cari")

model = Label(frame, text="Model", font=18)
model.place(x=10, y=40)
model_check = Checkbutton(frame,
                          text='Model dosyası oluştur',
                          variable=model_check_val,
                          command=createTabCMD,
                          onvalue=True,
                          offvalue=False)
model_check.place(x=120, y=40)

resource = Label(frame, text="Resource", font=18)
resource.place(x=10, y=80)
resource_check = Checkbutton(frame,
                             text='Resource dosyası oluştur',
                             command=createTabCMD,
                             variable=resource_check_val,
                             onvalue=True,
                             offvalue=False)
resource_check.place(x=120, y=80)

request = Label(frame, text="Request", font=18)
request.place(x=10, y=120)
request_check = Checkbutton(frame,
                            text='Request dosyası oluştur',
                            command=createTabCMD,
                            variable=request_check_val,
                            onvalue=True,
                            offvalue=False)
request_check.place(x=120, y=120)

policies = Label(frame, text="Policies", font=18)
policies.place(x=10, y=160)
policies_check = Checkbutton(frame,
                             text='Policies dosyası oluştur',
                             command=createTabCMD,
                             variable=policies_check_val,
                             onvalue=True,
                             offvalue=False)
policies_check.place(x=120, y=160)

controller = Label(frame, text="Controller", font=18)
controller.place(x=10, y=200)
controller_check = Checkbutton(frame,
                               text='Controller dosyası oluştur',
                               command=createTabCMD,
                               variable=controller_check_val,
                               onvalue=True,
                               offvalue=False)
controller_check.place(x=120, y=200)

migrate = Label(frame, text="Migrate", font=18)
migrate.place(x=10, y=240)
migrate_check = Checkbutton(frame,
                            text='Migtare dosyası oluştur',
                            command=createTabCMD,
                            variable=migrate_check_val,
                            onvalue=True,
                            offvalue=False)
migrate_check.place(x=120, y=240)


def createCMD():
    print('Start Create')
    # Generate MODEL
    if model_check_val.get():
        modelsCheckCMD(modul_name_var.get())
    else:
        remove_folder("Models")
    # Generate RESOURCES
    if resource_check_val.get():
        policiesCheckCMD(modul_name_var.get())
    else:
        remove_folder("Resources")
    # Generate REQUEST
    if request_check_val.get():
        policiesCheckCMD(modul_name_var.get())
    else:
        remove_folder("Request")
    # Generate POLICIES
    if policies_check_val.get():
        policiesCheckCMD(modul_name_var.get())
    else:
        remove_folder("Policies")
    # Generate CONTROLLER
    if controller_check_val.get():
        controllerCheckCMD(modul_name_var.get())
    else:
        remove_folder("Controllers")
    # Generate MIGRATE
    print('End Create')


createBtn = Button(frame, text="Create Module", command=createCMD)
createBtn.place(x=120, y=320)

button = Button(frame, text="Exit", width=30, command=root.destroy)
button.pack(side=BOTTOM)

root.mainloop()
