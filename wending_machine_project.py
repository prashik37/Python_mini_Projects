#
# print("            !!!Welcome to the Shiks_caffe!!!                   ")
# class Machine:
#     def __init__ (self):
#         self.Shiks_caffe = {
#     '1': {'name': 'chips   ',  'price': 20,'quantity':10},
#     '2': {'name': 'coldrink',  'price': 30,'quantity':10},
#     '3': {'name': 'bislery ',  'price': 20,'quantity':10},
#     '4': {'name': 'kitkat  ',  'price': 40,'quantity':10},
#     '5': {'name': 'milk    ',  'price': 20,'quantity':10},
#     '6': {'name': 'lollypop',  'price':  5,'quantity':10},
#     '7': {'name':  'candy   ',  'price':15,'quantity':10},
#     '8': {'name':  'sandwitch', 'price':45,'quantity':10},
#     '9': {'name':  'gelly    ', 'price':25,'quantity':10},
#     '10':{'name': 'cold_coffe', 'price':25,'quantity':10},
#
# }
#     def display(self):
#         print("MENU")
#         for item_id,details in self.Shiks_caffe.items():
#             print("------------------------------------------")
#             print(f"{item_id}   {details['name']}  price:{details['price']}Rs  quantity:{details['quantity']}")
#
#     def purchase(self,item_id,quantity,coin_amount):
#         if item_id in self.Shiks_caffe:
#             item = self.Shiks_caffe[item_id]
#             total_price =item['price'] * quantity
#
#             if coin_amount >= total_price:
#                 change = coin_amount - total_price
#
#                 print("Total Price:", total_price)
#                 print("Change:", change)
#                 self.order(item_id, quantity, change)
#
#
#     def insert_coin(self, item_id, quantity):
#         item = self.Shiks_caffe[item_id]
#         price = item['price'] * quantity
#         coin_amount = 0
#         while coin_amount < price:
#             coin = int(input("Insert 10 rs or 5 rs coin: "))
#             if coin == 10 or coin == 5:
#                 coin_amount =coin_amount + coin
#         return coin_amount
#
#     def order(self, item_id, quantity, change):
#         if change > 0:
#             print(f"Please collect your order: {quantity} {self.Shiks_caffe[item_id]['name']}")
#             print(f"Please collect your change: {change} rs.")
#         else:
#             print(f"Please collect your order: {quantity} {self.Shiks_caffe[item_id]['name']}")
#
#
# a = Machine()
# a.display()
# print()
# print()
# item_id= input("enter item_id to purchase ")
# quantity = int(input("enter quantity "))
# coin_amount = a.insert_coin(item_id, quantity)
# a.purchase(item_id,quantity,coin_amount)
# print()
# print()
# ans = input("u want to purchase other items?(yes/no):")
# if ans=="yes":
#     a.display()
#     print("\n")
#     item_id = input("enter item_id to purchase ")
#     quantity = int(input("enter quantity "))
#     coin_amount = a.insert_coin(item_id, quantity)
#     a.purchase(item_id, quantity,coin_amount)
#
# print()
# print()
# print("Thank you for visiting Shiks_Caffe!")s