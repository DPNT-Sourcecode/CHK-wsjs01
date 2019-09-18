from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    dict_prices = {"A":50, "B": 30, "C":20, "D": 15, "E": 40, "F": 10}
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
                        # Incorporate special deals for E
                        elif k=="E":
                            prod_count = v
                            free_B_items = prod_count // 2
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
                        elif k=='F':
                            prod_count = v
                            free_items = 0
                            if prod_count > 2:
                                if prod_count % 3 == 0:
                                    free_items = prod_count // 2
                                else:
                                    free_items = prod_count % 3
                            prod_count = prod_count-free_items
                            total_costs.append(prod_count*dict_prices[k])
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


