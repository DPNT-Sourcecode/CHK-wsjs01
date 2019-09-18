from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    dict_prices = {"A":50, "B": 30, "C":20, "D": 15}

    if (isinstance(skus, str)) & (skus.isalpha()):
        list_skus = list(skus.upper())
        dict_counts = Counter(list_skus)
        total_costs = []
        for k,v in dict_counts.items():
            if k=="A":
                deal_count = v//3
                deal_cost = deal_count * 130
                total_costs.append(deal_cost)

                non_deal_count = v-(deal_count*3)
                total_costs.append(non_deal_count*dict_prices[k])

            elif k=="B":
                deal_count = v//2
                deal_cost = deal_count * 45
                total_costs.append(deal_cost)

                non_deal_count = v-(deal_count*2)
                total_costs.append(non_deal_count*dict_prices[k])
                
            else:
                total_costs.append(v*dict_prices[k])
        return sum(total_costs)
    else:
        return -1



