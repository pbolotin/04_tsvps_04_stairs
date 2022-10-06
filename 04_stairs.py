import sys
import json

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def print_help():
    eprint("This is a help message")
    eprint("Use program with just one argument: filename with stairs description")
    eprint("Example:")
    eprint("04_staris.py filename_with_stairs_description")

def arguments_validation():
    if len(sys.argv) != 2:
        return False
    else:
        return True
        
def check_file(filename_to_check):
    try:
        f = open(filename_to_check, "r")
        f.close()
        return True
    except:
        return False
        
def read_file_into_stairs_list(filename):
    try:
        f = open(filename, "r")
        result = [int(item) for item in f]
        result.insert(0,0) #Need zero position
        return result
    except OSError:
        eprint("Fatal error read_file_into_enum_list with code 0001")
        exit()
        
if __name__ == "__main__":
    eprint("04_stairs")
    if not arguments_validation():
        print_help()
        exit()
    if not check_file(sys.argv[1]):
        print_help()
        exit()
    
    stairs = read_file_into_stairs_list(sys.argv[1])
    print(stairs)
    
    # First method
    current_place = 0
    max_summa = 0
    way_to_max = [("step len", "position on stairs", "summa")]
    while True:
        if (current_place < len(stairs) - 2 and stairs[current_place + 1] >= stairs[current_place + 2]) or (current_place == len(stairs) - 2):
            max_summa += stairs[current_place + 1]
            current_place += 1
            way_to_max.append((1,current_place,max_summa))
        elif current_place < len(stairs) - 2:
            max_summa += stairs[current_place + 2]
            current_place += 2
            way_to_max.append((2,current_place,max_summa))
        else:
            break

    print(way_to_max)
    
    # Second method
    curr_stair = 0
    curr_max = 0
    prev_max = 0
    prev_prev_max = 0
    while True:
        prev_prev_max = prev_max
        prev_max = curr_max
        
        cost_curr_stair = stairs[curr_stair]
        curr_max = max(prev_max, prev_prev_max) + cost_curr_stair
        
        print(f"Stair {curr_stair}, {curr_max}")
        
        curr_stair += 1
        if curr_stair == len(stairs): break