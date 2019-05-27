def roll_dice(num_dice, num_rolls):
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]
    for roll in range(0, len(double_list)):
      for die in range(0, len(double_list[roll])):
          double_list[roll][die] = (int)(random.random()*6 + 1)
    return double_list
def sum_of_roll(double_list):
    final_list = []
    for list in double_list:
        sum_of_values = sum(list)
        final_list.append(sum_of_values)
    return final_list

def yahtzee(double_list):
    counter = 0
    for list in double_list:
        if rows_equal(list) == True:
            counter += 1
        else:
            counter+= 0
    return counter
def rows_equal(list):
    return len(set(list)) <= 1
    
print("Testing sum_of_roll...")
print(sum_of_roll([[4, 5, 2],[6,2,1],[4,4,4]]), [11, 9, 12])
print(sum_of_roll([[3, 4, 6],[2,6,1],[3,4,3]]), [13, 9, 10])
print("Testing yahtzee...")
print(yahtzee([[4, 5, 2],[6,2,1],[4,4,4]]), 1)
print(yahtzee([[3, 4, 6],[2,6,1],[3,4,3]]), 0)