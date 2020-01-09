from abc import abstractmethod

class Agent(object):
    def __init__(self, name):
        self.name = name
       
    def __str__(self):
        return "Agent_" + self.name

    @abstractmethod
    def will_buy(self, value, price, prob):
        """Given a value, price, and prob of Junk,
        return True if you want to buy it; False otherwise.
        Override this method."""

class HalfProbAgent(Agent):
    """Buys if the prob < 0.5 no matter what the value or price is"""
    
    def will_buy(self, value, price, prob):
        return (prob < 0.5)

class RatioAgent(Agent):
    """Buys if the ratio of the price to value is below a specified threshold"""
    
    def __init__(self, name, max_p_v_ratio):
        super(RatioAgent, self).__init__(name)
        self.max_p_v_ratio = max_p_v_ratio
    
    def will_buy(self, value, price, prob):
        return (price/value <= self.max_p_v_ratio)

class BuyAllAgent(Agent):
    """Simply buys all products"""
    
    def will_buy(self, value, price, prob):
        return True

class StudentAgent(Agent):
    """The Student Agent"""
    
    def will_buy(self, value, price, prob):
        # CHANGE THIS. IMPLEMENT THE BODY OF THIS METHOD
        if (1-prob)*value > price:
            return True