"""
Name(s): Harrison Zhang
Name of Project: BOMBNERY: Kiosk #017

IMPORTANT NOTE: The repl says its coded in Bash (it's not) - I couldn't find a way to fix it but it is still in Python!

"""

price = 0
more = ""

def coffee():
  global order
  global size
  print()
  print("All of our coffee drinks come in two sizes: Medium (M) and Large (L).")
  print()
  print("A1. Americano (Hot/Cold):")
  print("M: $2.50")
  print("L: $3.25")
  print()
  print("A2. Latte (Hot/Cold):")
  print("M: $3.50")
  print("L: $4.50")
  print()
  print("A3. Caramel Latte (Hot/Cold):")
  print("M: $3.75")
  print("L: $5.00")
  print()
  print("A4. Mocha (Hot/Cold):")
  print("M: $4.00")
  print("L: $5.00")
  print()
  print("A5. Cappuccino (Hot/Cold):")
  print("M: $3.50")
  print("L: $4.55")
  print()
  order = input("Please enter the code of the drink you would like to order (ex. A1 for an Americano): ")
  order = order.upper()
  while order != "A1" and order != "A2" and order != "A3" and order != "A4" and order != "A5":
    print()
    order = input("Sorry, this is not a valid option. Please enter the number of the drink you would like to order: ")
    order = order.upper()
  print()
  size = input("Please enter M for a medium-sized drink and L for a large-sized drink: ")
  size = size.upper()
  while size != "M" and size != "L":
    print()
    size = input("Sorry, this is not a valid option. Please enter M for a medium-sized drink and L for a large-sized drink: ")
    size = size.upper()
  if size == "M" or size == "L":
    priceA()

def priceA():
  global price
  if order == "A1":
    if size == "M":
      price += 2.50
      heat()
    elif size == "L":
      price += 3.25
      heat()  
  elif order == "A2":
    if size == "M":
      price += 3.50
      heat()  
    elif size == "L":
      price += 4.50
      heat()     
  elif order == "A3":
    if size == "M":
      price += 3.75
      heat()    
    elif size == "L":
      price += 5.00
      heat()   
  elif order == "A4":
    if size == "M":
      price += 4.00
      heat()  
    elif size == "L":
      price += 5.00
      heat()
  elif order == "A5":
    if size == "M":
      price += 3.50
      heat()
    elif size == "L":
      price += 4.50
      heat()

def classictea():
  global order
  global size
  print()
  print("All of our classic tea drinks come in two sizes: Medium (M) and Large (L).")
  print()
  print("B1. Black Tea (Hot/Cold):")
  print("M: $3.00")
  print("L: $3.75")
  print()
  print("B2. Chai Tea (Hot/Cold):")
  print("M: $3.00")
  print("L: $3.75")
  print()
  print("B3. Green Tea (Hot/Cold):")
  print("M: $3.00")
  print("L: $3.75")
  print()
  print("B4. Jasmine Tea (Hot/Cold):")
  print("M: $3.00")
  print("L: $3.75")
  print()
  print("B5. Oolong Tea (Hot/Cold):")
  print("M: $3.00")
  print("L: $3.75")
  print()
  print("B6. Earl Grey Tea (Hot/Cold):")
  print("M: $3.00")
  print("L: $3.75")
  print()
  order = input("Please enter the code of the drink you would like to order (ex. B1 for a Black Tea): ")
  order = order.upper()
  while order != "B1" and order != "B2" and order != "B3" and order != "B4" and order != "B5" and order != "B6":
    print()
    order = input("Sorry, this is not a valid option. Please enter the number of the drink you would like to order: ")
    order = order.upper()
  print()
  size = input("Please enter M for a medium-sized drink and L for a large-sized drink: ")
  size = size.upper()
  while size != "M" and size != "L":
    print()
    size = input("Sorry, this is not a valid option. Please enter M for a medium-sized drink and L for a large-sized drink: ")
    size = size.upper()
  if size == "M" or size == "L":
    priceB()

def priceB():
  global price
  if order == "B1":
    if size == "M":
      price += 3.00
      heat()
    elif size == "L":
      price += 3.75
      heat()  
  elif order == "B2":
    if size == "M":
      price += 3.00
      heat()  
    elif size == "L":
      price += 3.75
      heat()     
  elif order == "B3":
    if size == "M":
      price += 3.00
      heat()    
    elif size == "L":
      price += 3.75
      heat()   
  elif order == "B4":
    if size == "M":
      price += 3.00
      heat()  
    elif size == "L":
      price += 3.75
      heat()
  elif order == "B5":
    if size == "M":
      price += 3.00
      heat()
    elif size == "L":
      price += 3.75
      heat()
  elif order == "B6":
    if size == "M":
      price += 3.00
      heat()
    elif size == "L":
      price += 3.75
      heat()

def milktea():
  global order
  global size
  print()
  print("All of our milk tea drinks come in two sizes: Medium (M) and Large (L).")
  print()
  print("C1. Black Milk Tea (Hot/Cold):")
  print("M: $4.00")
  print("L: $5.00")
  print()
  print("C2. Black Sugar Milk Tea (Hot/Cold):")
  print("M: $4.75")
  print("L: $5.75")
  print()
  print("C3. Honey Milk Tea (Hot/Cold):")
  print("M: $4.25")
  print("L: $5.25")
  print()
  print("C4. Matcha Milk Tea (Hot/Cold):")
  print("M: $4.00")
  print("L: $5.00")
  print()
  print("C5. Honey Matcha Milk Tea (Hot/Cold):")
  print("M: $4.25")
  print("L: $5.25")
  print()
  print("C6. Taro Milk Tea (Hot/Cold):")
  print("M: $4.50")
  print("L: $5.50")
  print()
  print("C7. Coffee Milk Tea (Hot/Cold):")
  print("M: $4.50")
  print("L: $5.50")
  print()
  print("C8. Thai Milk Tea (Hot/Cold):")
  print("M: $4.75")
  print("L: $5.75")
  print()
  order = input("Please enter the code of the drink you would like to order (ex. C1 for a Black Milk Tea): ")
  order = order.upper()
  while order != "C1" and order != "C2" and order != "C3" and order != "C4" and order != "C5" and order != "C6" and order != "C7" and order != "C8":
    print()
    order = input("Sorry, this is not a valid option. Please enter the number of the drink you would like to order: ")
    order = order.upper()
  print()
  size = input("Please enter M for a medium-sized drink and L for a large-sized drink: ")
  size = size.upper()
  while size != "M" and size != "L":
    print()
    size = input("Sorry, this is not a valid option. Please enter M for a medium-sized drink and L for a large-sized drink: ")
    size = size.upper()
  if size == "M" or size == "L":
    priceC()

def priceC():
  global price
  if order == "C1":
    if size == "M":
      price += 4.00
      heat()
    elif size == "L":
      price += 5.00
      heat()  
  elif order == "C2":
    if size == "M":
      price += 4.75
      heat()  
    elif size == "L":
      price += 5.75
      heat()     
  elif order == "C3":
    if size == "M":
      price += 4.25
      heat()    
    elif size == "L":
      price += 5.25
      heat()   
  elif order == "C4":
    if size == "M":
      price += 4.00
      heat()  
    elif size == "L":
      price += 5.00
      heat()
  elif order == "C5":
    if size == "M":
      price += 4.25
      heat()
    elif size == "L":
      price += 5.25
      heat()
  elif order == "C6":
    if size == "M":
      price += 4.50
      heat()
    elif size == "L":
      price += 5.50
      heat()
  elif order == "C7":
    if size == "M":
      price += 4.50
      heat()
    elif size == "L":
      price += 5.50
      heat()
  elif order == "C8":
    if size == "M":
      price += 4.75
      heat()
    elif size == "L":
      price += 5.75
      heat()

def fruittea():
  global price
  print()
  print("BOMBNERY uses a choose-your-own system for our fruit teas. All of our fruit teas are $4 for a medium and $5 for a large, and are all cold. To order a fruit tea, first select a fruit base.")
  print()
  print("Available fruit bases: Strawberry, Mango, Passion Fruit, Lychee, Blueberry, Kiwi, Lemon, Peach, Pineapple")
  print()
  fruitbase = input("Please input the fruit base you would like (ex. Strawberry): ")
  fruitbase = fruitbase.lower()
  while fruitbase != "strawberry" and fruitbase != "mango" and fruitbase != "passion fruit" and fruitbase != "lychee" and fruitbase != "kiwi" and fruitbase != "lemon" and fruitbase != "peach" and fruitbase != "pineapple":
    print()
    fruitbase = input("Sorry, this is not a valid option. Please enter the fruit base you would like to order: ")
    fruitbase = fruitbase.lower()
  print()
  print("Available tea bases: Black, Jasmine, Oolong, Earl Grey")
  print()
  teabase = input("Please input the tea base you would like (ex. Black): ")
  teabase = teabase.lower()
  while teabase != "black" and teabase != "jasmine" and teabase != "oolong" and teabase != "earl grey":
    print()
    teabase = input("Sorry, this is not a valid option. Please enter the tea base you would like to order: ")
    teabase = teabase.lower()
  print()
  size = input("Please enter M for a medium-sized drink and L for a large-sized drink: ")
  size = size.upper()
  while size != "M" and size != "L":
    print()
    size = input("Sorry, this is not a valid option. Please enter M for a medium-sized drink and L for a large-sized drink: ")
    size = size.upper()
  if size == "M":
    price += 4.00
    toppings()
  elif size == "L":
    price += 5.00
    toppings()

def slush():
  global order
  print()
  print("All of our slush drinks only come in one size: Large (L).")
  print()
  print("E1. Taro Slush (Cold):")
  print("L: $5.50")
  print()
  print("E2. Coconut Slush (Cold):")
  print("L: $5.50")
  print()
  print("E3. Mango Slush (Cold):")
  print("L: $5.50")
  print()
  print("E4. Strawberry Slush (Cold):")
  print("L: $5.50")
  print()
  print("E5. Mint Slush (Cold):")
  print("L: $5.50")
  print()
  print("E6. Matcha Slush (Cold):")
  print("L: $5.50")
  print()
  print("E7. Peach Slush (Cold):")
  print("L: $5.50")
  print()
  print("E8. Pineapple Slush (Cold):")
  print("L: $5.50")
  print()
  print("E9. Yogurt Slush (Cold):")
  print("L: $5.50")
  print()
  print("E10. Red Bean Slush (Cold):")
  print("L: $5.50")
  print()
  print("E11. Strawberry Yogurt Slush (Cold):")
  print("L: $6.50")
  print()
  print("E12. Mint Chocolate Slush (Cold):")
  print("L: $6.50")
  print()
  print("E13. Coconut Coffee Slush (Cold):")
  print("L: $6.50")
  print()
  order = input("Please enter the code of the drink you would like to order (ex. E1 for a Taro Slush): ")
  order = order.upper()
  while order != "E1" and order != "E2" and order != "E3" and order != "E4" and order != "E5" and order != "E6" and order != "E7" and order != "E8" and order != "E9" and order != "E10" and order != "E11" and order != "E12" and order != "E13":
    print()
    order = input("Sorry, this is not a valid option. Please enter the number of the drink you would like to order: ")
    order = order.upper()
  priceE()

def priceE():
  global price
  if order == "E1":
    price += 5.50
    toppings()
  elif order == "E2":
    price += 5.50
    toppings()
  elif order == "E3":
    price += 5.50
    toppings()
  elif order == "E4":
    price += 5.50
    toppings()
  elif order == "E5":
    price += 5.50
    toppings()
  elif order == "E6":
    price += 5.50
    toppings() 
  elif order == "E7":
    price += 5.50
    toppings()
  elif order == "E8":
    price += 5.50
    toppings()
  elif order == "E9":
    price += 5.50
    toppings()
  elif order == "E10":
    price += 5.50
    toppings()
  elif order == "E11":
    price += 6.50
    toppings()
  elif order == "E12":
    price += 6.50
    toppings()   
  elif order == "E13":
    price += 6.50
    toppings()

def dessert():
  global orderF
  global qty
  print()
  print("F1. Macarons (set of 4): $4.00")
  print("Available flavors: Chocolate, Thai Tea, Matcha, Strawberry")
  print()
  print("F2. Ice Cream:")
  print("2 Scoops: $3.00")
  print("3 Scoops: $4.00")
  print("Available flavors: Vanilla, Chocolate, Thai Tea, Matcha, Strawberry, Taro, Coffee")
  print()
  print("F3. Crepe Cake:")
  print("1 Slice: $2.00")
  print("8 Slices: $12.00")
  print("Available flavors: Vanilla, Chocolate, Matcha")
  print()
  orderF = input("Please enter the code of the dessert you would like to order (ex. F1 for a set of macarons): ")
  orderF = orderF.upper()
  while orderF != "F1" and orderF != "F2" and orderF != "F3":
    print()
    orderF = input("Sorry, this is not a valid option. Please enter the number of the drink you would like to order: ")
    orderF = orderF.upper()
  if orderF == "F1":
    print()
    macaron = input("Please enter the macaron flavor you would like (ex. Chocolate): ")
    macaron = macaron.lower()
    while macaron != "chocolate" and macaron != "thai tea" and macaron != "matcha" and macaron != "strawberry":
      print()
      macaron = input("Sorry, this is not a valid option. Please enter the macaron flavor you would like to order: ")
      macaron = macaron.lower()
    priceF()
  elif orderF == "F2":
    print()
    icecream = input("Please enter the ice cream flavor you would like (ex. Vanilla): ")
    icecream = icecream.lower()
    while icecream != "vanilla" and icecream != "chocolate" and icecream != "thai tea" and icecream != "matcha" and icecream != "strawberry" and icecream != "taro" and icecream != "coffee":
      print()
      icecream = input("Sorry, this is not a valid option. Please enter the ice cream flavor you would like to order: ")
      icecream = icecream.lower()
    qty = input("Please enter 2 to order two scoops and 3 to order 3 scoops: ")
    while qty != "2" and qty != "3":
      print()
      qty = input("Sorry, this is not a valid option. Please enter 2 to order two scoops and 3 to order 3 scoops: ")
    priceF()
  elif orderF == "F3":
    print()
    crepe = input("Please enter the crepe cake flavor you would like (ex. Vanilla): ")
    crepe = crepe.lower()
    while crepe != "vanilla" and crepe != "chocolate" and crepe != "matcha":
      print()
      crepe = input("Sorry, this is not a valid option. Please enter the crepe cake flavor you would like to order: ")
      crepe = crepe.lower()
    qty = input("Please enter 1 to order one slice and 8 to order 8 slices: ")
    while qty != "1" and qty != "8":
      print()
      qty = input("Sorry, this is not a valid option. Please enter 2 to order two scoops and 3 to order 3 scoops: ")
    priceF()  

def priceF():
  global price
  if orderF == "F1":
    price += 4.00
    final()
  elif orderF == "F2":
    if qty == "2":
      price += 3.00
      final()
    elif qty == "3":
      price += 4.00
      final()
  elif orderF == "F3":
    if qty == "1":
      price += 2.00
      final()
    elif qty == "2":
      price += 12.00
      final()

def promo():
  global orderG
  global size
  print()
  print("Our promotional section currently features 4 drinks and 1 dessert.")
  print()
  print("G1. Mint Milk Tea (Hot/Cold):")
  print("M: $4.50")
  print("L: $5.50")
  print()
  print("G2. Dalgona Milk Tea (Hot/Cold):")
  print("M: $4.50")
  print("L: $5.50")
  print()
  print("G3. Purple Yam (Ube) Milk Tea (Hot/Cold):")
  print("M: $4.50")
  print("L: $5.50")
  print()
  print("G4. Ube Slush (Cold):")
  print("L: $5.50")
  print()
  print("G5. Halo-Halo: $8.50")
  print("Halo-halo, Filipino for \"mixed\", is a Filipino dessert made up of layers of shaved ice and condensed milk topped with an assortment of chewy, crunchy, and creamy ingredients. We top ours with a scoop of our semi-sweet taro ice cream.")
  print()
  orderG = input("Please enter the code of the item you would like to order (ex. G1 for Mint Milk Tea): ")
  orderG = orderG.upper()
  while orderG != "G1" and orderG != "G2" and orderG != "G3" and orderG != "G4" and orderG != "G5":
    print()
    orderG = input("Sorry, this is not a valid option. Please enter the number of the drink you would like to order: ")
    orderG = orderG.upper()
  if orderG == "G1" or orderG == "G2" or orderG == "G3":
    print()
    size = input("Please enter M for a medium-sized drink and L for a large-sized drink: ")
    size = size.upper()
    while size != "M" and size != "L":
      print()
      size = input("Sorry, this is not a valid option. Please enter M for a medium-sized drink and L for a large-sized drink: ")
      size = size.upper()
    if size == "M" or size == "L":
      priceG()
  elif orderG == "G4" or orderG == "G5":
    priceG()

def priceG():
  global price
  if orderG == "G1":
    if size == "M":
      price += 4.50
      heat()
    elif size == "L":
      price +=  5.50
      heat()
  elif orderG == "G2":
    if size == "M":
      price += 4.50
      heat()
    elif size == "L":
      price += 5.50
      heat()
  elif orderG == "G3":
    if size == "M":
      price += 4.50
      heat()
    elif size == "L":
      price += 5.50
      heat()
  elif orderG == "G4":
    price += 5.50
    toppings()
  elif orderG == "G5":
    price += 8.50
    final()

def blurb():
  print()
  print("Welcome to BOMBNERY, the minimalist, all-natural cafe bringing refreshing flavors to Hunter’s doorstep. Our business’s name comes from the Korean words 봄 and 누리, phonetically bomnuri, which together mean spring world. We aspire to insert this spring world in each cup of tea and coffee we make, creating a warm and welcoming environment for our customers in every sip. We promise to deliver a variety of all natural, non-GMO drinks containing only the best ingredients from our suppliers. Through our menu, we hope you are able to experience memories of a comforting breeze that wraps around you, and bring these stories to your loved ones.")
  print()
  back = input("Enter MAIN to return to the main menu: ")
  back = back.upper()
  while back != "MAIN":
    print("Sorry, this is not a valid option.")
    back = input("Enter MAIN to return to the main menu: ")
    back = back.upper()
  main()

def heat():
  print()
  global heat
  heat = input("Please enter H for a hot drink and C for a cold drink: ")
  heat = heat.upper()
  while heat != "H" and heat != "C":
    print()
    heat = input("Sorry, this is not a valid option. Please enter H for a hot drink and C for a cold drink: ")
    heat = heat.upper()
  toppings()

def toppings():
  global price
  print()
  toppings = input("Please enter Y if you would like to browse/add toppings to your drink, and N if not: ")
  toppings = toppings.upper()
  while toppings != "Y" and toppings != "N":
    print()
    toppings = input("Sorry, this is not a valid option. Please enter Y if you would like to browse/add toppings to your drink, and N if not: ")
    toppings = toppings.upper()
  while toppings == "Y":
    print()
    print("T1. Tapioca Pearls: 0.50")
    print()
    print("T2. Mango Popping Pearls: 0.50")
    print()
    print("T3. Grass Jelly: 0.50")
    print()
    print("T4. Herbal Jelly: 0.50")
    print()
    print("T5. Coconut Jelly: 0.50")
    print()
    print("T6. Red Bean: 0.50")
    print()
    print("T7. Pudding: 0.75")
    print()
    interest = input("Please enter the code of a topping you would like to order. If you do not want any, please enter N: ")
    interest = interest.upper()
    while interest != "N" and interest != "T1" and interest != "T2" and interest != "T3" and interest != "T4" and interest != "T5" and interest != "T6" and interest != "T7":
      print()
      interest = input("Sorry, this is not a valid option. Please enter the code of a topping you would like to order. If you do not want any, please enter N: ")
      interest = interest.upper()
    if interest == "N":
      toppings = "N"
    elif interest == "T7":
      price += 0.75
      print()
      interest2 = input("Please enter Y if you would like to order additional toppings, and N if not: ")
      interest2 = interest2.upper()
      while interest2 != "Y" and interest2 != "N":
        print()
        interest2 = input("Sorry, this is not a valid option. Please enter Y if you would like to order additional toppings, and N if not: ")
        interest2 = interest2.upper()
      if interest2 == "N":
        toppings = "N"
      elif interest == "Y":
        toppings = "Y"
    else:
      price += 0.50
      print()
      interest2 = input("Please enter Y if you would like to order additional toppings, and N if not: ")
      interest2 = interest2.upper()
      while interest2 != "Y" and interest2 != "N":
        print()
        interest2 = input("Sorry, this is not a valid option. Please enter Y if you would like to order additional toppings, and N if not: ")
        interest2 = interest2.upper()
      if interest2 == "N":
        toppings = "N"
      elif interest == "Y":
        toppings = "Y"
  if toppings == "N":
    rest()

def rest():
  print()
  sweetness = input("Please enter 0 for no added sugar, 25 for little sugar, 50 for half sugar, 75 for less sugar, and 100 for normal sugar: ")
  while sweetness != "0" and sweetness != "25" and sweetness != "50" and sweetness != "75" and sweetness != "100":
    print()
    sweetness = input("Sorry, this is not a valid option. Please enter 0 for no added sugar, 25 for little sugar, 50 for half sugar, 75 for less sugar, and 100 for normal sugar: ")
  if heat == "C":
    print()
    icelvl = input("Please enter 0 for no ice, 50 for less ice, and 100 for full ice: ")
    while icelvl != "0" and icelvl != "50" and icelvl != "100":
      print()
      icelvl = input("Sorry, this is not a valid option. Please enter 0 for no ice, 50 for less ice, and 100 for full ice: ")
  final()

def final():
  global price
  global more
  print()
  print("Thank you for purchasing at BOMBNERY! Would you like to order any additional items?")
  print()
  more = input("Please enter Y to order more, N to proceed to checkout, and C to cancel this order: ")
  more = more.upper()
  while more != "Y" and more != "N" and more != "C":
    print()
    more = input("Sorry, this is not a valid option. Please enter Y to order more, N to proceed to checkout, and C to cancel this order: ")
    more = more.upper()
  if more == "Y":
    run()
  elif more == "C":
    price = 0
    run()
  elif more == "N":
    run()

def main():
  print("Welcome to BOMBNERY!")
  print("To see specific sections of our menu, please enter 1 for coffee drinks, 2 for classic tea drinks, 3 for milk tea drinks, 4 for fruit tea drinks, 5 for slush drinks, 6 for dessert, 7 for our promotional series, and 8 for a blurb about us!")
  catalog = input("Enter a number: ")
  while catalog != "1" and catalog != "2" and catalog != "3" and catalog != "4" and catalog != "5" and catalog != "6" and catalog != "7" and catalog != "8":
    print("Sorry, this is not a valid option.")
    print("To see specific sections of our menu, please enter 1 for coffee drinks, 2 for classic tea drinks, 3 for milk tea drinks, 4 for fruit tea drinks, 5 for slush drinks, 6 for dessert, 7 for our promotional series, and 8 for a blurb about us!")
    catalog = input("Enter a number: ")
  if catalog == "1":
    coffee()
  elif catalog == "2":
    classictea()
  elif catalog == "3":
    milktea()
  elif catalog == "4":
    fruittea()
  elif catalog == "5":
    slush()
  elif catalog == "6":
    dessert()
  elif catalog == "7":
    promo()
  elif catalog == "8":
    blurb()

def checkout():
  global price
  print("Your total is $%0.2f." %price)
  print()
  confirm = input("To cancel your order, please enter C. To confirm your order, please enter P: ")
  confirm = confirm.upper()
  while confirm != "C" and confirm != "P":
    print()
    confirm = input("Sorry, this is not a valid option. Please enter C to cancel your order or P to confirm your order: ")
    confirm = confirm.upper()
  if confirm == "C":
    price = 0
    run()
  elif confirm == "P":
    print()
    print("Thank you for purchasing at BOMBNERY! Please walk to the pick-up station at the front to receive your order. You will be asked to pay at the cashier.")

def run():
  global more
  if more != "N":
    print()
    main()
  else:
    print()
    checkout()

run()