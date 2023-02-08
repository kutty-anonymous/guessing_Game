import random
with open('animals.txt','r') as f:
    animals=f.read().split()
    animal=random.choice(animals).lower()
    life=len(animal)*2
    guess=list()
    for i in range(len(animal)):
        guess.append("?")
    finish=0
    print("\t\t\t\t\tWellcome Guessing words game\n\t\t\t\t\t--------------------")
    print(animal)
heart=u'\u2764'
def check(letter,animal,guess,count):
    index=0
    while index < len(animal):
        if letter in animal[index]:
            if letter !=guess[index]:
                guess[index]=letter
                count=count+1
            else:
                break    
        index=index+1
    return count
count=0

while life > 0:
    print("\n",guess)
    print(" heart ", life ," ",(heart+" ")*life)
    while True:
        letter=str(input("\n Enter One Letter : "))

        if len(letter)==1:
            break
        else:
            print("only one letter.\n")
    if letter in animal:
        count=check(letter,animal,guess,count)

    else:
        print("\nincorrect. You lose a heart")
        life=life-1

    if count==len(animal):
        finish=1

    elif life==0:
        finish=2   

    elif life==len(animal):
        i=0;
        print("\n You lose Half hearts so i give some words")
        while i<len(animal)-1:
            guess[i]=animal[i]
            i=i+2


    if finish==1:
        print("You Win... lossing List is " , len(animal)*2 - life)
        while True:
            enter=input("\n--------------------\n 1 . play next Match\n 2. Exit \n ")
            if enter=='1':
                animal=random.choice(animals).lower()
                count=0
                life=len(animal)*2
                guess=list()
                for i in range(len(animal)):
                    guess.append('?')
                print(animal)
                finish=0
                break

            elif enter=='2':
                finish=2
                break;   

            else:
                print("only 1 or 2")     

    elif finish==2:
        print("\n---------------------\nYou lossing All hearts\n")
        while True:
            enter=input(" 1 . Try This Word\n 2.Next Game \n 3.exit\n ")
            if enter =='1':
                guess=list()
                for i in range(len(animal)):
                    guess.append("?")
                count=0;
                life=len(animal)*2
                finish=0;
                break

            elif enter=='2':
                animal=random.choice(animals).lower()
                life=len(animal)*2
                count=0;
                guess=list()
                for i in range(len(animal)):
                  guess.append('?')
                finish=0
                break

            elif enter=='3':
                finish=2
                break

            else:
                print("Try again Number Invalid.\n")


    if finish==2:
        print("\nTHANK YOU")
        break


