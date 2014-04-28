from django.db import models

class Bet(models.Model):
    """This defines the properties of a single bet: the people involved, the outcome, the final price, etc."""
    outcome = models.IntegerField()
    date = models.DateTimeField('date of bet')
    price = models.IntegerField()
    bet_statement = models.CharField(max_length=300)
    choice_list = models.ManyToManyField(Person)
    accept_list = models.ManyToManyField(Person, through='BetMembership')

    def __unicode__(self):
        return self.bet_statement


class Person(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(Person)
    tokens = models.IntegerField()

    def __unicode__(self):
        return self.name

class BetMembership(models.Model):
    person = models.ForeignKey(Person)
    bet = models.ForeignKey(Bet)
    probability = models.FloatField()
    revenue = models.FloatField()
