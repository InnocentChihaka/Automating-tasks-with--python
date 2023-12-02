import os
import shutil

def files_organiser(source, destination):
   for file in os.listdir(source):
       file_path = os.path.join(source, file)
       extension = os.path.splitext(file)[1].lower()
       
       extension_folder = os.makedirs(os.path.join(destination, extension), exist_ok=True)
       destination_folder = os.path.join(extension_folder, file)
        
# move the folder to destination folder
       shutil.move(file_path, destination_folder)
       

files_organiser(source, destination)
        