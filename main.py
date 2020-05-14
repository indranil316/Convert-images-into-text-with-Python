import os
from googletrans import Translator

translator=Translator()

arr=[]
print("------------------------------THIS APPLICATION IS MADE BY INDRANIL KARMAKAR AND IS USING GOOGLE TESSERACT OCR----------------------------------")
print("Instruction : Rename the pictures as natural numbers starting from 1 to ..... n")
print("Enter the value of n : ")
n=int(input())
print("Press 1 to start the OCR")
status=int(input())
if status==1:
    for i in range(1,n+1,1):
        os.system("tesseract ./source/{}.png temp".format(i))
        os.system("type temp.txt>>output.txt")
    os.system("del /f temp.txt")
print("Text created.")
print("Translating to english......")
file=open("output.txt","r");
text=file.read()
file.close()
translation=translator.translate(text)
file2=open("translated text.txt","w")
file2.write("{}".format(translation))
file2.close()
print("Mission Completed")
print("Respect++")
