class Person:
    def __init__(self, friends_list=[], bet_history=[], tokens = 100):
        self.friends = friends_list
        self.bet_history = bet_history
        self.tokens = tokens
        

    def ChooseFriends(self, numbers, bet_instance):
        bet_instance.choice_list = [self.friends[num] for num in numbers]

    def ChooseModerator(self, number, bet_instance):
        bet_instance.moderator = self.friends(number)

    def PlaceBet(self, friend_numbers, moderator_number, bet_statement, probability, friends_responses, moderator_response):
        """bet_statement is a string, the statement of the bet"""
        """friends_responses is a list of 0's and 1's of length choice_list"""
        """friends_responses represents friends who agree to the bet"""
        """moderator_response is a 0 or 1, representing the moderator's agreement or disagreement"""
        """probability reflects the bet proposer's assigned probability; when you place a bet you also bet."""
        """You should include yourself in friend_numbers."""
        bet_instance = Bet()
        bet_instance.bet_statement = bet_statement
        print bet_instance.bet_statement 
        print "\n"
        print probability

        if moderator_response == 0:
            print "Moderator declined to participate."
        elif moderator_response == 1:
            ChooseFriends(self, friend_numbers, bet_instance)
            ChooseModerator(self, moderator_number, bet_instance)
            bet_instance.accept_list = [choice_list[friends_responses.index(num)] for num in friends_responses if num == 1]
            new_bet.probability_list[bet_instance.accept_list.index(self)] = probability
            self.bet_history = bet_history + [bet_instance]
            for friend in bet_instance.accept_list:
                friend.bet_history = friend.bet_history + [bet_instance]

        else: pass
        """This produces a list of friends who agree to bet, but only if the moderator agrees"""
        """It also adds a bet to all players' bet_history, with some of the attributes filled in:"""
        """the moderator, choice_list, accept_list, and bet_statement are identified, along with one of the probabilities."""

    def Bet(self, probability, bet_instance):
        """This is the action of betting -- giving a probability estimate."""
        """probability is a number between 0 and 1."""
        """bet_instance is a member of the class Bet."""
        if (self in bet_instance.accept_list) == False:
            print "You are not allowed to participate in this bet."
        else:
            index = bet_instance.accept_list.index(self)
            bet_instance.probability_list[index] = probability
            for friend in bet_instance.accept_list:
                index = friend.bet_history.index(bet_instance)
                my_bet = friend.bet_history[index]
                my_bet.probability_list[bet_instance.accept_list.index(friend)] = probability
        """This updates all the friends in the accept_list to have the given probability in the probability_list of the appropriate bet in their bet_history."""  

    def Moderate(self, outcome, bet_instance):
        if (self == bet_instance.moderator) == False:
            print "You are not the moderator of this bet."
        else:
            bet_instance.outcome = outcome
            
            for friend in bet_instance.accept_list:
                index = friend.bet_history.index(bet_instance)
                my_bet = friend.bet_history[index]
                my_bet.outcome = outcome
                friend_number = bet_instance.accept_list.index(friend)
                if bet_instance.probabilities[friend_number] > price:
                    friend.tokens = friend.tokens - 10 * bet_instance.probabilities
                elif bet_instance.probabilities[friend_number] < price:
                    friend.tokens = friend.tokens + 10 * bet_instance.probabilities
                else:
                    friend.tokens = friend.tokens + 5
                if outcome == 1:
                    if bet_instance.probabilities[friend_number] > price:
                        friend.tokens = friend.tokens + 10
                    elif bet_instance.probabilities[friend_number] < price:
                        friend.tokens = friend.tokens - 10
                    else:
                        pass
                else:
                    pass
    
        
    

class Bet:
    """This defines the properties of a single bet: the people involved, the outcome, the final price, etc."""
    def __init__(self, outcome=0, probability_list =[], price=0, choice_list = [], accept_list = [], moderator = Person(), bet_statement = ""):
        self.outcome = outcome
        self.probability_list = probability_list
        self.price = price
        self.choice_list = choice_list
        self.accept_list = accept_list
        self.moderator = moderator
        self.bet_statement = bet_statement
    """ I will also include a date, once I find out how to use timestamps."""

    def median_price(self):
        if len(probability_list) > 2:
            ordered = sorted(probability_list)
            if (len(probability_list) % 2) == 1:
                median = probability_list[(len(probability_list)+1)/2]
            else:
                median = probability_list[(len(probability_list)/2 + len(probabiity_list)/2 + 1)/2] """wrong"""
            price = median
        if len(probability_list) == 1:
                price = probability_list(0)
        if len(probability_list) == 2:
                price = probability_list(0)
