import customtkinter as ctk

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

# App Frame
root = ctk.CTk()
root.geometry('500x300')
root.title('Virtual keyboard')

def btn_clicked(value):
    print(value, end='')

button_config = {
    '1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (0, 3), '5': (0, 4),
    '6': (0, 5), '7': (0, 6), '8': (0, 7), '9': (0, 8), '0': (0, 9),
    'A': (1, 0), 'B': (1, 1), 'C': (1, 2), 'D': (1, 3), 'E': (1, 4),
    'F': (1, 5), 'G': (1, 6), 'H': (1, 7), 'I': (1, 8), 'J': (1, 9),
    'K': (1, 10), 'L': (1, 11), 'M': (1, 12), 'N': (1, 13), 'O': (2, 1),
    'P': (2, 2), 'Q': (2, 3), 'R': (2, 4), 'S': (2, 5), 'T': (2, 6),
    'U': (2, 7), 'V': (2, 8), 'W': (2, 9), 'X': (2, 10), 'Y': (2, 11),
    'Z': (2, 12), ' ': (3, 0) # if the spacebar looks shit uhh idk
}

# extremely useful comment
buttonframe = ctk.CTkFrame(root, bg='#f0f0f0')
buttonframe.columnconfigure(0, weight=1)


# there was a error thing in here and im too lazy to fix it.
# future me can do it later

# for text, (row, column) in button_config.items():
    # btn = ctk.CTkButton(buttonframe, width=7, height=3,         text=text, font=('Consolas', 20, 'bold'), 
    # command=lambda t=text: btn_clicked(t), bg='#007bff', fg='white', bd=0)
    # btn.grid(row=row, column=column, sticky='news', padx=2, pady=2)

buttonframe.pack(pady=20)
root.mainloop()