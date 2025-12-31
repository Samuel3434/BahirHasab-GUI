import tkinter as tk
import BHCal as bh
import holidays  
import random as rd
import my_moon as moon
import Ethiopian_to_gregorian as etog

root = tk.Tk()

root.geometry('850x670+20+20')
root.update_idletasks()
root.resizable(width=tk.FALSE,height = tk.FALSE)
root.title('Bahire Hassab')

current_year = 2016
######################################***variable***
screen_width = root.winfo_width()
screen_height = root.winfo_height()
days_of_week = ['ሰኞ','ማክሰኞ','ረቡዕ','ሀሙስ','አርብ','ቅዳሜ','እሁድ']
months = ['መስከረም','ጥቅምት','ህዳር','ታህሳስ','ጥር','የካቲት','መጋቢት','ሚያዝያ','ግንቦት','ሰኔ','ሐምሌ','ነሐሴ','ጳጉሜ']
SNFM = [0] # Starting Number For Month
# Frames

menu_frame = tk.Frame(root,bg='#052659',width= screen_width,height= 0.05*screen_height)
menu_frame.pack(expand = 1,fill = tk.BOTH,side=tk.TOP)

menu_year_shower_frame = tk.Frame(menu_frame,bg='#052659')
menu_year_shower_frame.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)

calendar_frame = tk.Frame(root, width=0.73*screen_width, height=0.958*screen_height,bg='#02c39a')
calendar_frame.pack(side=tk.LEFT, fill=tk.BOTH)
calendar_frame.pack_propagate(False)

calendar_days_frame = tk.Frame(calendar_frame,bg='#02c39a',width=0.75*screen_width,height=0.8*screen_height)
calendar_days_frame.pack(fill = tk.BOTH,expand=1)

control_frame = tk.Frame(calendar_frame,width=0.75*screen_width,height=0.12*screen_height,bg='#02c39A')
control_frame.pack()

daily_holidays_frame = tk.Frame(root,bg='#05668D', width=0.3*screen_width, height=0.725*screen_height)
daily_holidays_frame.pack(side=tk.TOP)
daily_holidays_frame.pack_propagate(False) 


lelit_frame = tk.Frame(root, width=(1/4)*screen_width,height=0.27*screen_height,bg='#05668d')
lelit_frame.pack(fill = tk.BOTH,expand=1)


teacher_frame = tk.Frame(calendar_frame, width=1.7*screen_width, height=0.95*screen_height)
###########################################****function*******


#**********************************************************
def eclipse_check(year, eclipse_result_frame,year_type):
    try:
        destroyer(eclipse_result_frame)
    except:
        pass
    if year_type == 'gc':
      aemete_alem = year + 5500
    elif year_type == 'ec':
      aemete_alem = year + 8+5500
    if aemete_alem % 19 == 0:
      result_text = f'There is an eclipse in {year}'
    else:
       result_text = f'There is no eclipse in {year}'
        
    result = tk.Label(eclipse_result_frame, text=result_text, background='#02c39a',font='70 ', fg=('#%02x%02x%02x') % (113, 57, 158))
    result.pack(pady=190)
def eclipse():
  destroyer(calendar_frame)
  try: 
    destroyer(menu_year_shower_frame)
  except:
    pass
  eclipse_frame = tk.Frame(calendar_frame, bg='#00a896')
  eclipse_frame.pack(side=tk.TOP,pady=10,padx=10,ipadx=10)
  eclipse_lbl = tk.Label(eclipse_frame,text= 'Enter Year',width=15,font='15',bg='#00a896',height=2).pack(side=tk.LEFT)
  eclipse_year_entry = tk.Entry(eclipse_frame, bg='#02c39A',width=70)
  eclipse_year_entry.pack(side=tk.LEFT)
  global eclipse_strvar
  eclipse_strvar = tk.StringVar()
  eclipse_strvar.set('ec')
  eclipse_frame2 = tk.Frame(calendar_frame,bg='#00a896')
  eclipse_frame2.pack(side=tk.TOP)
  year_type_ec = tk.Radiobutton(eclipse_frame2,text='Ethiopian Calendar',variable=eclipse_strvar,value='ec',bg='#00a896')
  year_type_ec.grid(row=0,column=0)
  year_type_gc = tk.Radiobutton(eclipse_frame2,text='Gregorian Calendar',variable=eclipse_strvar,value='gc',bg='#00a896')
  year_type_gc.grid(row=0,column=1)
  eclipse_result_frame = tk.Frame(calendar_frame,bg='#02c396')
  eclipse_result_frame.pack()
  result_button = tk.Button(eclipse_frame2, font=('arial', 10), width=10, height=2, relief=tk.FLAT, bg='#00a896', fg='white', text="Calculate", command=lambda: eclipse_check(int(eclipse_year_entry.get()), eclipse_result_frame,eclipse_strvar.get()))
  result_button.grid(row=2,column=0,columnspan=2)

def radio_checker(value,answer,R,*kag):
  if value.get() == bh.Wengelawi_name:
    R.config(bg='green')
  else:
    R.config(bg='red')
  for i in kag:
    i.config(bg='#02c39a')


def phase_label(year, month, day):
  global l
  try:
    l.destroy()
  except:
    pass
  l = tk.Label(calendar_frame, text = moon.moon_phase(year, month, day),background='#02c39a',fg = ('#%02x%02x%02x')%(113,57,158),font = 'Calibri 20 bold',width=15,height= 2, relief="flat")
  l.pack(pady=190)



def moon_phase_calc():
  destroyer(calendar_frame)
  try: 
    destroyer(menu_year_shower_frame)
  except:
    pass
  M_frame = tk.Frame(calendar_frame,bg='#00a896')
  M_frame.pack(side=tk.TOP,pady=10,padx=10,ipadx=10)
  year_label = tk.Label(M_frame, text = "Enter a year",height=3,bg='#00a896').pack(side=tk.LEFT)
  year = tk.Entry(M_frame, bg = "#02c398")
  year.pack(side=tk.LEFT)
  month_label = tk.Label(M_frame, text = "Enter a month",bg='#00a896').pack(side=tk.LEFT)
  month = tk.Entry(M_frame, bg = "#02c398")
  month.pack(side=tk.LEFT)
  day_label = tk.Label(M_frame, text = "Enter a day",bg='#00a896').pack(side=tk.LEFT)
  day = tk.Entry(M_frame, bg = "#02c398")
  day.pack(side=tk.LEFT)
  

  moonphase_stv = tk.StringVar()
  moonphase_stv.set('ec')
  MR_frame = tk.Frame(calendar_frame)
  MR_frame.pack()
  year_type_ec = tk.Radiobutton(MR_frame,text='Ethiopian Calendar',variable=moonphase_stv,value='ec',bg='#02c39a')
  year_type_ec.pack(side=tk.BOTTOM)
  year_type_gc = tk.Radiobutton(MR_frame,text='Gegorian Calendar',variable=moonphase_stv,value='gc',bg='#02c39a')
  year_type_gc.pack(side=tk.BOTTOM)
  def sending():
    if moonphase_stv.get() == 'ec':
      val2=etog.Ethiopian_to_gregorian(int(day.get()),int(month.get()),int(year.get()))
    else:
      val2 = [day.get(),month.get(),year.get()]

    phase_label(int(val2[0]), int(val2[1]), int(val2[2]))
  MC_frame = tk.Frame(calendar_frame)
  MC_frame.pack()
 
  b = tk.Button(MC_frame,font=('arial 10'), width=10, height=2, relief=tk.FLAT, bg='#00a896', fg='white', text = "Calculate" ,command = sending )
  b.pack(side=tk.LEFT)



    

def lelit_calc(d, m):
  destroyer(lelit_frame)
  if m == 12:
    hi = 6
  else:
    hi = (m + 2) // 2

  lelit = (bh.abekte + hi + d) if (bh.abekte + hi + d) <= 30 else (bh.abekte + hi + d) % 30
  lbl = tk.Label(lelit_frame,text=f'ሌሊት፡ {lelit}',width=20,height=2).pack(pady=35)





def general(year, month=0): 
  destroyer(calendar_days_frame, daily_holidays_frame,lelit_frame)
  
  gregorian_cal = etog.Ethiopian_to_gregorian(1,1,year) 

  try: 
    destroyer(menu_year_shower_frame)
  except:
    pass
  lbl = tk.Label(menu_year_shower_frame,text=f'{year}',font='60',bg='#052659',fg='white')
  lbl.pack(pady=10)
  bh.tsome = []
  bh.general_cal(year)
  no_days = 1
  calendar_row = 1
  override_bool = 0
  TEST = list()
  mi = (bh.mebacha_index) + 2*(month%13)
  is_leap = 1 if ((year + 1) % 4 == 0) else 0 

######################################################################
  for a, b in holidays.SH.items():
    for s in b.keys():
      TEST.append([a, s])

  for i in range(mi, mi + 30):
    for a in bh.tsome:
      TEST.append(a)

######################################################################
  holidays.Teaching_epi = []
  holidays.Teaching_epi.append(['ዓመተ-ዓለም',str(bh.amete_alem)])
  holidays.Teaching_epi.append(['መጠነ-ራበዒት',str(bh.metene_rabit)])
  holidays.Teaching_epi.append(['መባቻ',bh.mebacha])
  holidays.Teaching_epi.append (['ወንጌላዊ',bh.Wengelawi_name,bh.wengel])
  holidays.Teaching_epi.append(['መደብ',str(bh.medeb)])
  holidays.Teaching_epi.append(['ወንበር',str(bh.wenber)])
  holidays.Teaching_epi.append(['መጥቅዕ',str(bh.metqi)])
  holidays.Teaching_epi.append(['አበቅቴ',str(bh.abekte)])
  holidays.Teaching_epi.append(['መባጃ-ሐመር',(bh.Modified_mebaja_hammer)])
  for i in range(11):
    holidays.Teaching_epi.append([f'{bh.Bealat[i][0]}',bh.tsome[i][0]+' ' + str(bh.tsome[i][1])])


#########################################################################
  for i in range(7):
    calendar_days = tk.Label(calendar_days_frame, text=f'{days_of_week[i]}', bg='#02c39a', font='bold 12', width=9, height=4, fg='white')
    calendar_days.grid(column=i, row=0)

  if month % 13 == 12:
    
    for i in range(mi, mi + 5 + is_leap):
      for M, D in TEST:
        if M == months[month % 13] and D == no_days:
          color = 'blue'
          break
        else:
          color = '#00a896'
      btn = tk.Button(calendar_days_frame, text=f'{holidays.geeze_numbers[no_days-1]}',font=('arial 10'), width=5, height=3, relief=tk.FLAT, bg=color, fg='white', command=lambda a=no_days: holiday_diplayer(a, month % 13) )
      btn.grid(column=i % 7, row=calendar_row, padx=15, pady=7)
     
      no_days += 1
      if i % 7 == 6:
        calendar_row += 1
  else:
    for i in range(mi, mi + 30):
      for M, D in TEST:
        if M == months[month % 13] and D == no_days:
          color = 'blue'
          break
        else:
          color = '#00a896'
      btn = tk.Button(calendar_days_frame, text=f'{holidays.geeze_numbers[no_days-1]}',font=('arial 10') ,width=5, height=3, command=lambda a=no_days: holiday_diplayer(a, month % 13), relief=tk.FLAT, bg=color, fg='white')
      btn.grid(column=i % 7, row=calendar_row, padx=16, pady=7)
      no_days += 1
      if i % 7 == 6:
        calendar_row += 1
def destroyer(*fr):
  for i in fr:
    for child in i.winfo_children():
      child.destroy()

def next_or_following_month(NOF ,set_b = False,year1=0): 
  global current_year
  if not set_b:
    SNFM[0] = (SNFM[0]+1) if NOF else SNFM[0] -1
  elif set_b:
    SNFM[0] =0
    current_year = year1 
  PreviousBtn_StrVar.set(months[(SNFM[0]-1)%13])
  current_month_btn.configure(text= months[SNFM[0]%13])
  NextBtn_StrVar.set(months[(SNFM[0]+1)%13])
  if not set_b:
    general(current_year+SNFM[0]//13,SNFM[0])

def holiday_diplayer(day,m):
  lelit_calc(day, m)
  current_month_btn.configure(text = months[m] + " : " + str(day))
  destroyer(daily_holidays_frame)
 
  prl = []

  for k in range(11):
    if bh.tsome[k][0] == months[m] and bh.tsome[k][1] == day:
      
      lbl = tk.Label(daily_holidays_frame,text=f'{bh.Bealat[k][0]}',background=  ('#%02x%02x%02x')%(174,88,244),fg = 'white',font = 'Calibri 13 bold',width=23,height= 2)
      lbl.pack(pady=10)

  if months[m] in holidays.SH.keys():
    for er in holidays.SH[months[m]].keys():
      if er == day :
        for k in holidays.SH[months[m]][er]:
          lbl = tk.Label(daily_holidays_frame,text=f'{k}',bg=  ('#%02x%02x%02x')%(174,88,244),fg = 'white',font = 'Calibri 13 bold', width=23,height= 2)
          lbl.pack(pady=10)

  for i in holidays.YH[months[m]].keys(): 
    if i == day:
      for j in holidays.YH[months[m]][i]:
        lbl = tk.Label(daily_holidays_frame,text=f'{j}',fg='white' ,bg =  ('#%02x%02x%02x')%(174,88,244),font = 'Calibri 13 bold',width=23,height= 2)
        lbl.pack(pady=10)
        prl.append(j)
  for i in holidays.GH[day]:
    if i not in prl:
      lbl = tk.Label(daily_holidays_frame,text=f'{i}',background=('#%02x%02x%02x')%(233,233,233),fg = ('#%02x%02x%02x')%(174,88,244),font = 'Calibri 13 bold',width=23,height= 2)
      lbl.pack(pady=10)


# #********************************************************************************************************&&&&&&&&&&&&&&&&&&&&&&

def any_year_calculator(year1):
  SNFM[0] = 0
  button_disp()
  general(year1)

def bh_calculator(year):
  general(year)
  destroyer(calendar_frame)
  bh.general_cal(year)
#***************************************************************************************
  canvas = tk.Canvas(calendar_frame)
  canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

  scrollbar = tk.Scrollbar(calendar_frame, orient="vertical", command=canvas.yview)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

  canvas.configure(yscrollcommand=scrollbar.set, bg = "#02c39a")

  inner_frame = tk.Frame(canvas, bg = '#02c39a')
  inner_frame.configure(padx=240,pady=10)
  canvas.create_window((0, 0), window= inner_frame, anchor="nw")

  def configure_frame(event):
      canvas.configure(scrollregion=canvas.bbox("all"))

  inner_frame.bind("<Configure>", configure_frame)
#***************************************************************************************
  for i in range(20):
    L_amete_alem = tk.Label(inner_frame, bg="#02c39a",text =f'{holidays.Teaching_epi[i][0]} : {str(holidays.Teaching_epi[i][1])}', font = ("Arial", 13)).pack(pady=10)

def checker(T_entry, beal):

  def on_key_press(event):
      if T_entry.get() == '':
        T_entry.config(bg='white')
      elif T_entry.get() == str(beal[1]):
        T_entry.config(bg='green')
      else:
        T_entry.config(bg='red')
  return on_key_press


def Teacher():
  T_year = rd.randrange(1, 3001)
  frame_disp()

  any_year_calculator(T_year)
  general(T_year)
  global teacher_frame  # Declare teacher_frame as global if needed
  teacher_frame = tk.Frame(calendar_frame, width=0.7*screen_width, height=0.95*screen_height,bg= '#02c39a')
  teacher_frame.pack_propagate(False)
  destroyer(teacher_frame)

  teacher_frame.place(x=0, y=0)
  #*****************************************************************************************
  canvas = tk.Canvas(teacher_frame)
  canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

  scrollbar = tk.Scrollbar(teacher_frame, orient="vertical", command=canvas.yview)
  scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
  
  canvas.configure(yscrollcommand=scrollbar.set,bg= '#02c39a', bd = 30)

  inner_frame = tk.Frame(canvas)
  inner_frame.configure(padx=90,bg='#02c39a')
  canvas.create_window((30, 0), window=inner_frame, anchor="nw")

  def configure_frame(event):
      canvas.configure(scrollregion=canvas.bbox("all"))

  inner_frame.bind("<Configure>", configure_frame)
  #*****************************************************************************************
  lbl = tk.Label(inner_frame, width=10, bd=0, text=f'{T_year}', font=('Arial', 30),bg= '#02c39a')
  lbl.pack()

  for i in range(8):
      T_frame = tk.Frame(inner_frame,bg= '#02c39a')
      T_frame.pack()
      T_label = tk.Label(T_frame, height=2, text=f'{(holidays.Teaching_epi[i][0]).center(24," ")}', relief=tk.FLAT,bg= '#02c39a',font='Calibri 13 bold',bd=2)
      T_label.pack(side=tk.LEFT)
      if len(holidays.Teaching_epi[i]) == 3:
        var = tk.StringVar()
        var.set(None)

        x=  holidays.Teaching_epi[i][2]
        R1 = tk.Radiobutton(T_frame, text="ማቴዎስ", variable=var, value="ማቴዎስ", bg = "#02c39a",command=lambda: radio_checker(var,x,R1,R2,R3,R4),relief=tk.FLAT)
        R1.pack(side=tk.LEFT)
        R2 = tk.Radiobutton(T_frame, text="ማርቆስ", variable=var, value="ማርቆስ", bg = "#02c39a", command=lambda: radio_checker(var,x,R2,R1,R3,R4),relief=tk.FLAT)
        R2.pack(side=tk.LEFT)

        R3 = tk.Radiobutton(T_frame, text="ሉቃስ", variable=var, value="ሉቃስ", bg = "#02c39a", command=lambda: radio_checker(var,x,R3,R2,R1,R4),relief=tk.FLAT)
        R3.pack(side=tk.LEFT)
        R4 = tk.Radiobutton(T_frame, text="ዮሐንስ", variable=var, value="ዮሐንስ", bg = "#02c39a", command=lambda: radio_checker(var,x,R4,R2,R3,R1),relief=tk.FLAT)
        R4.pack(side=tk.LEFT)

      else:
        T_entry = tk.Entry(T_frame, bg='white')
        T_entry.pack(side=tk.LEFT)
        T_entry.bind('<FocusOut>', checker(T_entry, holidays.Teaching_epi[i]))
        T_entry.bind('<Return>', checker(T_entry, holidays.Teaching_epi[i]))

  for i in range(8, 20):
      T_frame = tk.Frame(inner_frame, bg= '#02c39a')
      T_frame.pack()
      T_label = tk.Label(T_frame, height=2, text=f'{holidays.Teaching_epi[i][0].center(24," ")}', relief=tk.FLAT,bg='#02c39a',font='Calibri 13 bold')
      T_label.pack(side=tk.LEFT)
      T_entry = tk.Entry(T_frame, bg='white')
      T_entry.pack(side=tk.LEFT)

      T_entry.bind('<FocusOut>', checker(T_entry, holidays.Teaching_epi[i]))

def entry_displayer(button_name):
  try:
    destroyer(teacher_frame)
    teacher_frame.destroy()
  except:
    pass
  frame_disp()

  global year_entry
  pop_up = tk.Toplevel(calendar_days_frame)
  pop_up.geometry('250x80')
  pop_up.title('Enter a year')
  year_entry = tk.Entry(pop_up, width=60)
  year_entry.pack(padx=20)
  btn = tk.Button(pop_up, text="Calculate", padx=10, pady=5)
  btn.pack()

  if button_name == "b1" :
      btn.config(command=lambda: any_year_calculator(int(year_entry.get())))
      year_entry.bind('<Return>', lambda event:any_year_calculator(int(year_entry.get())))
  elif button_name == "b2" :
      btn.config(command=lambda:bh_calculator(int(year_entry.get())))
      year_entry.bind('<Return>', lambda event:bh_calculator(int(year_entry.get())))


  
def ham_displayer():
  destroyer(daily_holidays_frame)
  b1 = tk.Button(daily_holidays_frame,text='Year',background='#00cccc',fg = ('#%02x%02x%02x')%(113,57,158),font = 'Calibri 13 bold',width=15,height= 2, relief="flat", command= lambda: entry_displayer("b1")).pack(pady = 6)
  b2 = tk.Button(daily_holidays_frame,text='BH calculator',background='#00cccc',fg = ('#%02x%02x%02x')%(113,57,158),font = 'Calibri 13 bold',width=15,height= 2, relief="flat", command=lambda: entry_displayer("b2")).pack(pady = 6)
  b3 = tk.Button(daily_holidays_frame,text='Exercise',background='#00cccc',fg = ('#%02x%02x%02x')%(113,57,158),font = 'Calibri 13 bold',width=15,height= 2, relief="flat",command=Teacher).pack(pady = 6)
  b4 = tk.Button(daily_holidays_frame,text='Moon Phase',background='#00cccc',fg = ('#%02x%02x%02x')%(113,57,158),font = 'Calibri 13 bold',width=15,height= 2, relief="flat", command = moon_phase_calc).pack(pady = 6)
  b5 = tk.Button(daily_holidays_frame,text='Eclipse',background='#00cccc',fg = ('#%02x%02x%02x')%(113,57,158),font = 'Calibri 13 bold',width=15,height= 2, relief="flat", command = eclipse).pack(pady = 6)
  

def button_disp():
  #next month buttons
  global NextBtn_StrVar
  global PreviousBtn_StrVar
  global CurrentBtn_StrVar
  global current_month_btn
  global previous_month_btn
  global next_month_btn
  NextBtn_StrVar = tk.StringVar()
  PreviousBtn_StrVar  = tk.StringVar()
  CurrentBtn_StrVar = tk.StringVar()

  PreviousBtn_StrVar.set(months[(SNFM[0]-1)%13])
  NextBtn_StrVar.set(months[(SNFM[0]+1)%13])

  previous_month_btn = tk.Button(control_frame,fg='white' ,bg='#00a896',bd=0,width=15, height=3,command= lambda : next_or_following_month(0), textvariable=PreviousBtn_StrVar,)
  previous_month_btn.place(x=10,y=0,anchor=tk.NW)

  current_month_btn = tk.Label(control_frame,fg='white',bg= '#00a896',bd = 0,width= 15,height=3,text= months[SNFM[0]%13])
  current_month_btn.place(x =(0.75*screen_width)*0.5,y = 20 ,anchor = tk.CENTER)

  next_month_btn = tk.Button(control_frame,fg='white' ,bg='#00a896',bd=0,width=15, height=3,command= lambda:next_or_following_month(1),textvariable=NextBtn_StrVar)
  next_month_btn.place(x=480,y=0,anchor=tk.NW)

def frame_disp():
  global calendar_days_frame
  global control_frame
  destroyer(calendar_frame)
  calendar_days_frame = tk.Frame(calendar_frame,bg='#02c39a',width=0.75*screen_width,height=0.8*screen_height)
  calendar_days_frame.pack(fill = tk.BOTH,expand=1)

  control_frame = tk.Frame(calendar_frame,width=0.75*screen_width,height=0.12*screen_height,bg='#02c39A')
  control_frame.pack()

# ##########################################******calling******

general(current_year ,SNFM[0])

############################********hamburger-menu
ham_icon = tk.PhotoImage(file = r'ham.png')
hamburger_menu = tk.Button(menu_frame,width=30,height=32, bg = "#052659",relief="flat",image=ham_icon, command=ham_displayer)
hamburger_menu.pack(side = tk.RIGHT, pady=5, padx=15)

button_disp()

root.mainloop()



