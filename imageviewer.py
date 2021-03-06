


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')
root.iconbitmap()

my_img1 = ImageTk.PhotoImage(Image.open("images/dog1.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/dog2.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/dog3.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/dog4.jpeg"))

image_list = [image=my_img1, image=my_img2, image=my_img3, image=my_img4]
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
  global my_label
  global button_forward
  global button_back
  
my_label.grid_forget()
my_label = Label1(image=image_list[image_number-1])

button_forward=Button(root, text=">>", command=lambda: forward(image_number+1))
button_back=Button(root, text="<<", command=lambda: forward(image_number-1))


if image_number == 4:
  button_forward = Button(root, text">>", state=DISABLED)

my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)

def back():
  global my_label
  global button_forward
  global button_back
  
  my_label.grid_forget()
  my_label=Label(image=image_list[image_number-1])
  button_forward = Button(root, text=">>", command=Lambda: forward(image_number+1))
  button_back=Button(root, text="<<", command=lambda: forward(image_number-1))
  
  if image_number == 1:
  button_back = Button(root, text"<<", state=DISABLED)
  
  my_label.grid(row=0, column=0, columnspan=3)
  button_back.grid(row=1, column=0)
  button_forward.grid(row=1, column=2)
