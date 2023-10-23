print("Change owed: ")
shillings = int(input())
print("tip: ")
tip = int(input())

shillings = shillings - tip

tax = int(shillings * 16 / 100)
print("Tax: ",tax)
shillings = shillings - tax

thousand_notes = int(shillings / 1000)
print("A thousand shilling notes: ",thousand_notes)
shillings = shillings - thousand_notes * 1000

five_hundred_notes = int(shillings / 500)
print("Five hundred shillinh notes: ",five_hundred_notes)
shillings = shillings - five_hundred_notes * 500

two_hundred_notes = int(shillings / 200)
print("Two hundred shilling notes: ",two_hundred_notes)
shillings = shillings - two_hundred_notes * 200

one_hundred_notes = int(shillings / 100)
print("One hundred shilling notes: ",one_hundred_notes)
shillings = shillings - one_hundred_notes * 100

fifty_notes = int(shillings / 50)
print("Fifty shilling notes: ",fifty_notes)
shillings = shillings - fifty_notes * 50

twenty_coins = int(shillings / 20)
print("Twenty shilling coins: ",twenty_coins)
shillings = shillings - twenty_coins * 20

ten_coins = int(shillings / 10)
print("Ten shilling coins: ",ten_coins)
shillings = shillings - ten_coins * 10

five_coins = int(shillings / 5)
print("Five shilling coins: ",five_coins)
shillings = shillings - five_coins * 5

one_coins = int(shillings / 1)
print("One shilling coins: ",one_coins)
shillings = shillings - one_coins * 1
