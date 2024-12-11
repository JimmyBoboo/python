
def place_order(ribbe=0, pinne=0, lute=0, nut=0, rein=0):
    
    order = {
    "ribbe": ribbe,
    "pinnekjøtt": pinne,
    "lutefisk": lute,
    "nøttefisk": nut,
    "reindyrstek": rein}
    
    
    
    if rein > 0:
        print("Buhuu")

    return(order)

result = place_order(ribbe=2, pinne=3, lute=5, nut=0, rein=2)
print(result)



        
