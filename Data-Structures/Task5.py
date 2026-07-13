shopping_cart=[]
while True:
      product=input("Enter a product name or done if you want to finish").strip()
      if product=="done":
        break
      action=input("Enter action you want to perform on product").strip()
      if action=="add":
          shopping_cart.append(product)
      elif action=="delete":
          shopping_cart.remove(product)
      else:
          print("Please enter a valid action")
print(shopping_cart)



    


