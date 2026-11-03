# class CashPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# class UPIPayment:
#     def cardpay(self,amount):
#       print("Paid",amount,"using UPI")
# class CardPayment:
#     def cardpay(self,amount):
#         print("Paid",amount,"using card")

# class NetBanking:
#     def pay(self,amount):
#         print("Paid",amount,"using NetBanking")

# Payment=[
#     CashPayment(),
#     UPIPayment(),
#     CardPayment(),
#     NetBanking()
# ]

# choice=input("choise payment method (cash/upi/card/netbanking):")

# if choice == "chash":
#     payment=CashPayment()
# elif choice == "upi":
#     payment=UPIPayment()
# elif choice == "card":
#     payment=CardPayment()
# elif choice == "netbanking":
#     payment=NetBanking()
#     exit()


# payment.pay(1000)
# class Mobile_Notification:
#      def send(self,massage):
#          print("send_notification",massage,"Mobile")
    
# class Email_Notification:
#     def send(self,massage):
#         print("send_notification",massage,"Email")
# class SMS_Notification:
#     def send(self,massage):
#         print("send_notification",massage,"SMS")
# Notification=[Mobile_Notification(),
#                Email_Notification(),
#                SMS_Notification()

# ]

# for Notification in Notification:
#     Notification.send()

class MobileNotification:
    def send(self, message):
        print("Send Notification:", message, "Mobile")

class EmailNotification:
    def send(self, message):
        print("Send Notification:", message, "Email")

class SMSNotification:
    def send(self, message):
        print("Send Notification:", message, "SMS")


notifications = [
    MobileNotification(),
    EmailNotification(),
    SMSNotification()
]

for notification in notifications:
    notification.send("Hello Anushka")