import tkinter as tk

root = tk.Tk()                                                          # create object of tkinter module

root.title("Python Doc")                                                # set UI title
root.geometry("750x500")                                                    # set UI dimensions in pixels


checkBtn = tk.Checkbutton(root, height=20, width=50, font=('Arial', 10))      # dyn EditText Text(parent,height,width,font)
checkBtn.place(x=100,y=100,height=50,width=50)                                  # placing & state dimensions



root.mainloop()  # call mainloop() to make GUI continuous


"""

# *** Views ***
    # TextView
    textView = tk.Label(root, text="Hello World!", font=('Arial', 18))            Label(parent,text,font)
     
    # EditText(dynamic) 
    nLineEditText = tk.Text(root, height=20, width=50, font=('Arial', 10))        Text(parent,height,width,font)

    # EditText(static)  
    singleLineEditText = tk.Entry(root, font=('Arial', 10))                       Entry(parent,font)

    # Button      
    btn = tk.Button(root, text="Click Os", font=("Arial", 10))                    Button(parent,text,font)

    # CheckBox
    checkBox = tk.Checkbutton(root, height=20, width=50, font=('Arial', 10))      Checkbutton(parent,height,width,font)

# using either pack or place after each view
varName.pack(padx=10, pady=10)                                               # padding
varName.place(x=100,y=100,height=50,width=50)                                # placing & state dimensions

"""


"""

gridContainer = tk.Frame(root)                                              # GridLayout    Frame(root)
gridContainer.columnconfigure(0, weight=1)                                      # ClmNo with ratio
gridContainer.columnconfigure(1, weight=1)                                      # ClmNo with ratio
gridContainer.columnconfigure(2, weight=1)                                      # ClmNo with ratio

btn1=tk.Button(gridContainer, text="1", font=('Arial', 10))
btn1.grid(row=0,column=0,sticky=tk.W+tk.E)                          # Allocate bt1 in 00

btn1=tk.Button(gridContainer, text="2", font=('Arial', 10))
btn1.grid(row=0,column=1,sticky=tk.W+tk.E)                          # Allocate btn2 in 01

btn1=tk.Button(gridContainer, text="3", font=('Arial', 10))
btn1.grid(row=0,column=2,sticky=tk.W+tk.E)

gridContainer.pack(fill="x")


"""