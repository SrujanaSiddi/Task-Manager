import hashlib
users = {}
tasks = {}

print("Welcome to Task-Manager!\n")

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register():
    username = input("Enter a username: ")
    if username in users:
        print("username already exists, pick another.")
    else:
        password = input("Enter a password: ")
        hashed_password = hash_password(password)
        users[username] = hashed_password
        choice = int(input("Do you want to see the password? 1.Yes 2.No: "))
        if choice == 1:
            print(password)
        print("User  registered!")
    
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == hash_password(password):
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

def add_task(username):
    task = input("Enter a task: ")
    if username in tasks:
        tasks[username].append(task)
    else:
        tasks[username] = [task]
    print("Task added!")

def delete_task(username):
    view_tasks(username)
    if username in tasks and tasks[username]: 
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index <= len(tasks[username]):
            removed_task = tasks[username].pop(task_index)
            print(f"Task '{removed_task}' deleted.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

def mark_complete(username):
    view_tasks(username)
    if username in tasks and tasks[username]: 
        task_index = int(input("Enter the task number to complete: ")) - 1
        if 0 <= task_index <= len(tasks[username]):
            status = 'completed'
            print("Task is marked complete.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks to complete.")
    return status


def view_tasks(username):
    print("Your tasks: ")
    if username in tasks:
        for task in tasks[username]:
            print("- " + task)
    else:
        print("No tasks found.")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("1.Add Task\t2.View tasks\t3.delete task\t4.Mark a task\t5.Logout.")
                    task_choice = input("Choose an option: ")

                    if task_choice == '1':
                        add_task(username)
                    elif task_choice == '2':
                        view_tasks(username)
                    elif task_choice == '3':
                        delete_task(username)
                    elif task_choice == '4':
                        mark_complete(username)
                    elif task_choice == '5':
                        break
                    else:
                        print("Invalid option.")
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Invalid option.")

main()
