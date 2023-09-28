# 0.2 Strange Device
# You head towards the hill where Cosmo detected the second cipher plate. A narrow trail branches off the main path. You hesitate for a second.

# "Don't worry, this forest is not dangerous for humans", Cosmo calms you down. "I suggest that we follow the trail - it will lead us up to that hill."

# The trail leads you deeper into the forest. After a while, you see that it starts to wind its way up. You hike the hill and see that Cosmo was right. At the top, there is a round clearing with a chest in its center that looks similar to the one in the key workshop. You know that there is another plate inside without Cosmo telling you.

# The chest is locked, but the display and buttons embedded in its lid tell you that this time, you require a code instead of a key to open it. The display shows you two lines of what seems to be a computing task. Behind the chest, some cryptic rules are engraved in a large stone:

# X; X; R; Q; -> 0
# X; Y; R; Q; -> 1
# Y; X; R; Q; -> 1
# Y; Y; R; Q; -> 1

# X; X; N; Q; -> 0
# Y; X; N; Q; -> 0
# X; Y; N; Q; -> 0
# Y; Y; N; Q; -> 1
# "Ahhh, this type of lock is quite common here", Cosmo says. "You have to solve the problem that is shown on the display. Once upon a time, the leaders of the civilization that lived here used decoding devices for these locks. Without a device, it is very hard to solve the problem, but luckily, someone left hints in the stone. There is always some logic behind the codes, and with these rules, I am sure a human like you will find the solution quickly. There are only two buttons on the chest, "0" and "1", so the solution must be a combination of them!"

# You look closer to the task shown on the display:

# YXYY; YYXY; N; Q;
# XYXX; XYYX; R; Q;

# "But this gives me two solutions - one for each line", you complain. "Which one do I have to enter?"

# "Oh, sorry, I forgot to tell you", Cosmo replies. "If there are multiple solutions, you can just concatenate them."

import pandas as pd
import numpy as np

# Prepare the cripted rules
rules = pd.DataFrame({
    'X':['X', 'X', 'Y', 'Y', 'X', 'Y', 'X', 'Y'],
    'Y':['X', 'Y', 'X', 'Y', 'X', 'X', 'Y', 'Y'],
    'R':['R', 'R', 'R', 'R', 'N', 'N', 'N', 'N'],
    'Q':['Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q', 'Q'],
    'result':[0, 1, 1, 1, 0, 0, 0, 1]
})

# Solve the first line
first_line_split = 'YXYY; YYXY; N; Q; '.split('; ')
first_line_matrix = [list(first_line_split[0]), list(first_line_split[1]), list(first_line_split[2]), list(first_line_split[3])]
first_line_result = ''
for i in range(4):
    rule_result = rules[rules['X'] == first_line_matrix[0][i]]
    rule_result = rule_result[rule_result['Y'] == first_line_matrix[1][i]]
    rule_result = rule_result[rule_result['R'] == first_line_matrix[2][0]]
    rule_result = rule_result[rule_result['Q'] == first_line_matrix[3][0]]   
    first_line_result += str(rule_result['result'].values[0])
print(first_line_result) # 1001

# Solve the second line
second_line_split = 'XYXX; XYYX; R; Q;'.split('; ')
second_line_matrix = [list(second_line_split[0]), list(second_line_split[1]), list(second_line_split[2]), list(second_line_split[3])]
second_line_result = ''
for i in range(4):
    rule_result = rules[rules['X'] == second_line_matrix[0][i]]
    rule_result = rule_result[rule_result['Y'] == second_line_matrix[1][i]]
    rule_result = rule_result[rule_result['R'] == second_line_matrix[2][0]]
    rule_result = rule_result[rule_result['Q'] == second_line_matrix[3][0]]   
    second_line_result += str(rule_result['result'].values[0])
print(second_line_result) # 0110

# Concatenate the results
solution = str(first_line_result) + str(second_line_result)
print(solution) #10010110




