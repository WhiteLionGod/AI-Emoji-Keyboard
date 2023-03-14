while True:
  message = input("Enter Your Message: ")
  
  def emoji_converter(message):
    message = message.split()
    emojis = {
      "happy": "😊",
      "lol" : "😂",
      "sick":"🤒"
    }
    output = ""
    for word in message:
      output+= emojis.get(word,word) + " "
    return(output)
  
  print(emoji_converter(message))