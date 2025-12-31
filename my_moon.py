def jd_calc(year, month, day):
  if month <= 2:
      year -= 1
      month += 12

  a = year // 100
  b = 2 - a + (a // 4)
  y = year + 4716
  m = month + 1
  global julian_day
  julian_day = int(365.25 * y) + int(30.6001 * m) + day + b - 1524.5
  
def moon_age_function(year, month, day):
  jd_calc(year, month, day)
  days_since_epoch = julian_day
  global moon_age
  moon_age = days_since_epoch % 29.53058867

def moon_phase(year, month, day):
  moon_age_function(year, month, day)
  if moon_age >= 0 and moon_age < 1.84566:
   return "New Moon"
  elif moon_age >= 1.84566 and moon_age < 5.53699:
    return "Waxing Crescent"
  elif moon_age >= 5.53699 and moon_age < 9.22831:
    return "First Quarter"
  elif moon_age >= 9.22831 and moon_age < 12.91963:
    return "Waxing Gibbous"
  elif moon_age >= 12.91963 and moon_age < 16.61096:
    return "Full Moon"
  elif moon_age >= 16.61096 and moon_age < 20.30228:
    return "Waning Gibbous"
  elif moon_age >= 20.30228 and moon_age < 23.99361:
    return "Last Quarter"
  elif moon_age >= 23.99361 and moon_age < 27.68493:
    return "Waning Crescent"
  elif moon_age >= 27.68493 and moon_age < 29.53058867:
    return "New Moon"


