import os
import shutil

#Folder path you want to organize
FOLDER_PATH = os.getcwd() #Current working directory

#File type mapping
File_Type = { 
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz','.tff'],
    'Scripts': ['.js', '.sh', '.bat']
    }

# Create folder if they don't exit
for folder in File_Type.keys(): #Create folder for each fiel type
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

#Organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)
       
    #skip folders
    if os.path.isdir(file_path):
        continue

    #Get file extention
    # print(os.path.splitext(file)[1].lower())
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in File_Type.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))

print("Files Organized succfully✅")

