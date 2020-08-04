print("Loops and Conditionals exercise")

# For loop
# x is a loop variable
for x in range(5):
  print(x)

for x in range(3, 6):
  print(x)


# While loop
count = 0 
while (count < 3):
  count += 1
  print("Hello friend!")
  print(count)
  
# CONDITIONALS

i = 15
if (i > 15):
  print("i is more than 15.")
  print("i'm in an if block")
elif (i == 15):
  print("i is equal to 15.")
  print("i'm in an elif")
else:
  print("i is less than 15")
  print("i'm in an else block")