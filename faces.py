#3 İfade Dönüştürme
 def convert(text):
      text = text.replace(":)", "🙂")
      text = text.replace(":(", "🙁")
      return text
 
 def main():
      text = input("Metin girin: ")
      print(convert(text))

  main()

