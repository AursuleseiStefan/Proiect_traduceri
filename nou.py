import sys
import os


def creare_folder():
    directory_path = './'
    directory_name = 'directorcutraduceri'

    # Create the directory
    os.mkdir(os.path.join(directory_path, directory_name))


dictionar_de_cai = []
dictionar_de_arg = []


def citire_de_la_tastaura():
    if len(sys.argv) == 2:
        # The first command-line argument (sys.argv[0]) is the script name
        # Additional arguments start from sys.argv[1]
        name2 = sys.argv[1]

        name1 = sys.argv[0]
        dictionar_de_arg.append(name1)
        dictionar_de_arg.append(name2)


def print_folder_contents(folder_path):
    # Get the list of files and directories within the folder
    contents = os.listdir(folder_path)

    # Print each item in the folder
    for item in contents:
        dictionar_de_cai.append(item)
    return dictionar_de_cai


dictidetrad = []
dicti2 = []


def citiredinargumente():
    caleadinfolder = print_folder_contents(dictionar_de_arg[1])
    print(caleadinfolder)
    for ceva in caleadinfolder:
        path_dir = dictionar_de_arg[1]
        path_dir = path_dir.replace("\\", "/")
        file_path = path_dir +"/" + ceva
        print("File path:", file_path)
        functie_pentru_fiecare_fisier(file_path, ceva)


def functie_pentru_fiecare_fisier(file_path, numefisier):
    with open(file_path,  errors="ignore") as file:
        # Read the entire file content
        # content = file.read()
        # print(content)

        # Read the file line by line
        lines = file.readlines()
        for line in lines:
            dictidetrad.append(line)
    convertire()
    scrieinfisier(numefisier)


def scrieinfisier(numefisier):
    original_directory = os.getcwd()
    print(original_directory)
    nume_unde_sa_scrie = './directorcutraduceri'
    os.chdir(nume_unde_sa_scrie)
    file_path2 = numefisier
    with open(file_path2, "w") as file:
        for item in dicti2:
            file.write(item + "\n")
        print("List written to the file successfully.")
    os.chdir(original_directory)


def convertire():
    for cuvant in dictidetrad:
        # print (cuvant)
        # cuvant2 = cuvant.replace("º", "s")
        # cuvant2 = cuvant.replace("þ", "t")
        cuvant2 = cuvant.replace("ã", "a").replace("þ", "t").replace("º", "s")

        dicti2.append(cuvant2)


if __name__ == "__main__":
    # print(print_folder_contents(citire_de_la_tastaura()))
    creare_folder()
    citire_de_la_tastaura()
    citiredinargumente()
    # convertire()
    # scrieinfisier()

