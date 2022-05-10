from tkinter import * 
from tkinter import ttk 
import Api.Admin_Api as Api 
import Service.Widget_service as ws 
class Admin_User_create: 
    @staticmethod 
    def generate_users(obj): 
        # clear all frames 
        for frame in obj.allframes: 
            frame.place_forget() 
        obj.allframes = [] 
        obj.user_name = StringVar()
        obj.user_password = StringVar()
        obj.user_role = StringVar()
        #craete form frame 
        obj.formframe = Frame(obj.window, bg="pink") 
        obj.formframe.place(x=70, y=250, width=450, height=450) 
        obj.allframes.append(obj.formframe) 

        # create table frame 
        obj.tableframe = Frame(obj.window, bg="pink") 
        obj.tableframe.place(x=540, y=250, width=450, height=450) 
        obj.allframes.append(obj.tableframe) 
        Admin_User_create.generate_user_table(obj)
        Admin_User_create.generate_form(obj)


    @staticmethod 
    def generate_user_table(obj): 

        def clickusertable(event):
            # get selected user 
            cur = obj.tree.selection() 
            cur = obj.tree.item(cur)
            data = cur['values'] 
            try: 
                obj.user_name.set(data[0])
                obj.user_password.set(data[1])
                obj.user_role.set(data[2])

            except: 
                pass

        #create a tree view 
        obj.tree = ttk.Treeview(obj.tableframe, columns=("username", "password", "roles"), height=10) 
        obj.tree.place(x=0, y=0, width=450, height=450)
        obj.tree.heading("#0") 
        obj.tree.heading("username", text="Username") 
        obj.tree.heading("password", text="Password") 
        obj.tree.heading("roles", text="Roles") 
        obj.tree.column("#0", width=0, stretch= False) 
        obj.tree.column("username", width=150, stretch=False) 
        obj.tree.column("password", width=150, stretch=False)  
        obj.tree.column("roles", width=150, stretch=False)
        obj.tree.bind("<<TreeviewSelect>>", clickusertable)
        
        #create scrollbar
        obj.scrollbarx = Scrollbar(obj.tableframe, orient="vertical", command=obj.tree.yview) 
        obj.scrollbarx.place(x=450, y=0, width=20, height=450)
        obj.scrollbary = Scrollbar(obj.tableframe, orient="horizontal", command=obj.tree.xview)
        obj.scrollbary.place(x=0, y=450, width=450, height=20)
        
        api = Api.Admin_Api() 
        users = api.get_all_users_data() 
        for user in users: 
            obj.tree.insert('', 'end', values=(user['username'], user['password'], user['roles']))

    @staticmethod 
    def generate_form(obj): 
        obj.label_username = Label(obj.formframe, text="Username", bg="pink") 
        obj.label_username.place(x=0, y=0, width=100, height=50) 
        obj.entry_username = Entry(obj.formframe, textvariable=obj.user_name, state=DISABLED) 
        obj.entry_username.place(x=100, y=0, width=300, height=50) 

        obj.label_password = Label(obj.formframe, text="Password", bg="pink") 
        obj.label_password.place(x=0, y= 70, width=100, height=50) 
        obj.entry_password = Entry(obj.formframe, textvariable=obj.user_password) 
        obj.entry_password.place(x=100, y=70, width=300, height=50) 

        obj.label_role = Label(obj.formframe, text="Role", bg="pink") 
        obj.label_role.place(x=0, y=140, width=100, height=50)
        
        
        obj.entry_role = ws.mycombobox(obj.formframe, textvariable=obj.user_role) 
        obj.entry_role.set_completion_list(["Admin", "User"])
        obj.entry_role.place(x=100, y=140, width=300, height=50)
         
         #create update button 
        obj.button_update = Button(obj.formframe, text="Update") 
        obj.button_update.place(x=100, y=200, width=100, height=50) 
        #create delete button 
        obj.button_delete = Button(obj.formframe, text="Delete") 
        obj.button_delete.place(x=200, y=200, width=100, height=50) 

        #create create button
        obj.button_create = Button(obj.formframe, text="Create new user", command=lambda: Admin_User_create.create_user())
        obj.button_create.place(x=100, y=250, width=200, height=50) 

    @staticmethod 
    def create_user(): 
        window = Tk()
        window.title("Create new user") 
        window.geometry("500x500") 
        window.resizable(False, False) 
        window.configure(background="pink") 
        # create label 
        label_username = Label(window, text="Username", bg="pink") 
        label_username.place(x=0, y=0, width=100, height=50) 
        # create entry 
        entry_username = Entry(window) 
        entry_username.place(x=100, y=0, width=200, height=50) 
        # create label 
        label_password = Label(window, text="Password", bg="pink")  
        label_password.place(x=0, y=70, width=100, height=50) 
        # create entry
        entry_password = Entry(window) 
        entry_password.place(x=100, y=70, width=200, height=50) 
        # create label
        label_role = Label(window, text="Role", bg="pink")
        label_role.place(x=0, y=140, width=100, height=50)
        # create entry
        entry_role = ws.mycombobox(window)
        entry_role.set_completion_list(["Admin", "User"])
        entry_role.place(x=100, y=140, width=200, height=50)

        # create create button 
        button_create = Button(window, text="Create")
        button_create.place(x=100, y=200, width=100, height=50) 
        #exit button 
        button_exit = Button(window, text="Exit", command=window.destroy) 
        button_exit.place(x=200, y=200, width=100, height=50) 

        window.mainloop() 


     





