emoji = {
    ":)" : "😊",
    ":(" : "😞"
     }

statement = input("statement: ")
message = statement.split(' ')
output = "" 
for word in message:
    output += emoji.get(word, word) + " "
print(output)
    
