import time
from backup import BackupTool


def main():
    backup_tool = BackupTool()
    backup_tool.full_backup("folder1")
    time.sleep(1)
    backup_tool.full_backup("folder1")
    time.sleep(1)
    backup_tool.differential_backup("folder1")
    time.sleep(10)
    backup_tool.differential_backup("folder1")
    time.sleep(1)
    backup_tool.differential_backup("folder1")

    for b in backup_tool.backup_list:
        print(b.type, b.source, b.destination, b.date)
        for f in b.files:
            print(f.path, f.hash)


if __name__ == '__main__':
    main()
