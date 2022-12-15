import shutil
import os


def create_new_folder(name):
    os.mkdir(name)

def delete_folder(name):
    os.rmdir(name)

def open_folder(name):
    os.chdir(name)

def previuos_dir(cur_dir):
    if cur_dir != os.getcwd():
        os.chdir("..")
    else:
        print("Выход за пределы рабочей папки запрещен!")

def create_file(name):
    file = open(name, "a")
    file.close()

def text_entry(name, text):
    file = open(name, "a")
    file.write(text)
    file.close()

def view_file(name):
    file = open(name, "r")
    print(file.read())
    file.close()

def delete_file(name):
    os.remove(name)

def copy_file(name, new_dir):
    shutil.copyfile(name, new_dir)

def replace_file(name, new_dir):
    shutil.move(name, new_dir)

def rename_file(name, new_name):
    os.rename(name, new_name)
