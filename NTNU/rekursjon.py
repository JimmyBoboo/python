sum_list = ([1,3[5,3], [6,[4,2]]]) = 24

def sum_list(list):
    total = 0
    for element in list:
        if isinstance(element, list):
            total += sum_list(element)
        
        else:
            total += element
            
        return total


