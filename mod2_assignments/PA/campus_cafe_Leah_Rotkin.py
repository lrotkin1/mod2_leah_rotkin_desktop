#pseudo code
'''start
print campus cafe
      coffee price
      muffin price
input how many coffees and muffins
input tip amount
function - receipt
    print receipt
    print amount of coffee at $2 =
    print amount of coffee at $2 =
    print subtotal
    print tax
    print total
    print Thank You!
call function
end'''






print("== Campus Cafe ==")
print("Coffee - $2")
print("Muffin - $3")

print("")

coff = int(input("How many coffes would you like? "))
muff = int(input("How many muffins would you like? "))

print("")

tip = int(input("Enter tip amount, e.g., 10 for 10% ?"))

print("")


def receipt():
    print("---Receipt---")

    tot_coff= int(coff*2)
    tot_muff = int(muff*3)

    print(coff, "x coffe @ $2 =$", coff*2,)
    print(muff, "x muffin @ $3 =$",muff*3)

    food = tot_coff + tot_muff

    print("subtotal:$", round(food,2))

    print("")

    print("Tax(8.875%):$",round(.08875*food,2))

    final_tip = (food / (tip))
    print("Tip(10%):$", round(final_tip,2))

    tot_money = food + final_tip + .08875*food

    print("TOTAL:$",round(tot_money,2))

    print("")

    print("Thank You!")

receipt()