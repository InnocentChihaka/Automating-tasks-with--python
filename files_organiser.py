import os, shutil

def files_organiser(source, destination):
   for file in os.listdir(source):
       file_path = os.path.join(source, file)
       extension = os.path.splitext(file)[1].lower()

# creating the new folder for the extension
        extension_folder = os.makedirs(os.path.join(destination, extension), exist_ok=True)
        destination_folder = os.path.join(extension_folder, file)
        
# move the folder to destination folder
        shutil.move(file_path, destination_folder)
        
   
files_organiser()
        
#1 i need to get the path
#2 list of files inside the path
#3 get the file
#4 split the filename and extension
# 5 create a a new forlder 
# 6 move the file to the new flder and destination