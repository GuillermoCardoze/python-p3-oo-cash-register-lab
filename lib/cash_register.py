class CashRegister:
    def __init__(self, discount=0, total=0, items=None, last_transaction_amount=0):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []
        self.last_transaction_amount = last_transaction_amount

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity 
        self.items.extend([item] * quantity)
        self.last_transaction_amount = price * quantity
        return self.items

    def apply_discount(self):
      if self.discount == 0:
        print("There is no discount to apply.")
      else:
        percent_discount = float(self.discount / 100)
        discount_in_dollars = self.total * percent_discount
        int_total = int(self.total - discount_in_dollars)
        self.total = int_total
        print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if self.last_transaction_amount != 0:
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0
            self.items.pop()  # Remove last item
            if not self.items:
                return 0.0
        else:
            return "No transaction to void"