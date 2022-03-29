import random
import time 

#introduction
print("Hi! Here is the place where I recommend a great book for you to read.")
print("Get ready to find your next favourite book!")
print("*********************************************")
print("What genre of book do you want to read?")

#asking for inputs
genre = input("Romance, mystery, or fantasy? ")
readingspeed = int(input("Approximately how many pages of a novel can you read in 1 hour?"))

#lists of book recommendations and their number of pages
rbook1 = ["The Notebook by Nicholas Sparks",214]
rbook2 = ["It Ends With Us by Colleen Hoover",384]
rbook3 = ["Punk 57 by Penelope Douglas",342]
rbook4 = ["The Deal by Elle Kennedy",376]

mbook1 = ["Murder on the Orient Express by Agatha Christie",256]
mbook2 = ["The Girl on the Train by Paula Hawkins",317]
mbook3 = ["The Guest List by Lucy Foley", 320]
mbook4 = ["The Girl with the Dragon Tattoo by Stieg Larsson",672]

fbook1 = ["The Name of the Wind by Patrick Rothfuss", 662]
fbook2 = ["Throne of Glass by Sarah J. Mass", 416]
fbook3 = ["Six of Crows by Leigh Bardugo",465]
fbook4 = ["The Fifth Season by N.K. Jemsin",512]

#lists of books by genre
romancebooks = [rbook1, rbook2,rbook3,rbook4]
mysterybooks = [mbook1, mbook2, mbook3, mbook4]
fantasybooks = [fbook1, fbook2,fbook3,fbook4]

#finding a book recommendation
if genre == "romance" or genre == "Romance":
  random = (random.choice(romancebooks)) #randomly choosing a list which contains the title of a book and the number of pages
  bookrec = random[0] #taking the title of the book which is the first item in the list
  readinghours = random[1]/readingspeed #finding the number of hours it would take to finish the book using the second item in the list: the number of pages
  readinghoursrounded = round(readinghours) #rounding  up or down to a whole number
  
  if random == rbook2: #my favourite book is rbook2
    print("I like you, so I will recommend you my favourite book!")

elif genre == "mystery" or genre == "Mystery":
  random = (random.choice(mysterybooks))
  bookrec = random[0] 
  readinghours = random[1]/readingspeed
  readinghoursrounded = round(readinghours) 

else:
  random = (random.choice(fantasybooks))
  bookrec = random[0]
  readinghours = random[1]/readingspeed
  readinghoursrounded = round(readinghours)

print("")
print("You asked for", genre,"so you should read...")
time.sleep(1)
print(bookrec+"!")
time.sleep(1.5)

#so if the person is a fast reader, it will not tell them the book will take 0 hours to read
if readinghoursrounded == 0:
  print("It will take you less than an hour to read.")

else:
  print("It will take you approximately",readinghoursrounded,"hour(s) to read.")

time.sleep(1.5)
print("Have fun!")