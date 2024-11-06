from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.
CATEGORY = (
    ('Board Game', 'Board Game'),
    ('Craft Supplies', 'Craft Supplies'),
    ('Event Supplies', 'Event Supplies'),
    ('Small Misc.', 'Small Misc.'),
    ('Large Misc./Electronics', 'Large Misc./Electronics'),
    ('Food/Edible', 'Food/Edible'),
    ('Locker Tools', 'Locker Tools')

)

# Model for each item
class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Item'

    def __str__(self):
        return f"{self.name} : {self.quantity} stock"


# Model for each student supply on loan
class Loan(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    # Setting the due date for loaned item
    check_out = models.DateField(auto_now_add=True)
    due = datetime.now() + relativedelta(month=1)
    due_date = models.DateField(default=due)

    def __str__(self):
        return f'{self.item.name} checked out by {self.student.username}'