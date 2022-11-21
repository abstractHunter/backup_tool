import shutil
import datetime
import hashlib
import os


class FileBackupInfo:
    """
        FileBackupInfo:
            a class that represents a file and its hash
    """

    def __init__(self, path):
        self.path = path
        self.hash = self.get_hash()

    def get_hash(self):
        """
            get_hash:
                returns the hash of the file based on its content
        """
        with open(self.path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    def __eq__(self, other):
        """
            __eq__:
                checks if two FileBackupInfo objects are equal
                returns True if the paths are equal
        """
        return self.path == other.path and self.hash == other.hash


class BackupInfo:
    """
        BackupInfo:
            a class that represents a backup
    """

    def __init__(self, type, source, destination, date):
        self.type = type
        self.source = source
        self.destination = destination
        self.date = date
        self.files = []


class BackupTool:
    """
        BackupTool:
            a class that represents a backup tool
    """

    def __init__(self):
        self.backup_list = []
        self.last_full_backup = None

    def full_backup(self, source):
        """
            full_backup:
                creates a full backup of the source folder
                adds all the files in the source folder to the backup list

                arguments:
                    source: the folder to be backed up

                returns:
                    None
        """
        backup_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        destination = source + '_full_backup_' + backup_date

        # copy the source folder to the destination
        shutil.copytree(source, destination)

        # create a BackupInfo object
        bkp_info = BackupInfo('full', source, destination, backup_date)
        bkp_info.files = [FileBackupInfo(
            source + '/' + f) for f in os.listdir(source)]

        # save the backup info
        self.backup_list.append(bkp_info)
        self.last_full_backup = bkp_info

    def differential_backup(self, source):
        """
            differential_backup:
                creates a differential backup of the source folder
                adds the files that have changed or created since the last backup

                arguments:
                    source: the folder to be backed up

                returns:
                    None

        """
        backup_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        destination = source + '_differential_backup_' + backup_date

        # create the destination folder
        os.mkdir(destination)

        bkp_info = BackupInfo(
            'differential', source, destination, backup_date)

        last_backup = self.backup_list[-1]

        for file in os.listdir(source):
            fpath = source + '/' + file
            fbi = FileBackupInfo(fpath)

            # add newly created files
            if (fbi not in self.last_full_backup.files) and (fbi not in last_backup.files):
                shutil.copy(fpath, destination)
                bkp_info.files.append(fbi)

            # check if the file have been modified and add them to the backup
            else:
                if fbi in last_backup.files:
                    findex = last_backup.files.index(fbi)
                    prev_fbi = last_backup.files[findex]
                else:
                    findex = self.last_full_backup.files.index(fbi)
                    prev_fbi = self.last_full_backup.files[findex]

                if fbi.hash != prev_fbi.hash:
                    shutil.copy(fpath, destination)
                    bkp_info.files.append(fbi)

        # save the backup info
        self.backup_list.append(bkp_info)

    def restore(self):
        pass
