rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random ;
y=int(input("what do you choose ? type 0 for rock , 1 for paper or 2 for scissors \n"))
if y>=3 or y<0:
  print("you typed an invalid number , you lose")
else : 
    l=[rock,paper,scissors]
    x=random.randint(0,2)
    print (f"computure choose :{l[x]} ")
    print (f"you choose : {l[y]}")
    if y==0 and x==2:
      print ("you win ! ")
    elif y==2 and x==0:
      print ("you lose ! ")
    elif y>x :
      print ("you win !")
    elif x>y :
      print("you lose ! ")
    elif y==x:
      print("it's a draw ")
  


