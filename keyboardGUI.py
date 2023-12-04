import customtkinter as ctk
import ttkbootstrap as ttk
import tkinter as tk

# System Settings
ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# App Frame
root = ctk.CTk()
root.geometry('500x300')
root.title('Virtual keyboard')

label = tk.Label()
textbox = tk.Text()
button = tk.Button()


def btn1_clicked():
    print('1', end='')

def btn2_clicked():
    print('2', end='')

def btn3_clicked():
    print('3', end='')

def btn4_clicked():
    print('4', end='')

def btn5_clicked():
    print('5', end='')

def btn6_clicked():
    print('6', end='')

def btn7_clicked():
    print('7', end='')

def btn8_clicked():
    print('8', end='')

def btn9_clicked():
    print('9', end='')

def btn0_clicked():
    print('0', end='')


def btn_spacebar_clicked():
    print(' ', end='')

def btn_a_clicked():
    print('a', end='')

def btn_b_clicked():
    print('b', end='')

def btn_c_clicked():
    print('c', end='')

def btn_d_clicked():
    print('d', end='')

def btn_e_clicked():
    print('e', end='')

def btn_f_clicked():
    print('f', end='')

def btn_g_clicked():
    print('g', end='')

def btn_h_clicked():
    print('h', end='')

def btn_i_clicked():
    print('i', end='')

def btn_j_clicked():
    print('j', end='')

def btn_k_clicked():
    print('k', end='')

def btn_l_clicked():
    print('l', end='')

def btn_m_clicked():
    print('m', end='')

def btn_n_clicked():
    print('n', end='')

def btn_o_clicked():
    print('o', end='')

def btn_p_clicked():
    print('p', end='')

def btn_q_clicked():
    print('q', end='')

def btn_r_clicked():
    print('r', end='')

def btn_s_clicked():
    print('s', end='')

def btn_t_clicked():
    print('t', end='')

def btn_u_clicked():
    print('u', end='')

def btn_v_clicked():
    print('v', end='')

def btn_w_clicked():
    print('w', end='')

def btn_x_clicked():
    print('x', end='')

def btn_y_clicked():
    print('y', end='')

def btn_z_clicked():
    print('z', end='')


buttonframe = ctk.CTkFrame(root)
buttonframe.columnconfigure(0, weight=1)
letterframe = ttk.Frame(root)
letterframe.columnconfigure(0, weight=3)

btn1 = tk.Button(buttonframe, padx=10, text='1', font=('Roboto', 24, 'bold'), command=btn1_clicked)
btn1.grid(row=0, column=0, sticky='news')

btn2 = tk.Button(buttonframe, padx=10, text='2', font=('Roboto', 24, 'bold'), command=btn2_clicked)
btn2.grid(row=0, column=1, sticky='news')

btn3 = tk.Button(buttonframe, padx=10, text='3', font=('Roboto', 24, 'bold'), command=btn3_clicked)
btn3.grid(row=0, column=2, sticky='news')

btn4 = tk.Button(buttonframe, padx=10, text='4', font=('Roboto', 24, 'bold'), command=btn4_clicked)
btn4.grid(row=0, column=3, sticky='news')

btn5 = tk.Button(buttonframe, padx=10, text='5', font=('Roboto', 24, 'bold'), command=btn5_clicked)
btn5.grid(row=0, column=4, sticky='news')

btn6 = tk.Button(buttonframe, padx=10, text='6', font=('Roboto', 24, 'bold'), command=btn6_clicked)
btn6.grid(row=0, column=5, sticky='news')

btn7 = tk.Button(buttonframe, padx=10, text='7', font=('Roboto', 24, 'bold'), command=btn7_clicked)
btn7.grid(row=0, column=6, sticky='news')

btn8 = tk.Button(buttonframe, padx=10, text='8', font=('Roboto', 24, 'bold'), command=btn8_clicked)
btn8.grid(row=0, column=7, sticky='news')

btn9 = tk.Button(buttonframe, padx=10, text='9', font=('Roboto', 24, 'bold'), command=btn9_clicked)
btn9.grid(row=0, column=8, sticky='news')

btn0 = tk.Button(buttonframe, padx=10, text='0', font=('Roboto', 24, 'bold'), command=btn0_clicked)
btn0.grid(row=0, column=9, sticky='news')

buttonframe.pack(padx=20, pady=20)


btn_a = tk.Button(letterframe, padx=100, text='A', font=('Roboto', 22, 'bold'), command=btn_a_clicked)
btn_a.grid(row=0, column=0)

btn_b = tk.Button(letterframe, text='B', font=('Roboto', 22, 'bold'), command=btn_b_clicked)
btn_b.grid(row=0, column=1)

btn_c = tk.Button(letterframe, text='C', font=('Roboto', 22, 'bold'), command=btn_c_clicked)
btn_c.grid(row=0, column=2)

btn_d = tk.Button(letterframe, text='D', font=('Roboto', 22, 'bold'), command=btn_d_clicked)
btn_d.grid(row=0, column=3)

btn_e = tk.Button(letterframe, text='E', font=('Roboto', 22, 'bold'), command=btn_e_clicked)
btn_e.grid(row=0, column=4)

btn_f = tk.Button(letterframe, text='F', font=('Roboto', 22, 'bold'), command=btn_f_clicked)
btn_f.grid(row=0, column=5)

btn_g = tk.Button(letterframe, text='G', font=('Roboto', 22, 'bold'), command=btn_g_clicked)
btn_g.grid(row=0, column=6)

btn_h = tk.Button(letterframe, text='H', font=('Roboto', 22, 'bold'), command=btn_h_clicked)
btn_h.grid(row=0, column=7)

btn_i = tk.Button(letterframe, text='I', font=('Roboto', 22, 'bold'), command=btn_i_clicked)
btn_i.grid(row=0, column=8)

btn_j = tk.Button(letterframe, text='J', font=('Roboto', 22, 'bold'), command=btn_j_clicked)
btn_j.grid(row=0, column=9)

btn_k = tk.Button(letterframe, text='K', font=('Roboto', 22, 'bold'), command=btn_k_clicked)
btn_k.grid(row=0, column=10)

btn_l = tk.Button(letterframe, text='L', font=('Roboto', 22, 'bold'), command=btn_l_clicked)
btn_l.grid(row=0, column=11)

btn_m = tk.Button(letterframe, text='M', font=('Roboto', 22, 'bold'), command=btn_m_clicked)
btn_m.grid(row=0, column=12)

btn_n = tk.Button(letterframe, text='N', font=('Roboto', 22, 'bold'), command=btn_n_clicked)
btn_n.grid(row=0, column=13)

btn_o = tk.Button(letterframe, text='O', font=('Roboto', 22, 'bold'), command=btn_o_clicked)
btn_o.grid(row=1, column=1)

btn_p = tk.Button(letterframe, text='P', font=('Roboto', 22, 'bold'), command=btn_p_clicked)
btn_p.grid(row=1, column=2)

btn_q = tk.Button(letterframe, text='Q', font=('Roboto', 22, 'bold'), command=btn_q_clicked)
btn_q.grid(row=1, column=3)

btn_r = tk.Button(letterframe, text='R', font=('Roboto', 22, 'bold'), command=btn_r_clicked)
btn_r.grid(row=1, column=4)

btn_s = tk.Button(letterframe, text='S', font=('Roboto', 22, 'bold'), command=btn_s_clicked)
btn_s.grid(row=1, column=5)

btn_t = tk.Button(letterframe, text='T', font=('Roboto', 22, 'bold'), command=btn_t_clicked)
btn_t.grid(row=1, column=6)

btn_u = tk.Button(letterframe, text='U', font=('Roboto', 22, 'bold'), command=btn_u_clicked)
btn_u.grid(row=1, column=7)

btn_v = tk.Button(letterframe, text='V', font=('Roboto', 22, 'bold'), command=btn_v_clicked)
btn_v.grid(row=1, column=8)

btn_w = tk.Button(letterframe, text='W', font=('Roboto', 22, 'bold'), command=btn_w_clicked)
btn_w.grid(row=1, column=9)

btn_x = tk.Button(letterframe, text='X', font=('Roboto', 22, 'bold'), command=btn_x_clicked)
btn_x.grid(row=1, column=10)

btn_y = tk.Button(letterframe, text='Y', font=('Roboto', 22, 'bold'), command=btn_y_clicked)
btn_y.grid(row=1, column=11)

btn_z = tk.Button(letterframe, text='Z', font=('Roboto', 22, 'bold'), command=btn_o_clicked)
btn_z.grid(row=1, column=12)

btn_spacebar = tk.Button(letterframe, text='  ', font=('arial'), command=btn_spacebar_clicked)
btn_spacebar.grid(row=1, column=0)

btn_spacebar = tk.Button(letterframe, text='  ', font=('arial'), command=btn_spacebar_clicked)
btn_spacebar.grid(row=1, column=13)

letterframe.pack()


root.mainloop()
