def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    zeros = list1.count(0) 
    ones = list1.count(1)
    list0= [ones,zeros]
    
    
    return list0