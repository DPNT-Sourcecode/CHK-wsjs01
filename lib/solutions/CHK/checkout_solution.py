from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        if (isinstance(skus, str)) & (skus.isalpha()):
            list_skus = list(skus.upper())
            dict_counts = Counter(list_skus)
        else:
            return -1
    except:
        return -1
