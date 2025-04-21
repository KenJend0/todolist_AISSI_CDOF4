import sys

todo_list = []

def afficher_taches():
    if not todo_list:
        print("\nNo tasks\n")
    else:
        print("\nTasks :")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def ajouter_tache(task):
    todo_list.append(task)
    print(f"\nTask added : {task}\n")

def supprimer_tache(index):
    try:
        removed = todo_list.pop(index - 1)
        print(f"\nTask removed : {removed}\n")
    except IndexError:
        print("\nIncorrect index\n")

def menu():
    print("Todo list Menu")
    print("1. View Tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    choix = input("Choose an option : ")
    return choix

def main():
    while True:
        choix = menu()
        if choix == '1':
            afficher_taches()
        elif choix == '2':
            task = input("Enter task : ")
            ajouter_tache(task)
        elif choix == '3':
            afficher_taches()
            try:
                index = int(input("Task number to remove : "))
                supprimer_tache(index)
            except ValueError:
                print("\nIncorrect entry !\n")
        elif choix == '4':
            print("\nSee you ! !\n")
            sys.exit()
        else:
            print("\nInvalid option, try again\n")

if __name__ == "__main__":
    main()
