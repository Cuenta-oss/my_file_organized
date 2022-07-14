from pathlib import Path, PurePath
import shutil
import os


def run():

    def create_path(ruta, lista):
        '''
        Funcion que recibe una ruta y una lista de archivos y crea directorios en la ruta indicada
        Parametros:
            ruta: ruta donde se crearan los directorios.
            lista: lista de nombres de los directorios a crear.
        Devuelve:
            La creacion de los directorios en la ruta indicada.
        '''
        for i in lista:
            try:
                PurePath.joinpath(Path.cwd(), ruta, i).mkdir()
                return "Directories created"
            except FileExistsError:
                pass

    def get_file(file_source):
        '''
        Función que recibe una ruta donde se escentran los archivos a organizar, moviendolo a una ruta 
        especificada.
        Parametros:
            file_source: ruta donde se encuentran los archivos a organizar.
        Devuelve:
            Los archivos movidos a la ruta indicada.
        '''
        for i in Path(file_source).iterdir():
            root, extension = os.path.splitext(i)
            print("File name: {} -> extension: {}".format(root, extension))
            if extension in [".jpg", ".png", ".gif", ".jpeg"]:
                file_destination = r"D:\Content\Imagenes"
                shutil.move(os.path.join(file_source, i), file_destination)
            elif extension in [".xls", ".xlsx"]:
                file_destination = r"D:\Content\Excel"
                shutil.move(os.path.join(file_source, i), file_destination)
            elif extension in [".doc", ".docx"]:
                file_destination = r"D:\Content\Word"
                shutil.move(os.path.join(file_source, i), file_destination)
            elif extension in [".pdf"]:
                file_destination = r"D:\Content\PDF"
                shutil.move(os.path.join(file_source, i), file_destination)
            elif extension in [".ppt", ".pptx"]:
                file_destination = r"D:\Content\PowerPoint"
                shutil.move(os.path.join(file_source, i), file_destination)
            else:
                file_destination = r"D:\Content\Otros"
                shutil.move(os.path.join(file_source, i), file_destination)
    # Nombres dee los irectorios a crear
    directories_name = ["Excel", "PDF", "Word", "PowerPoint",
                        "Imagenes", "Otros", "Video", "Audio", "Archivos"]
    create_path(r"D:\Content", directories_name)
    get_file(r"C:\Users\afg11\Downloads")


if __name__ == '__main__':
    run()
