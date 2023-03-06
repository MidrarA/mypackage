def top_n(item, n):
    """ This takes in an array of int and returns the top n numbers in descending order

    args:
    item= array of integers
    n= number of integers to return

    return:
    array of top n numbers in descending order

    e.g:
    >>>top_n([4,6,9,2,7],3)
    [9,7,6]
    """
    result=sorted(item,reverse=True)
    return result[:n]

