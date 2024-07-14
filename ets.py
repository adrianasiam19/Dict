 # dictionary trywork
glossaries= {
   'variables' : 'represented by letters', 
   'functions' : 'to store a group of statements',
   'loops' : 'representing cycles',
   'lists' : 'to store data',
   'dictionary' : 'to store values '
}

for word, meaning in glossaries.items(): 
   print(f"\n{word}: {meaning}")

Engineering_Programmes = {
   'Nicole': 'Computer engineering',
   'Ama' : 'Biomedical engineering',
   'Adwoa': 'Electrical Engineering',
   'John' : 'Marine Engineering'
}
for name, programmes in Engineering_Programmes.items():
   print(f"{name.title()} is a student of the {programmes.title()} department.") 

favoruite_language = {
   'Jonathan': 'Python',
   'Nana Kwame' : 'C',
   'Asiamah' : 'Java',
   'Okyere' : 'C ++'
}
friends = ['Nana kwame','Okyere']
for name in favoruite_language.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
       language = favoruite_language[name].title()
       print(f"\t{name.title()},I see you love {language}!")
   



       # Midsem
       message = input("Tell me something, and i will repeat it back to you:")
       print(message)
       prompt = "If you share your name, we can personlize the messages you see."
       prompt += "\nwhat is your first name?"
       name = input(prompt)
       print(f"\nHello,{name}")(())

       height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")