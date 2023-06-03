import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import serial
import time

def chose_helper_button_clicked(event):
    print("Start button clicked!")
    helper_window() 
def accept_button_clicked(event):
    print("accept button clicked!")
    congrats_window()
def camera_button_clicked(event):
    print("camera button clicked!")
    camera_window()

# ----------------------------------------------Create the intro window----------------------------------------------
root = tk.Tk()
root.title("pick a helper")
#----------------------------------------------bg----------------------------------------------
# Get the screen width and height
screen_width, screen_height = 360, 800
root.geometry("%dx%d" % (screen_width, screen_height))
#make bg dimentions equal to window
bg_image_pg1 = Image.open("seva buddy app bg.png")
if bg_image_pg1.size != (screen_width, screen_height):
    bg_image_pg1 = bg_image_pg1.resize((screen_width, screen_height), Image.ANTIALIAS)
bg_image_pg1 = ImageTk.PhotoImage(bg_image_pg1)
#Adding background image in form of a label
bg_label_pg1 = ttk.Label(root, image = bg_image_pg1)
bg_label_pg1.place(x=0, y=0, relwidth=1, relheight=1)
bg_label_pg1.image = bg_image_pg1
#----------------------------------------------start button----------------------------------------------
# import the Start button image
chose_helper_image = Image.open("chose helper button.png")
chose_helper_image = chose_helper_image.resize((20, 20), Image.ANTIALIAS)
chose_helper_image = ImageTk.PhotoImage(chose_helper_image)
# Create a canvas to hold the start button image
chose_helper_canvas_1 = tk.Canvas(root, width=chose_helper_image.width(), height=chose_helper_image.height(), bg='white', highlightthickness=0)
chose_helper_canvas_1.pack()
# Add the image to the canvas
chose_helper_canvas_1.create_image(0, 0, anchor='nw', image=chose_helper_image)
chose_helper_canvas_1.place(relx=0.43, rely=0.315, anchor="center")
# Bind the button click event to the function
chose_helper_canvas_1.bind("<Button-1>", chose_helper_button_clicked)
# create the Start button with image
# start_button = tk.Button(root, image=start_button_image, bg = 'white',relief=tk.FLAT, command=start_button_clicked)
# start_button.pack()
# start_button.place(relx=0.5, rely=0.60, anchor="center")
# Create a canvas to hold the start button image
chose_helper_canvas_2 = tk.Canvas(root, width=chose_helper_image.width(), height=chose_helper_image.height(), bg='white', highlightthickness=0)
chose_helper_canvas_2.pack()
# Add the image to the canvas
chose_helper_canvas_2.create_image(0, 0, anchor='nw', image=chose_helper_image)
chose_helper_canvas_2.place(relx=0.47, rely=0.455, anchor="center")
# Bind the button click event to the function
chose_helper_canvas_2.bind("<Button-1>", chose_helper_button_clicked)
# Create a canvas to hold the start button image
chose_helper_canvas_3 = tk.Canvas(root, width=chose_helper_image.width(), height=chose_helper_image.height(), bg='white', highlightthickness=0)
chose_helper_canvas_3.pack()
# Add the image to the canvas
chose_helper_canvas_3.create_image(0, 0, anchor='nw', image=chose_helper_image)
chose_helper_canvas_3.place(relx=0.36, rely=0.605, anchor="center")
# Bind the button click event to the function
chose_helper_canvas_3.bind("<Button-1>", chose_helper_button_clicked)
# Create a canvas to hold the start button image
chose_helper_canvas_4 = tk.Canvas(root, width=chose_helper_image.width(), height=chose_helper_image.height(), bg='white', highlightthickness=0)
chose_helper_canvas_4.pack()
# Add the image to the canvas
chose_helper_canvas_4.create_image(0, 0, anchor='nw', image=chose_helper_image)
chose_helper_canvas_4.place(relx=0.36, rely=0.765, anchor="center")
# Bind the button click event to the function
chose_helper_canvas_4.bind("<Button-1>", chose_helper_button_clicked)

def helper_window():
    helper_window = tk.Toplevel()  # Create a new top-level window
    helper_window.title("helper window")  # Set the title of the new window
    #----------------------------------------------bg----------------------------------------------
    # Get the screen width and height
    screen_width, screen_height = 360, 800
    helper_window.geometry("%dx%d" % (screen_width, screen_height))
    #make bg dimentions equal to window
    bg_image_helper_window = Image.open("gig opportunity.png")
    if bg_image_helper_window.size != (screen_width, screen_height):
         bg_image_helper_window = bg_image_helper_window.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg_image_helper_window = ImageTk.PhotoImage(bg_image_helper_window)
    #Adding background image in form of a label
    bg_label_helper_window = ttk.Label(helper_window, image = bg_image_helper_window)
    bg_label_helper_window.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_helper_window.image = bg_image_helper_window
    #----------------------------------------------accept button----------------------------------------------
    # import the Start button image
    accept_button_image = Image.open("accept button.png")
    accept_button_image = accept_button_image.resize((80, 80), Image.ANTIALIAS)
    accept_button_image = ImageTk.PhotoImage(accept_button_image)
    # Create a canvas to hold the start button image
    accept_button_canvas = tk.Canvas(helper_window, width=accept_button_image.width(), height=accept_button_image.height(), highlightthickness=0)
    accept_button_canvas.pack()
    # Add the image to the canvas
    accept_button_canvas.create_image(0, 0, anchor='nw', image=accept_button_image)
    accept_button_canvas.place(relx=0.3, rely=0.70, anchor="center")
    # Bind the button click event to the function
    accept_button_canvas.bind("<Button-1>", accept_button_clicked)
    #----------------------------------------------deny button----------------------------------------------
    # import the Start button image
    deny_button_image = Image.open("deny button.png")
    deny_button_image = deny_button_image.resize((80, 80), Image.ANTIALIAS)
    deny_button_image = ImageTk.PhotoImage(deny_button_image)
    # Create a canvas to hold the start button image
    deny_button_canvas = tk.Canvas(helper_window, width=deny_button_image.width(), height=deny_button_image.height(), bg='white', highlightthickness=0)
    deny_button_canvas.pack()
    # Add the image to the canvas
    deny_button_canvas.create_image(0, 0, anchor='nw', image=deny_button_image)
    deny_button_canvas.place(relx=0.7, rely=0.70, anchor="center")
    # Bind the button click event to the function
    deny_button_canvas.bind("<Button-1>", _button_clicked)
def congrats_window(): 
#----------------------------------------------create central window----------------------------------------------
    congrats_window = tk.Toplevel()  # Create a new top-level window
    congrats_window.title("congrats")  # Set the title of the new window
    congrats_window.geometry("360x800")
#----------------------------------------------central window bg----------------------------------------------
    #make bg dimentions equal to window
    congrats_window_bg = Image.open("congrats window.png")
    if congrats_window_bg.size != (360, 800):
         congrats_window_bg = congrats_window_bg.resize((360, 800), Image.ANTIALIAS)
    congrats_window_bg = ImageTk.PhotoImage(congrats_window_bg)
    #Adding background image in form of a label
    congrats_window_canvas = tk.Label(congrats_window, image = congrats_window_bg)
    congrats_window_canvas.place(x=0, y=0, relwidth=1, relheight=1)
    congrats_window_canvas.image = congrats_window_bg
    #----------------------------------------------start button----------------------------------------------
    # import the Start button image
    camera_button_image = Image.open("camera logo.png")
    camera_button_image = camera_button_image.resize((25, 25), Image.ANTIALIAS)
    camera_button_image = ImageTk.PhotoImage(camera_button_image)
    # Create a canvas to hold the start button image
    camera_button_canvas = tk.Canvas(congrats_window, width=camera_button_image.width(), height=camera_button_image.height(), bg='blue', highlightthickness=0)
    camera_button_canvas.pack()
    # Add the image to the canvas
    camera_button_canvas.create_image(0, 0, anchor='nw', image=camera_button_image)
    camera_button_canvas.place(relx=0.15, rely=0.959, anchor="center")
    # Bind the button click event to the function
    camera_button_canvas.bind("<Button-1>", camera_button_clicked)
    
def camera_window(): 
#----------------------------------------------create central window----------------------------------------------
    camera_window = tk.Toplevel()  # Create a new top-level window
    camera_window.title("video calling")  # Set the title of the new window
    camera_window.geometry("360x450")
#----------------------------------------------central window bg----------------------------------------------
    #make bg dimentions equal to window
    camera_window_bg = Image.open("white bg.png")
    if camera_window_bg.size != (360, 400):
         camera_window_bg = camera_window_bg.resize((360, 400), Image.ANTIALIAS)
    camera_window_bg = ImageTk.PhotoImage(camera_window_bg)
    #Adding background image in form of a label
    camera_window_canvas = tk.Label(camera_window, image = camera_window_bg)
    camera_window_canvas.place(x=0, y=0, relwidth=1, relheight=1)
    camera_window_canvas.image = camera_window_bg
    
    label_data_wifi = tk.Label(camera_window, text="waiting for network...")
    label_data_wifi.pack()
    #----------------------------------------------start button----------------------------------------------
    # import the Start button image
    white_button_image = Image.open("start button red bg.png")
    white_button_image = white_button_image.resize((110, 60), Image.ANTIALIAS)
    white_button_image = ImageTk.PhotoImage(white_button_image)
    # Create a canvas to hold the start button image
    white_button_canvas = tk.Canvas(root, width=white_button_image.width(), height=white_button_image.height(), bg='white', highlightthickness=0)
    white_button_canvas.pack()
    # Add the image to the canvas
    white_button_canvas.create_image(0, 0, anchor='nw', image=white_button_image)
    white_button_canvas.place(relx=0.5, rely=0.60, anchor="center")
    # Bind the button click event to the function
    white_button_canvas.bind("<Button-1>", white_button_clicked)
    

# Start the Tkinter event loop
root.mainloop()