from django.db import models

# create the Account Model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # defines the model Manager
    Accounts = models.Manager()

    # allows references to a specific account be returned as the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


# choices for transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawl', 'Withdrawal')]


# create the Transaction model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # defines the model Manager
    Transactions = models.Manager()