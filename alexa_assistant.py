def detect_alexa(text):
  words = text.split()
  count = words.count('alexa'.lower())
  

  if count > 1:
      return "Just say Alexa one time please"
  elif count ==1:
      return "Wow, you just said my name"
  else:
      return "Alexa was not detected in your text, please try entering another text that contains the word Alexa"

writing = input("Enter your text please: ")
result = detect_alexa(writing.lower())
print(result)
