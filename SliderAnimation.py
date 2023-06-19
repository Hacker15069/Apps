class SliderAnimate:
    def __init__(self, root, widget, type, start_pos, stretch_length=50, frame_length=10, delay=10, height=600, width=600):
        
        #specifying the window to display the widget(self.widget)
        self.root = root

        #specifying the widget for a window(self.root)
        self.widget = widget

        #specifying if the widget should be on the right or left side and
        #in which direction(horizontal or vertical)
        self.type = type

        #specifying the distance the animation will move from a point to another
        self.stretch_length = stretch_length

        #specifying the placement of the widget
        self.start_pos = start_pos

        #specifying the length of the frame per time(self.delay)
        self.frame_length = frame_length

        #specifying how long it will take for the next frame to appear
        self.delay = delay

        #specifying the height of the animated widget
        self.height = height

        #specifying the width of the animated widget
        self.width = width

        #this attribute keeps track of the widget movement
        # (the widget current length and/or the x/y position depending on the type(self.type))
        self.present_length = 0

        #the self.new_length attribute was created for the right side only, in 
        # either the vertical or horizontal direction
        self.new_length = 0

        #the tell the program to either open the widget(forward method) 
        #or close the widget(backward method)
        self.end_meet = False

    # this forward method stretches the widget to the expected length(self.stretch_lengths)
    def forward(self):
        #this ensures the width of the animated widget doesn't expand over the expected length(self.stretch_length)
        if self.present_length < self.stretch_length:

            #As I said earlier, this keeps track of the frame movement
            self.present_length+=self.frame_length
            
            #This block statement is only for widgets that are the left side of a window that wants to
            #move horizontally
            if self.type == ("left","hor"):
                self.widget.place(
                x=self.start_pos[0],
                y=self.start_pos[1],
                height=self.height,
                width=self.present_length)

            #This block statement is only for widgets that are the left side of a window that wants to
            #move vertically
            elif self.type == ("left","ver"):
                self.widget.place(
                x=self.start_pos[0],
                y=self.start_pos[1],
                height=self.present_length,
                width=self.width)
            
            #This block statement is only for widgets that are the right side of a window that wants to
            #move horizontally
            elif self.type == ("right","hor"):
                #the self.new_length attribute is made for the right sides only in either the
                # horizontal or vertical direction
                self.new_length = self.start_pos[0]-self.present_length

                self.widget.place(
                x=self.new_length,
                y=self.start_pos[1],
                height=self.height,
                width=self.present_length)
            
            #This block statement is only for widgets that are the right side of a window that wants to
            #move vertically
            elif self.type == ("right","ver"):
                #the self.new_length attribute is made for the right sides only in either the
                # horizontal or vertical direction
                self.new_length = self.start_pos[1]-self.present_length

                self.widget.place(
                x=self.start_pos[0],
                y=self.new_length,
                height=self.present_length,
                width=self.width)

            #calls the foward method ones the the delay(self.delay) has ended
            self.root.after(self.delay, self.forward) 

        #if the first command in the forward method is False, this attribute carries the value True.
        #  It is need for the second method to close the widget after in has been opened
        self.end_meet = True

    # this stretches the widget back to its initial position as if it has never been moved 
    def backward(self):

        #the first condition here works for only the horizontal directions(left&right) but the 
        # second condition if for only the horizontal direction(left&right)
        conditions = [
            self.present_length > self.start_pos[0],
            self.present_length > self.start_pos[1]
        ]

        #this ensures that the position gets back to its initial position
        if conditions[0] or conditions[1]:

            #Again keeping track of the frame movement
            self.present_length-=self.frame_length

            #This block statement is only for widgets that are the left side of a window that wants to
            #move horizontally
            if self.type == ("left","hor"):
                self.widget.place(
                x=self.start_pos[0],
                y=self.start_pos[1],
                height=self.height,
                width=self.present_length)

            #This block statement is only for widgets that are the left side of a window that wants to
            #move vertically
            elif self.type == ("left","ver"):
                self.widget.place(
                x=self.start_pos[0],
                y=self.start_pos[1],
                height=self.present_length,
                width=self.width)
            
            #This block statement is only for widgets that are the right side of a window that wants to
            #move horizontally
            elif self.type == ("right","hor"):
                #the self.new_length attribute is made for the right sides only in either the
                # horizontal or vertical direction
                self.new_length = self.new_length+self.frame_length

                self.widget.place(
                x=self.new_length,
                y=self.start_pos[1],
                height=self.height,
                width=self.present_length)
            
            #This block statement is only for widgets that are the right side of a window that wants to
            #move vertically
            elif self.type == ("right","ver"):
                self.new_length = self.new_length+self.frame_length

                self.widget.place(
                x=self.start_pos[0],
                y=self.new_length,
                height=self.present_length,
                width=self.width)

            #calls the backward method ones the the delay(self.delay) has ended
            self.root.after(self.delay, self.backward)

        #if the first command in the backward method is False, this attribute carries the value True.
        # It is needed for the second method to open the widget after in has been opened
        self.end_meet = False

    #this is the method the that tells when to move forward or backward with the help of 
    #the self.end_meet and self.end_meet boolean variables
    def motion(self):
        if self.end_meet == False:
            self.forward()
        elif self.end_meet == True:
            self.backward()

if __name__ == "__main__":
    def test():
        from tkinter import ttk
        import tkinter as tk

        #self.root --> window
        
        window = tk.Tk()
        window.title('Animated Widget')
        window.geometry('600x400')

        #self.widget --> label
        canvas = tk.Canvas(window, bg='lightblue')

        #This button runs the motion method
        Type = {
            "left_hor": [("left", "hor"), (0,0)], 
            "left_ver": [("left", "ver"), (0,0)],
            "right_hor": [("right", "hor"), (600,0)],
            "right_ver": [("right", "ver"), (0,400)]
        }

        #initializing the 'SliderAnimate' class for testing
        animation = SliderAnimate(
            root=window,
            widget=canvas,
            type=Type["right_ver"][0],
            start_pos=Type["right_ver"][1],
            stretch_length=300,
            width=600, 
            height=400)
        
        #Note: Be careful with the start_pos and the type of the SliderAnimate class, this
        # two must work together to work well. Check out the example above for a quick sample.

        #button for testing
        ttk.Button(window, text='Button', command=animation.motion).pack()

        window.mainloop()

    test()