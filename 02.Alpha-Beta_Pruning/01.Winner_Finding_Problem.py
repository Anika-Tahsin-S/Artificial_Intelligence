import random as rand
import math

# Alpha-Beta Pruning calculation
def Alpha_Beta_Pruning(Random_Points, alpha, beta, depth, index, maximizer): # Checking on depth 0
    # 4 level binary Tree so highest depth will be 3
    if depth == 3: # last depth has the random values
        return Random_Points[index]
    # print("show me",Random_Points[index])

    if maximizer: 
        # alpha = max value = - inf
        max_value = -math.inf

        for i in range(2): # 2 branches explore
            # On second depth, index = 2 * 0 + 1 = 1, minimum (continued for other braches)
            explore = Alpha_Beta_Pruning(Random_Points, alpha, beta, depth + 1, 2 * index + i, False) # seeing depth 3 values
            # print(Random_Points, alpha, beta, depth + 1, 2 * index + i)
            max_value = max(max_value, explore)
            # print("<<<<<<<<<<><<<<<max show",max_value, explore)
            alpha = max(alpha, max_value)
            # print("<<<<<<<<<<<<<<<<aplha dekhao", (alpha, max_value))
            if beta <= alpha:
                break
        return max_value
        
    else:
        # beta = min value = inf
        min_value = math.inf

        for i in range(2):# 2 branches explore
            # On second depth, index = 2 * 0 + 1 = 1, maximum (continued for other braches)
            explore = Alpha_Beta_Pruning(Random_Points, alpha, beta, depth + 1, 2 * index + i, True)
            # print(Random_Points, alpha, beta, depth + 1, 2 * index + i)
            min_value = min(min_value, explore)
            # print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> min val", (min_value, explore))
            beta = min(beta, min_value)
            # print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> min val", (beta, min_value))
            if beta <= alpha:
                break
        return min_value

# ----------------------------------------------------------------------------------------------- #
# Input ARC
ID_Input = input('Enter ID: ')
ID_Input = ID_Input.replace('0', '8')

Total_Shuffle = int(ID_Input[3])

Min_Point_For_Optimus = int(ID_Input[4])

Total_Points_Win_Optimus = int(ID_Input[-1:-3:-1])
Max_Point_For_Optimus = math.ceil(Total_Points_Win_Optimus * 1.5)

Random_Points = [rand.randint(Min_Point_For_Optimus, Max_Point_For_Optimus) for bleh in range(8)] 
# The randint() method returns an integer number selected element from the specified range. 
# Note: This method is an alias for randrange(start, stop+1) .


# ----------------------------------------------------------------------------------------------- #
# Random Point Generate ARC
def search(Random_Points):
                            # Alpha_Beta_Pruning(Random_Points, alpha, beta, depth, index, maximizer)
    possible_highest_points = Alpha_Beta_Pruning(Random_Points, -math.inf, math.inf, 0, 0, True)
    return possible_highest_points

achieved_points = search(Random_Points)

winner = "Optimus Prime" if achieved_points >= Total_Points_Win_Optimus else "Megatron"


# ----------------------------------------------------------------------------------------------- #
# Shuffle ARC ( To see how many times won a game )
Shuffled = []
win_count = 0

for i in range(Total_Shuffle):
    New_Random_Points = rand.choice(Random_Points) # from the previous Random_Points in a specified sequence took random elememt
    Shuffled.append(New_Random_Points)
    if achieved_points >= New_Random_Points: 
        win_count += 1

max_number_from_shuffle = max(Shuffled)

# ----------------------------------------------------------------------------------------------- #
# Output ARC
print( )
print("Generated 8 random points between the minimum and maximum point ") 
print("limits: ", Random_Points)
print("Total points to win: ", Total_Points_Win_Optimus)
print("Achieved point by applying alpha-beta pruning = ", achieved_points)
print("The winner is ", winner)

print( )
print("After the Shuffle:")
print("List of all points values from each shuffle: ", Shuffled)
print("The maximum value of all shuffles: ", max_number_from_shuffle)
print(f"Won {win_count} times out of {Total_Shuffle} shuffles")