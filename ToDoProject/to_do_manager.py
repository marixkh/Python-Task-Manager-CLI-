#to do manager
#variables
tasks = []

#main menu
def main_menu():
    print('Welcome To Our Task Manager')
    to_do = input('1.Add Task\n2.Show Tasks\n3.Remove Tasks\n4.Search Task\n5.Exit\n')
    if to_do == '1':
        add_task()
    elif to_do == '2':
        show_tasks()
    elif to_do == '3':
        remove_tasks()
    elif to_do == '4':
        search_tasks()
    elif to_do == '5':
        print('Have A Nice Day:)')
        exit()
    else:
        print('Invalid Choice, Try Again:(')

#add_task
def add_task():
    task_user = input('Enter Your Task: ').strip().lower()
    if task_user:
        tasks.append(task_user)
        #new part of my program/ reading and writing in files
        try:
            with open('tasks.txt', mode='a', encoding="utf-8") as file:
                file.write(task_user + '\n')
                print('Added To File Successfully:)')
        except:
            print('No File')
    else:
        print('Task Cannot Be Empty!!!')
        return

#show_tasks
def show_tasks():
    try:
        with open('tasks.txt', mode='r', encoding="utf-8") as file:
            content = file.readlines()
            if not content:
                print('No Tasks Found')
            else:
                print('\nMY TASKS: ')
                for index, task in enumerate(content, 1):
                    print(f'{index}.{task.strip()}')
    except FileNotFoundError: # اگر کلاً فایلی وجود نداشت
        print('--- No Tasks Found (File not created yet) ---')     
    # if tasks:
    #     for index, task in enumerate(tasks,1):
    #         print(f'{index} . {task}')
    # else:
    #     print('No Tasks Yet!!!')

#remove_tasks
def remove_tasks():
    list_tasks = []
    try:
        with open('tasks.txt', mode='r', encoding="utf-8") as file:
            content = file.readlines()
            if not content:
                print('No Tasks Found')
            else:
                for item in content:
                    list_tasks.append(item)
                remove = input('Which Task Do You Want To Remove?')
                if remove.isdigit():
                    remove = int(remove)
                    if remove >= 1 and remove <= len(list_tasks):
                        list_tasks.pop(int(remove)-1)
                    else:
                        print('Out Of Range!!!')
                else:
                    print('Invalid Number!!!')
        with open('tasks.txt', mode='w', encoding="utf-8") as file:
            for item in list_tasks:
                file.write(f'{item.strip()}\n')

    except:
        print('--- No Tasks Found (File not created yet) ---')
        # with open('tasks.txt', mode=)
        # if remove.isdigit():
        #     choice = int(remove)-1
        #     if choice>=0 and choice<len(tasks):
        #         tasks.pop(int(remove)-1)
        #         print(f'Task {choice+1} Deleted Successfully:)\n') 
        #     else:
        #         print('Out Of Range')
        # else:
        #     print('Invalid Task Number')
#search tasks
def search_tasks():
    list_tasks = []
    search_bar = input('What Are You Looking For? ').strip().lower()
    try:
        with open('tasks.txt', mode='r',encoding="utf-8") as file:
            content = file.readlines()
            if content:
                for item in content:
                    if search_bar in item:
                        print(f'-{item}')
            else:
                print('No Added Task yet')
    except:
        print('--- No Tasks Found (File not created yet) ---')


if __name__ == "__main__":
    try:
        while True:
            main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        exit()
