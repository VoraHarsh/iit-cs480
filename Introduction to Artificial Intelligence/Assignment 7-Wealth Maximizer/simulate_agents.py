import numpy as np

from agents import HalfProbAgent, RatioAgent, BuyAllAgent, StudentAgent

def simulate_agents(agents, value, num_products, alpha, beta, seed=None):
    
    wealth = {}
    
    bought = {}
    
    for agent in agents:
        wealth[agent] = 0
        bought[agent] = 0
    
    if seed is not None:
        np.random.seed(seed)
    
    for _ in range(num_products):
        # price is always lower than or equal to the value
        price = np.random.rand()*value
        
        # prob of being Junk
        prob = np.random.beta(alpha, beta)
        
        # Junk or not?
        junk = prob > np.random.rand()
        
        for agent in agents:
            if agent.will_buy(value, price, prob):
                wealth[agent] -= price
                bought[agent] += 1
                if not junk:
                    wealth[agent] += value
    
    return wealth, bought


def format_money(m):
    if m >= 0:
        return "${:,.2f}".format(m)
    else:
        return "-${:,.2f}".format(-1*m)


def simulate_a_seed(name, seed):
    value = 1000.

    num_products = 10000

    agents = []

    agents.append(HalfProbAgent("hp"))

    agents.append(RatioAgent("ratio_0.75", 0.75))
    agents.append(RatioAgent("ratio_0.50", 0.5))
    agents.append(RatioAgent("ratio_0.25", 0.25))
    agents.append(BuyAllAgent("buy_all"))
    agents.append(StudentAgent(name))


    # Fifty-fifty
    wealth, count = simulate_agents(agents, value, num_products, 1, 1, seed)

    print('-' * 60)
    print('FIFTY-FIFTY')
    print('-' * 60)
    print("{:20}\t{:>20}\t{:>10}".format("Agent", "Wealth", "Count"))
    for agent in agents:
        print("{:20}\t{:>20}\t{:>10}".format(str(agent), format_money(wealth[agent]), "{:,}".format(count[agent])))
    
    
    # More Junk
    wealth, count = simulate_agents(agents, value, num_products, 2, 1, seed)

    print('-' * 60)
    print('MORE JUNK')
    print('-' * 60)

    print("{:20}\t{:>20}\t{:>10}".format("Agent", "Wealth", "Count"))
    for agent in agents:
        print("{:20}\t{:>20}\t{:>10}".format(str(agent), format_money(wealth[agent]), "{:,}".format(count[agent])))
    
    # Fewer Junk
    wealth, count = simulate_agents(agents, value, num_products, 1, 2, seed)


    print('-' * 60)
    print('FEWER JUNK')
    print('-' * 60)

    print("{:20}\t{:>20}\t{:>10}".format("Agent", "Wealth", "Count"))
    for agent in agents:
        print("{:20}\t{:>20}\t{:>10}".format(str(agent), format_money(wealth[agent]), "{:,}".format(count[agent])))

if __name__ == '__main__':
    
    # Change this
    student_first_name = "Harsh"
    
    # Change this
    cwid = "A20445400"
    
    seed = 0
    
    print('=' * 100)
    print("Seed %d" %seed)
    print('=' * 100)
    simulate_a_seed(student_first_name, seed)
    
    seed = int(cwid[1:])
    
    print()
    
    print('=' * 100)
    print("Seed %d" %seed)
    print('=' * 100)
    simulate_a_seed(student_first_name, seed)

