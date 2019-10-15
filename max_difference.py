# Here, max_index > min_index
def get_max_diff(ele_list):
    max_diff = ele_list[1] - ele_list[0]    
    if(ele_list[0] < ele_list[1]):
        min_i = 0
        curr_min = 0
    else:
        min_i = 1
        curr_min = 1
    for j in range(2, len(ele_list)):
        # Calculate the dfference between current minimum and new element
        if((ele_list[j] - ele_list[curr_min]) > max_diff):
            max_diff = ele_list[j] - ele_list[curr_min]
            max_j = j
            min_i = curr_min
            print(max_diff, min_i, max_j)

        # Update the min_index if new element is less than current minimum
        if(ele_list[j] < ele_list[curr_min]):
            curr_min = j
    return max_diff, min_i, max_j

if __name__ == '__main__':
    ele_list = [10, 9, 3, 4, 9, 8, 6, 1, 4, 3, 2, 1]
    ans = get_max_diff(ele_list)
    print(ans)
