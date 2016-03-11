## changes the name of files so that no numbers appear in the name

import os ## 
def rename_files():
    file_list = os.listdir(r"prank")
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir(r"prank")
    for file_name in file_list:
        print(file_name)
        os.rename(file_name, file_name.translate(None, '1234567890'))
        
rename_files()
