from tkinter import *
from PIL import Image, ImageTk
import os

#Now create Tkinter Window
root = Tk()
root.geometry("650x500")
root.resizable(False,False)
root.title("King's Gallery")

#Find the File path
path = os.getcwd()
li = os.listdir(path)
#Now check that or jpg or pang others all removed
typ=[".jpg",".png"]

#now new list have jpg and png file
new=[]
for i in range(len(li)):
  a=li[i]
  b=a.find('.')
  if a[b:] in typ:
    new.append(a)
#Create a cloumn Variable And Row variable
cou=0
ro=0

#Create the next button work is strated
def next(label,newroot,index):
  ind=index+1
  newroot.title("King's Gallery : {}".format(new[index]))
  label.grid_forget()
  if ind>len(new)-1:
    ind=0
    image(newroot,ind)
  else:
    image(newroot,ind)
  return

#Create Previous button work is started
def Previous(label,newroot,index):
  ind=index-1
  label.grid_forget()
  newroot.title("King's Gallery : {}".format(new[index]))
  if ind<0:
    ind=len(new)-1
    image(newroot,ind)
  else:
    image(newroot,ind)
  return

#Now we make the image in to the window
def image(newroot,k):
  #making a selected image
  tempimg=Image.open("{}".format(new[k]))
  #crop the selected image
  selectimg=tempimg.resize((250,250), Image.ANTIALIAS)
  final=ImageTk.PhotoImage(selectimg)
  #display the selected image
  label=Label(newroot,image=final,height=250,width=250)
  label.image=final
  label.grid(row=0,column=1)
  #buttons
  #Call The Next function
  nex=Button(newroot,text="Next>>",command=lambda:next(label,newroot,k))
  nex.grid(row=1,column=2)
  #Call the Previous Function
  privious=Button(newroot,text="<<Previous",command=lambda:Previous(label,newroot,k))
  privious.grid(row=1,column=0)
  #Destroy the new Window
  Exit=Button(newroot,text="!EXIT!",command=newroot.destroy)
  Exit.grid(row=1,column=1)
  return 

#position of the Button
def my_fun(k):
  #Create a new window
  newroot=Toplevel(root)
  newroot.title("King's Gallery : {}".format(new[k]))
  newroot.geometry("400x300")
  newroot.resizable(False,False)
  image(newroot,k)
  
#Now start to print the Images
for j in range(len(new)):
  #At the first Open The image
  img= Image.open(new[j])
  #and Resize The image
  image1=img.resize((100,100), Image.ANTIALIAS)
  #And print The image in the tkinter Window Use the label1
  test = ImageTk.PhotoImage(image1)
  label1 = Button(image=test,height=100,width=100,command=lambda k=j:my_fun(k))
  label1.image = test
  #Spearate the by using column
  if cou%8==0:
    ro+=1
    cou=0
  #And print the position of the image
  label1.grid(row=ro,column=cou)
  cou+=1

root.mainloop()