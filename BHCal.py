#Vaiables
days = ["ሰኞ", "ማክሰኞ", "ረቡዕ", "ሀሙስ", "አርብ", "ቅዳሜ", "እሁድ"]
months = ["ጥር", "የካቲት", "መጋቢት", "ሚያዝያ", "ግንቦት", "ሰኔ", "ሐምሌ", "ነሐሴ", "ጳጉሜ"]

wengel = ["ዮሐንስ", "ማቴዎስ", "ማርቆስ", "ሉቃስ"]

MebajaHammer_day = ['አርብ','ሀሙስ','ረቡዕ','ማክሰኞ','ሰኞ','እሁድ','ቅዳሜ']

Bealat =  [
	[ "አቢይ-ጾም","14","Monday" ],[ "ደብረ-ዘይት","41","Sunday" ],[ "ሆሳእና","62","Sunday" ],[ "ስቅለት","67","Friday" ],[ "ትንሳኤ","69","Sunday" ],[ "ርክበ-ካህናት","93","Wednesday" ],[ "እርገት","108","Thursday" ],[ "ጰራቅሊጦስ","118","Sunday" ],[ "ጾመ-ሐዋርያት","119","Monday" ],[ "ጾመ-ድህርነት","121","Wedensday" ],['ነነዌ']

]

tsome = []
amete_alem = 0 
metene_rabit = 0
mebacha_index = 0

#calculations
def tsome_shower(Bealat,tsome):
  tsome_num = Modified_mebaja_hammer + int(Bealat[1])
  after_month = tsome_num // 30
  if tsome_num % 30 == 0:
    tsome.append([months[months.index(Nenewe_month) + after_month - 1], 30])
  else:
    tsome.append([months[months.index(Nenewe_month)+after_month], tsome_num % 30])
  return tsome

def general_cal(year):
  global metene_rabit
  global mebacha_index
  global amete_alem
  amete_alem = 5500 + year

  metene_rabit = amete_alem // 4
  mebacha_index = (amete_alem + metene_rabit) % 7


  global mebacha 
  mebacha = days[mebacha_index]

  global Wengelawi_name
  Wengelawi_name = wengel[amete_alem%4]

  global medeb
  medeb = amete_alem % 19
  global wenber
  wenber = medeb - 1 if medeb != 0 else 18

  global metqi
  metqi = (19 * wenber) % 30 if wenber != 0 else 30
  global abekte
  abekte = (11 * wenber) % 30 if wenber != 0  else 0

  if metqi >= 2 and metqi < 14:
    val =  (days.index(mebacha) + 30 + metqi -1)%7
  elif metqi > 14 and metqi <= 30:
    val = (days.index(mebacha)+ metqi -1 )%7

  global MebajaHammer
  global Modified_mebaja_hammer
  MebajaHammer = (MebajaHammer_day.index(days[val]) + metqi +2)
  Modified_mebaja_hammer = MebajaHammer %30

  global Nenewe_var
  global Nenewe_month
  Nenewe_month = months[0 + MebajaHammer//31] if (metqi > 14 and metqi <=30) else months[1]
  Nenewe_var = Nenewe_month + ' '+ str(MebajaHammer%31)

  for i in range(10):
    tsome_shower(Bealat[i],tsome)
  if MebajaHammer > 30:
    MebajaHammer %= 30
  tsome.append([Nenewe_month,MebajaHammer])

