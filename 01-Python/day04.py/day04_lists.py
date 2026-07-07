fruits=["Apple","Mango","peache","bannana"]
print(fruits)
print(fruits[0])
print(fruits[3])
fruits[1]="Orange"
print(fruits)
print(len(fruits))
for fruit in fruits:
    print(fruit)
fruits.append("avacado")
print(fruits)
fruits.remove("Orange")
print(fruits)
fruits.pop(-2)
print (fruits)    