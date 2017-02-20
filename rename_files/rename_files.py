import os

def rename_files():
    #returns a list containing the names of the entries in the directory given by path.
    file_list = os.listdir(r"/Users/briceida/prank")
    # returns current working directory of a process
    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)
    #changes the current working directory to the given path.It returns None in all the cases.
    os.chdir(r"/Users/briceida/prank")

    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.strip("0123456789"))
        #renames the file or directory src to dst.os.rename(src, dst)
        os.rename(file_name, file_name.strip("0123456789"))

    os.chdir(saved_path)
        

rename_files()
