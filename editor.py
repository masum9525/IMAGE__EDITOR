from tkinter import ttk, Tk, PhotoImage,RIDGE,Canvas,GROOVE,Scale, HORIZONTAL,filedialog,RAISED
import cv2
from PIL import Image,ImageTk
import numpy as np


class FrontEnd: 
    def __init__(self, master):
        self.master=master
        self.master.geometry("750x630+250+10")
        self.master.title("MASUM'S  EDITOR")
        

#THE HEAD OF THE EDITOR____________________________________________________

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text="WELCOME TO  MASUM'S WORLD OF EDITING ").grid(row=0, column=1)
        ttk.Label(self.frame_header, text="PLEASE UPLOAD THE PHOTO TO EDIT").grid(row=1, column=1)
        
#THE MENU OF THE EDITOR______________________________________

        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief="ridge", padding=(50,20))

        ttk.Button(self.frame_menu,text="UPLOAD", command=self.upload_action).grid(row=0, 
            column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="FILTER", command=self.filter_action).grid(row=1, 
            column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="BLUR", command=self.blur_action).grid(row=2, 
            column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="ADJUST", command=self.adjust_action).grid(row=3, 
            column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="ROTATE", command=self.rotate_action).grid(row=4, 
            column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="FLIP", command=self.flip_action).grid(row=5, 
            column=0, padx=5, pady=5, sticky="sw")
        ttk.Button(self.frame_menu, text="SAVE", command=self.save_action).grid(row=6, 
            column=0, padx=5, pady=5, sticky="sw")
        
#FOOTER OF THE EDITOR_______________________________________________

        self.apply_and_cancel=ttk.Frame(self.master)
        self.apply_and_cancel.pack()
        ttk.Button(
            self.apply_and_cancel, text="APPLY", command=self.apply_action).grid(row=0, column=0,
             padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.apply_and_cancel, text="CANCEL", command=self.cancel_action).grid(row=0, column=1,
             padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.apply_and_cancel, text="REVERT ALL CHANGES", command=self.revert_action).grid(row=0, column=2,
             padx=5, pady=5, sticky='sw')
       
#WHERE PICTURE IS UPLOADED____________________________________________________
        self.canvas= Canvas(self.frame_menu, bg="orange", width=300, height=400)
        self.canvas.grid(row=0,column=1, rowspan=7)
        
        
      
        
    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass
        self.side_frame= ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief="raised", padding=(50,15))

#___________________UPLOAD________________________
 
    def upload_action(self):
        self.canvas.delete("all") 
        self.filename= filedialog.askopenfilename() 
        self.orignal_image=cv2.imread(self.filename)

        self.edited_image=cv2.imread(self.filename)
        self.filtered_image=cv2.imread(self.filename)
        
        self.display_image(self.edited_image)

    

 
#_____________________________FILTERS__________________

    def filter_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Negative", command=self.negative_action).grid(row=0, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Black & White", command=self.bw_action).grid(row=1, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Stylisation", command=self.style_action).grid(row=2, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(row=3, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Emboss", command=self.emb_action).grid(row=4, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Sepio", command=self.sepio_action).grid(row=5, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Binary-Threesolding", command=self.binary_action).grid(row=6, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Eroision", command=self.eoision_action).grid(row=7, column=2,padx=5,pady=5
            )
        ttk.Button(
            self.side_frame, text="Dialation", command=self.dialation_action).grid(row=8, column=2,padx=5,pady=5
            )



# ____________________BLUR________________________________________________

    def blur_action(self):
        self.refresh_side_frame()

        ttk.Label(
            self.side_frame, text="Averaging Blur").grid(row=0,column=2,padx=5,pady=5, sticky='sw')
       
        self.average_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1,column=2,padx=5,sticky='sw')

        ttk.Label(
            self.side_frame, text="Gaussian Blur").grid(row=2,column=2,padx=5,pady=5, sticky='sw')
        self.gaussian_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.gaussian_action)
        self.gaussian_slider.grid(row=3,column=2,padx=5,sticky='sw')

        ttk.Label(
            self.side_frame, text="Median Blur").grid(row=4,column=2,padx=5,pady=5, sticky='sw')
        self.median_slider = Scale(
            self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.median_action)
        self.median_slider.grid(row=5,column=2,padx=5,sticky='sw')

    
# _________________________ADJUST______________________

    def adjust_action(self):
        self.refresh_side_frame()
        ttk.Label(
            self.side_frame,text="Brightness").grid(row=0,column=2,padx=5,pady=5,sticky='sw')
        self.brightness_slider= Scale(
            self.side_frame, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL, command=self.brightness_action)
        self.brightness_slider.grid(row=1,column=2,padx=5,sticky='sw')
        self.brightness_slider.set(1)

        ttk.Label(
            self.side_frame,text="Sauration").grid(row=2,column=2,padx=5,pady=5,sticky='sw')
        self.saturation_slider= Scale(
            self.side_frame, from_=0, to_=2, resolution=0.1, orient=HORIZONTAL, command=self.saturation_action)
        self.saturation_slider.grid(row=3,column=2,padx=5,sticky='sw')
        self.saturation_slider.set(0)
         
#________________________________ROTATE_________________

    def rotate_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Rotate Left", command=self.rotate_left_action).grid(row=0, 
            column=2,padx=5,pady=5,sticky='sw')
        ttk.Button(
            self.side_frame, text="Rotate Right", command=self.rotate_right_action).grid(row=1, 
            column=2,padx=5,pady=5,sticky='sw')


  #_________________________FLIP__________________________________


    def flip_action(self):
        self.refresh_side_frame()
        ttk.Button(
            self.side_frame, text="Vertical Flip", command=self.vertical_action).grid(row=0, 
            column=2,padx=5,pady=5,sticky='sw')
        ttk.Button(
        self.side_frame, text="Horizontal Flip", command=self.horizontal_action).grid(row=1, 
            column=2,padx=5,pady=5,sticky='sw')


#____________________________SAVE_______________________________
    def save_action(self):
        orignal_file_type=self.filename.split('.')[-1]
        filename=filedialog.asksaveasfilename()
        filename=filename+"."+orignal_file_type

        cv2.imwrite(filename,self.edited_image)
        self.filename=filename


#____________________APPLY CANCEL NAD REVERT______________________________
    def apply_action(self):
        self.edited_image=self.filtered_image
        self.display_image(self.filtered_image)
        
    def cancel_action(self):
        self.display_image(self.edited_image)

    def revert_action(self):
        self.edited_image=self.orignal_image.copy()
        self.display_image(self.orignal_image)


#_______________________________Filter section___________________________________________________________________-

    def negative_action(self):
        self.filtered_image=cv2.bitwise_not(self.edited_image)
        self.display_image(self.filtered_image)
    def bw_action(self):
        self.filtered_image=cv2.cvtColor(self.edited_image, cv2.COLOR_BGR2GRAY)
        self.display_image(self.filtered_image)
        
    def sketch_action(self):
        ret, self.filtered_image=cv2.pencilSketch(self.edited_image, sigma_s=60,sigma_r=0.07,shade_factor=0.05)
        self.display_image(self.filtered_image)

    def style_action(self):
        self.filtered_image=cv2.stylization(self.edited_image, sigma_s=10,sigma_r=0.15)
        self.display_image(self.filtered_image)

    def emb_action(self):
        kernel=np.array([[0,-1,-1,],[1,0,-1],[1,1,0]])
        self.filtered_image=cv2.filter2D(self.orignal_image, -1,kernel)
        self.display_image(self.filtered_image)

    def sepio_action(self):
        kernel=np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        self.filtered_image=cv2.filter2D(self.orignal_image, -1,kernel)
        self.display_image(self.filtered_image)

    def binary_action(self):
        ret, self.filtered_image=cv2.threshold(self.edited_image,127,255,cv2.THRESH_BINARY)
        self.display_image(self.filtered_image)

    def eoision_action(self):
        kernel=np.ones((1,2), np.uint8)
        self.filtered_image=cv2.erode(self.edited_image,kernel, iterations=1)
        self.display_image(self.filtered_image)
        
    def dialation_action(self):
        kernel=np.ones((1,2), np.uint8)
        self.filtered_image=cv2.dilate(self.edited_image,kernel, iterations=1)
        self.display_image(self.filtered_image)


#_____________________________________BLUR SECTION____________________________________________
    
    def averaging_action(self,value):
        value=int(value)
        if value%2==0:
            value=value+1
        self.filtered_image=cv2.blur(self.edited_image, (value,value))
        self.display_image(self.filtered_image)

    def median_action(self, value):
        value=int(value)
        if value%2==0:
            value=value+1
        self.filtered_image=cv2.medianBlur(self.edited_image, value)
        self.display_image(self.filtered_image)
        
    def gaussian_action(self, value):
        value=int(value)
        if value%2==0:
            value=value+1
        self.filtered_image=cv2.GaussianBlur(self.edited_image, (value,value), 0)
        self.display_image(self.filtered_image)


#________________________ROATE AND FLIP____________________________________________________

    def rotate_left_action(self):
        self.filtered_image=cv2.rotate(self.edited_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.display_image(self.filtered_image)

    def rotate_right_action(self):
        self.filtered_image=cv2.rotate(self.edited_image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.filtered_image)

    def vertical_action(self):
        self.filtered_image=cv2.flip(self.edited_image,0)
        self.display_image(self.filtered_image)

    def horizontal_action(self):
        self.filtered_image=cv2.flip(self.edited_image,2)
        self.display_image(self.filtered_image)


#_______________________BRIGHTNESS AND SATURATON________________________________

    def brightness_action(self,value):
        self.filtered_image=cv2.convertScaleAbs(self.edited_image, alpha=self.brightness_slider.get())
        self.display_image(self.filtered_image)

    def saturation_action(self,event):
        self.filtered_image=cv2.convertScaleAbs(self.edited_image,alpha=1,beta=self.saturation_slider.get())
        self.display_image(self.filtered_image)

#___________________________DISPLAY CONTENT__________________________________________

    def display_image(self,image=None):
        #destroys all the old canvas widget
        self.canvas.delete("all")
        #if image is notpassed, we are going to show the recent edited image
        if image is None:
            image=self.edited_image.copy()
            
        else:
            image=image
            #we have to convert to rgb because image is always taken in bg form
        
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels= image.shape #channels pixels
        ratio=height/width

#if image size is greater than the canvas, assigning new height and width
        if  height>400 or width>300:
            if ratio<1:
                new_width=300
                new_height=int(new_width*ratio)
            else:
                new_height=400
                new_width=int(new_height*(width/height))
        self.ratio=height/new_height
        self.new_image=cv2.resize (image,(new_width,new_height))

        self.new_image=ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.canvas.config(width=new_width,height=new_height)
        self.canvas.create_image(new_width/2,new_height/2, image=self.new_image)


    
root=Tk()
FrontEnd(root)
root.mainloop()         

