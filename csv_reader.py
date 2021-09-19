import csv
import os
import shutil

file0 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/balaclava_ski_mask.csv")
file1 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/eyeglasses.csv")
file2 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/face_no_mask.csv")
file3 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/face_other_covering.csv")
file4 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/face_shield.csv")
file5 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/face_with_mask.csv")
file6 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/face_with_mask_incorrect.csv")
file7 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/hijab_niqab.csv")
file8 = open(
    "D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/no_mask.csv")
directory = 'D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/archive (1)/Medical mask/Medical mask/Medical Mask/images/'
destination = 'D:/Courses/Data Science Praktikum/Homeworks/Task-1/Datasets/Mask/no_mask/'

def copy(directory, destination, src=''):
    shutil.copy(directory+img, destination + img)

files = [file0, file1, file2, file3, file4, file5, file6, file7, file8]

csvreader = csv.reader(files[8])
for row in csvreader:
    img = row[0]
    copy("/path/directory","/path/destination", src=img)



row.close()

# 
# https: // stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
# https: // www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
# 
