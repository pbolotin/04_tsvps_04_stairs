import sys
import json

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def print_help():
    eprint("This is a help message")
    eprint("Use program with just one argument: filename to sort")
    eprint("Example:")
    eprint("01_selectsort.py sort_this_file.txt > out.txt")
    eprint("It will sort content of file sort_this_file.txt and place result in the out.txt")
    eprint("So... Good Luck!")

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
        
def read_file_into_enum_list(filename):
    try:
        f = open(filename, "r")
        result = [(itr, item.rstrip('\n')) for itr, item in enumerate(f)]
        return result
    except OSError:
        eprint("Fatal error with code 0001")
        exit()

def show_input(enum_list):
    eprint("Input:")
    [eprint(f"[{n}]:{s}") for n, s in enum_list]
        
def selection_sort_enum_list_and_comment_steps(enum_list, order="a"):
    for step in range(1, len(enum_list)):
        left_idx = step - 1
        eprint(f"Step {step}: try to swap between rightest value in the left part and min(max) value in the right part")
        eprint([t[0] for t in enum_list[:left_idx+1]],"|",[t[0] for t in enum_list[left_idx+1:]])
        swap_candidate = left_idx
        for right_idx in range(left_idx + 1, len(enum_list)):
            if order == "a" and enum_list[swap_candidate][1] > enum_list[right_idx][1]:
                eprint(f"SWAP CANDIDATE:{left_idx}:{enum_list[left_idx][0]},{right_idx}:{enum_list[right_idx][0]}")
                swap_candidate = right_idx
            elif order != "a" and enum_list[swap_candidate][1] < enum_list[right_idx][1]:
                eprint(f"SWAP CANDIDATE:{left_idx}:{enum_list[left_idx][0]},{right_idx}:{enum_list[right_idx][0]}")
                swap_candidate = right_idx
                
        if swap_candidate != left_idx:
            eprint(f"SWAP {left_idx}:{enum_list[left_idx][0]}, {swap_candidate}:{enum_list[swap_candidate][0]}")
            swap = enum_list[left_idx]
            enum_list[left_idx] = enum_list[swap_candidate]
            enum_list[swap_candidate] = swap
            
        eprint()
            
    eprint("RESULT:", [t[0] for t in enum_list])
    
def bubble_sort_enum_list_and_comment_steps(enum_list, order="a"):
    for step in range(0, len(enum_list)):
        for rev_step in range(len(enum_list)-1, step, -1):
            eprint(f"Left limit: {step}, right step: {rev_step}")
            eprint(f"Compare: {rev_step - 1} and {rev_step} positions")
            if order == "a" and enum_list[rev_step - 1][1] > enum_list[rev_step][1]:
                eprint(f"SWAP")
                swap = enum_list[rev_step - 1]
                enum_list[rev_step - 1] = enum_list[rev_step]
                enum_list[rev_step] = swap
            elif order != "a" and enum_list[rev_step - 1][1] < enum_list[rev_step][1]:
                eprint(f"SWAP")
                swap = enum_list[rev_step - 1]
                enum_list[rev_step - 1] = enum_list[rev_step]
                enum_list[rev_step] = swap
                
    eprint("RESULT:", [t[0] for t in enum_list])
    
def merge_sort_enum_list_and_comment_steps(enum_list, order="a"):
    def merge_two_lists(list_one, list_two):
        merged_list = []
        while True:
            if list_one[0][1] > list_two[0][1]:
                el = list_two.pop(0)
                merged_list.append(el)
                if len(list_two) == 0:
                    merged_list += list_one
                    break
            else:
                el = list_one.pop(0)
                merged_list.append(el)
                if len(list_one) == 0:
                    merged_list += list_two
                    break
        eprint(*[t[0] for t in merged_list],"|",end = "")
        return merged_list

    limit = len(enum_list)
        
    size_of_part = 1
    while size_of_part < limit:
        iter = 0
        while True:
            part_one_start_idx = iter * size_of_part
            if part_one_start_idx >= limit:
                break
            
            part_one_end_idx = (iter + 1) * size_of_part
            if part_one_end_idx >= limit:
                break
                
            part_two_start_idx = (iter + 1) * size_of_part
            if part_two_start_idx >= limit:
                break
            
            part_two_end_idx = (iter + 2) * size_of_part
            if part_two_end_idx >= limit:
                part_two_end_idx = limit
            
            enum_list[part_one_start_idx:part_two_end_idx] = merge_two_lists(enum_list[part_one_start_idx:part_one_end_idx], enum_list[part_two_start_idx:part_two_end_idx])
            
            iter += 2
            
        size_of_part *= 2
        eprint("END\n")

    if order != "a": enum_list.reverse()
    eprint("RESULT:", [t[0] for t in enum_list])

def output_result(enum_list):
    for n, s in enum_list:
        if sys.stdout.isatty():
            eprint(f"[{n}]:", end="", flush=True)
            print(s, flush=True)
        else:
            print(s)

def load_config_json():
    cfg = None
    if check_file("03_mergesort_cfg.json"):
        f = open("03_mergesort_cfg.json", "r")
        cfg = json.load(f)
        f.close()
    else: #defaul config
        cfg = {"SortDirection":"a"}
    return cfg
    
if __name__ == "__main__":
    eprint("03_mergesort")
    if not arguments_validation():
        print_help()
        exit()
    if not check_file(sys.argv[1]):
        print_help()
        exit()
    
    cfg = load_config_json()
    
    enm_lst = read_file_into_enum_list(sys.argv[1])
    show_input(enm_lst)
    #selection_sort_enum_list_and_comment_steps(enm_lst, cfg["SortDirection"])
    #bubble_sort_enum_list_and_comment_steps(enm_lst, cfg["SortDirection"])
    merge_sort_enum_list_and_comment_steps(enm_lst, cfg["SortDirection"])
    output_result(enm_lst)