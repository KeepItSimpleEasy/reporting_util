import os
import datetime
import zipfile
import glob


class Util:

    @staticmethod
    def get_list_of_files(dir_name, file_pattern):
        # create a list of file and sub directories
        # names in the given directory
        list_of_file = os.listdir(dir_name)
        all_files = list()
        # Iterate over all the entries
        for entry in list_of_file:
            if entry.endswith(file_pattern):
                # Create full path
                full_path = os.path.join(dir_name, entry)
                # If entry is a directory then get the list of files in this directory
                all_files.append(full_path)
        return all_files

    @staticmethod
    def move_list_of_files(dir_name, archive_name, file_pattern):
        # create a list of file and sub directories
        # names in the given directory
        list_of_file = os.listdir(dir_name)
        # Iterate over all the entries

        for entry in list_of_file:
            if entry.endswith(file_pattern):
                # Create full path
                os.rename((dir_name + entry), (archive_name + entry + "_" + Util.get_curr_time_stamp()))

    @staticmethod
    def is_out_put_success(dir_name, file_name_pattern, file_ext):
        file_pattern = dir_name + file_name_pattern
        status = False
        if glob.glob(file_pattern + "*" + file_ext):
            status = True
        return status

    @staticmethod
    def get_curr_time_stamp():
        now = datetime.datetime.now()
        return str(now.strftime("%Y%m%d_%H-%M-%S"))

    @staticmethod
    def zip_files(dir_in, dir_out, file_pattern, zip_file_name):
        file_paths = Util.get_list_of_files(dir_in, file_pattern)
        with zipfile.ZipFile(dir_out+zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # writing each file one by one
            for file in file_paths:
                zip_file.write(file, os.path.relpath(file, dir_in))

    @staticmethod
    def get_environment_property(prop):
        return os.environ.get(prop)

