#5 Bahşiş Hesaplama 
  def dollars_to_float(d):
      return float(d.replace("$", ""))
 
  def percent_to_float(p):
      return float(p.replace("%", "")) / 100
 
  meal = input("Yemek ne kadardı? ")
  tip = input("Yüzde kaç bahşiş? ")
 
  meal = dollars_to_float(meal)
  tip = percent_to_float(tip)
 
  tip_amount = meal * tip
 
  print(f"Bahşiş: ${tip_amount:.2f}")


