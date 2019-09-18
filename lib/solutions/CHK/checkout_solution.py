from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def deal(original_price, multiplier, deal_price):

    return list_costs
def superdeal(prod_count, og_price, deal_mult, deal_price, super_mult, super_price):
    costs=[]
    prod_count = v
    while (prod_count // super_mult) > 0:
        superdeal_count = prod_count//super_mult
        superdeal_cost = superdeal_count * super_price
        costs.append(superdeal_cost)
        prod_count -= superdeal_count*super_mult
    while (prod_count // deal_mult) > 0:
        deal_count = prod_count//deal_mult
        deal_cost = deal_count * deal_price
        total_costs.append(deal_cost)
        prod_count -= deal_count*deal_mult
    costs.append(prod_count*dict_prices[k])
    return list_costs

def checkout(skus):
    dict_prices = {"A":50, "B":30, "C":20, "D":15, "E":40, "F":10,
                   "G":20, "H":10, "I":35, "J":60, "K":80, "L":90,
                   "M":15, "N":40, "O":10, "P":50, "Q":30, "R":50,
                   "S":30, "T":20, "U":40, "V":50, "W":20, "X":90,
                   "Y":10, "Z":50}
    dict_deals = {"A":2, "B":1, "C":0, "D":0, "E":4, "F":4,
                   "G":0, "H":2, "I":0, "J":0, "K":1, "L":0,
                   "M":4, "N":4, "O":0, "P":1, "Q":1, "R":4,
                   "S":0, "T":0, "U":4, "V":2, "W":0, "X":0,
                   "Y":0, "Z":0}
    try:
        # If skus is not empty, if it is, return 0
        if skus:
            # If input is a string and consists of only uppercase alphabetical chars
            if (skus.isupper()) &(isinstance(skus, str)) & (skus.isalpha()):
                list_skus = list(skus)
                total_costs = []
                # If basket is not empty calculate costs
                if len(list_skus)>0:
                    dict_counts = Counter(list_skus)
                    # Reverse keys to get to E items before Bs
                    reverse_keys = reversed(sorted(dict_counts.keys()))
                    dict_counts_rev = {k:dict_counts[k] for k in reverse_keys}
                    # For every item in basket, calculate cost
                    for k,v in dict_counts_rev.items():
                        # Incorporate special deals for A
                        if k=="A":
                            prod_count = v
                            while (prod_count // 5) > 0:
                                superdeal_count = prod_count//5
                                superdeal_cost = superdeal_count * 200
                                total_costs.append(superdeal_cost)
                                prod_count -= superdeal_count*5
                            while (prod_count // 3) > 0:
                                deal_count = prod_count//3
                                deal_cost = deal_count * 130
                                total_costs.append(deal_cost)
                                prod_count -= deal_count*3
                            total_costs.append(prod_count*dict_prices[k])
                        # Incorporate special deals for B
                        elif k=="B":
                            try:
                                prod_count = v-free_B_items
                            except:
                                prod_count = v
                            while (prod_count // 2) > 0:
                                deal_count = prod_count//2
                                deal_cost = deal_count * 45
                                total_costs.append(deal_cost)
                                prod_count -= deal_count*2

                            total_costs.append(prod_count*dict_prices[k])
                        # Incorporate special deals for E
                        elif k=="E":
                            prod_count = v
                            free_B_items = prod_count // 2
                            total_costs.append(prod_count*dict_prices[k])
                        elif k=='F':
                            prod_count = v
                            free_items = 0
                            while prod_count > 0:
                                prod_count -= 2
                                if prod_count > 0:
                                    prod_count -= 1
                                    free_items += 1
                            item_count = v-free_items
                            total_costs.append(item_count*dict_prices[k])

                        # Every other item
                        else:
                            total_costs.append(v*dict_prices[k])
                    return sum(total_costs)
            else:
                return -1
        else:
            return 0
    except:
        return -1



