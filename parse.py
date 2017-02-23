
#params = (rows, cols, topping_limit, cell_limit)
def parse(filename):
    # datatype here
    with open(filename, 'r') as f:
        rows, cols, topping_limit, cell_limit = map(int, f.readline().split())
        data = f.read().split("\n")[:-1] # delete the last newline
        
        for line in data:
            pass # insert into datatype
    
    # return data


def precompute_stuff():
    pass
