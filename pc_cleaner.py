import os
import shutil


extensions={
"documents":[".txt",".pdf",".docx"],
"excel_files":[".csv",".xls"],
"python_files":[".py"],
"softwares":[".exe",".rar"],
"music":[".mp3",".wav"],
"videos":[".mp4",".3gp"],
"pics":[".jpeg",".png",".jpg",".JPG",".JPEG"]
}


folder_path=input("enter the path of the folder= ")
def folder_seperate(a,extension):
    c=[]
    for i in os.listdir(a):
        for j in extension:
            if (i.endswith(j)):
                c.append(i)
    return c
for k,m in extensions.items():
    # print(f"{k}:-\n{folder_seperate(folder_path,m)}")
    folder_path_name= os.path.join(folder_path,k)
    os.mkdir(folder_path_name)
    for i in folder_seperate(folder_path,m):
        file_path=os.path.join(folder_path,i)
        folder_file=os.path.join(folder_path_name,i)
        shutil.move(file_path,folder_file)
    




