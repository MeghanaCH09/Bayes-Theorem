st_prob = 0.2

st_pos_prob = 0.02*0.85
nost_pos_prob = 0.8*0.02
positive_prob = st_pos_prob + nost_pos_prob 

pos_give_st_prob = 0.85

prob_result = (st_prob*pos_give_st_prob)/(positive_prob)

print("The probability of a person testing positivr and hvaing strep throat is: ", round((prob_result), 3))