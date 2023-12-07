import customtkinter as ctk
import ttkbootstrap as ttk
import tkinter as tk

# System Settings
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')

# App Frame
root = ctk.CTk()
root.geometry('500x300')
root.title('Virtual keyboard')

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

letterframe = ctk.CTkFrame(root)
letterframe.columnconfigure(0, weight=3)

spacebarframe = ctk.CTkFrame(root)
spacebarframe.columnconfigure(0, weight=4)

btn1 = ctk.CTkButton(buttonframe, width=9, height=7, text='1', font=('Consolas', 28, 'bold'), command=btn1_clicked)
btn1.grid(row=0, column=0, sticky='news', padx=2)

btn2 = ctk.CTkButton(buttonframe, width=9, height=7, text='2', font=('Consolas', 28, 'bold'), command=btn2_clicked)
btn2.grid(row=0, column=1, sticky='news', padx=2)

btn3 = ctk.CTkButton(buttonframe, width=9, height=7, text='3', font=('Consolas', 28, 'bold'), command=btn3_clicked)
btn3.grid(row=0, column=2, sticky='news', padx=2)

btn4 = ctk.CTkButton(buttonframe, width=9, height=7, text='4', font=('Consolas', 28, 'bold'), command=btn4_clicked)
btn4.grid(row=0, column=3, sticky='news', padx=2)

btn5 = ctk.CTkButton(buttonframe, width=9, height=7, text='5', font=('Consolas', 28, 'bold'), command=btn5_clicked)
btn5.grid(row=0, column=4, sticky='news', padx=2)

btn6 = ctk.CTkButton(buttonframe, width=9, height=7, text='6', font=('Consolas', 28, 'bold'), command=btn6_clicked)
btn6.grid(row=0, column=5, sticky='news', padx=2)

btn7 = ctk.CTkButton(buttonframe, width=9, height=7, text='7', font=('Consolas', 28, 'bold'), command=btn7_clicked)
btn7.grid(row=0, column=6, sticky='news', padx=2)

btn8 = ctk.CTkButton(buttonframe, width=9, height=7, text='8', font=('Consolas', 28, 'bold'), command=btn8_clicked)
btn8.grid(row=0, column=7, sticky='news', padx=2)

btn9 = ctk.CTkButton(buttonframe, width=9, height=7, text='9', font=('Consolas', 28, 'bold'), command=btn9_clicked)
btn9.grid(row=0, column=8, sticky='news', padx=2)

btn0 = ctk.CTkButton(buttonframe, width=9, height=7, text='0', font=('Consolas', 28, 'bold'), command=btn0_clicked)
btn0.grid(row=0, column=9, sticky='news', padx=2)

buttonframe.pack(pady=20)

# SPECIAL CHARACTERS GO HERE
# WILL BE ADDED LATER
# (TRUST)

btn_a = ctk.CTkButton(letterframe, width=7, height=7, text='A', font=('Consolas', 28, 'bold'), command=btn_a_clicked)
btn_a.grid(row=0, column=0, padx=2, pady=2)

btn_b = ctk.CTkButton(letterframe, width=7, height=7, text='B', font=('Consolas', 28, 'bold'), command=btn_b_clicked)
btn_b.grid(row=0, column=1)

btn_c = ctk.CTkButton(letterframe, width=7, height=7, text='C', font=('Consolas', 28, 'bold'), command=btn_c_clicked)
btn_c.grid(row=0, column=2)

btn_d = ctk.CTkButton(letterframe, width=7, height=7, text='D', font=('Consolas', 28, 'bold'), command=btn_d_clicked)
btn_d.grid(row=0, column=3)

btn_e = ctk.CTkButton(letterframe, width=7, height=7, text='E', font=('Consolas', 28, 'bold'), command=btn_e_clicked)
btn_e.grid(row=0, column=4)

btn_f = ctk.CTkButton(letterframe, width=7, height=7, text='F', font=('Consolas', 28, 'bold'), command=btn_f_clicked)
btn_f.grid(row=0, column=5)

btn_g = ctk.CTkButton(letterframe, width=7, height=7, text='G', font=('Consolas', 28, 'bold'), command=btn_g_clicked)
btn_g.grid(row=0, column=6)

btn_h = ctk.CTkButton(letterframe, width=7, height=7, text='H', font=('Consolas', 28, 'bold'), command=btn_h_clicked)
btn_h.grid(row=0, column=7)

btn_i = ctk.CTkButton(letterframe, width=7, height=7, text='I', font=('Consolas', 28, 'bold'), command=btn_i_clicked)
btn_i.grid(row=0, column=8)

btn_j = ctk.CTkButton(letterframe, width=7, height=7, text='J', font=('Consolas', 28, 'bold'), command=btn_j_clicked)
btn_j.grid(row=0, column=9)

btn_k = ctk.CTkButton(letterframe, width=7, height=7, text='K', font=('Consolas', 28, 'bold'), command=btn_k_clicked)
btn_k.grid(row=0, column=10)

btn_l = ctk.CTkButton(letterframe, width=7, height=7, text='L', font=('Consolas', 28, 'bold'), command=btn_l_clicked)
btn_l.grid(row=0, column=11)

btn_m = ctk.CTkButton(letterframe, width=7, height=7, text='M', font=('Consolas', 28, 'bold'), command=btn_m_clicked)
btn_m.grid(row=0, column=12)

btn_n = ctk.CTkButton(letterframe, width=7, height=7, text='N', font=('Consolas', 28, 'bold'), command=btn_n_clicked)
btn_n.grid(row=0, column=13)

btn_o = ctk.CTkButton(letterframe, width=7, height=7, text='O', font=('Consolas', 28, 'bold'), command=btn_o_clicked)
btn_o.grid(row=1, column=1)

btn_p = ctk.CTkButton(letterframe, width=7, height=7, text='P', font=('Consolas', 28, 'bold'), command=btn_p_clicked)
btn_p.grid(row=1, column=2)

btn_q = ctk.CTkButton(letterframe, width=7, height=7, text='Q', font=('Consolas', 28, 'bold'), command=btn_q_clicked)
btn_q.grid(row=1, column=3)

btn_r = ctk.CTkButton(letterframe, width=7, height=7, text='R', font=('Consolas', 28, 'bold'), command=btn_r_clicked)
btn_r.grid(row=1, column=4)

btn_s = ctk.CTkButton(letterframe, width=7, height=7, text='S', font=('Consolas', 28, 'bold'), command=btn_s_clicked)
btn_s.grid(row=1, column=5)

btn_t = ctk.CTkButton(letterframe, width=7, height=7, text='T', font=('Consolas', 28, 'bold'), command=btn_t_clicked)
btn_t.grid(row=1, column=6)

btn_u = ctk.CTkButton(letterframe, width=7, height=7, text='U', font=('Consolas', 28, 'bold'), command=btn_u_clicked)
btn_u.grid(row=1, column=7)

btn_v = ctk.CTkButton(letterframe, width=7, height=7, text='V', font=('Consolas', 28, 'bold'), command=btn_v_clicked)
btn_v.grid(row=1, column=8)

btn_w = ctk.CTkButton(letterframe, width=7, height=7, text='W', font=('Consolas', 28, 'bold'), command=btn_w_clicked)
btn_w.grid(row=1, column=9)

btn_x = ctk.CTkButton(letterframe, width=7, height=7, text='X', font=('Consolas', 28, 'bold'), command=btn_x_clicked)
btn_x.grid(row=1, column=10)

btn_y = ctk.CTkButton(letterframe, width=7, height=7, text='Y', font=('Consolas', 28, 'bold'), command=btn_y_clicked)
btn_y.grid(row=1, column=11)

btn_z = ctk.CTkButton(letterframe, width=7, height=7, text='Z', font=('Consolas', 28, 'bold'), command=btn_o_clicked)
btn_z.grid(row=1, column=12)

letterframe.pack(ipady=5, ipadx=0, pady=2)

btn_spacebar = ctk.CTkButton(spacebarframe, width=3, height=3, text='SPACEBAR', font=('Consolas', 28, 'bold'), command=btn_spacebar_clicked)
btn_spacebar.grid(row=0, column=0)

spacebarframe.pack(ipady=4, ipadx=168)

root.mainloop()
