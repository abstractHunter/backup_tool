import os
from backup import BackupTool


def backup(backup_tool):
    print("\nBackup")
    source = input("Enter source directory: ")

    print("\n1. Full Backup")
    print("2. Differential Backup")
    print("0. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        print("Full Backup")
        backup_tool.full_backup(source=source)
    elif choice == "2":
        print("Differential Backup")
        backup_tool.differential_backup(source=source)
    elif choice == "0":
        return
    else:
        print("Invalid choice")


def restore(backup_tool):
    print("\nRestore")


def main():
    backup_tool = BackupTool()

    # clear the screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    cont = True
    while cont:

        print("""
Welcome to the Backup Tool

        1. Backup
        2. Restore
        0. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            backup(backup_tool)

        elif choice == "2":
            restore(backup_tool)

        elif choice == "0":
            cont = False
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
