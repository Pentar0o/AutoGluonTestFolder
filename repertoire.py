import os
import sys

#To use it (e.g) Launch the script in the same folder as the train on
#python3 repertoire.py .

if len(sys.argv) >1 :
    path = sys.argv[1]
    #We check if the folder train is existing and the test folder
    if os.path.exists(path+'/train'):   
        if not os.path.exists(path+'/test'): 
            os.mkdir(path+'/test')

        #We copy 10% of the files in the test folder and sub folders
        L = os.listdir("train")
        for dossier in L:
            os.mkdir(path+'/test/'+dossier)
            liste2=os.listdir(path+'/train/'+dossier)
            size=round(len(liste2)/10)
            for element in liste2:
                os.rename(path+f'/train/{dossier}/{element}', path+f'/test/{dossier}/{element}')
                size-=1
                if size==0:break

