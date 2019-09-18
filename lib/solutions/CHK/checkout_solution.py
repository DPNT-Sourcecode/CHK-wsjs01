from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    dict_prices = {"A":50, "B": 30, "C":20, "D": 15}

    try:
        if (isinstance(skus, str)) & (skus.isalpha()):
            list_skus = list(skus.upper())
            dict_counts = Counter(list_skus)
            total_costs = []
            for k,v in dict_counts.items():
                if k=="A":
                    total_costs.append(v*dict_prices[key])

                elif k=="B":
                    total_costs.append(v*dict_prices[key])

                else:
                    total_costs.append(v*dict_prices[key])
            return total_costs.sum()
        else:
            return -1
    except:
        return -1

