import collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    list_skus = list(skus)
    dict_counts = Counter(list_skus)

