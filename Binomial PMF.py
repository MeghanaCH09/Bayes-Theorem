from math import comb

n = 10        
p = 0.5    

def binomial_pmf(k, n, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

total_probability = 0
for k in range(2, 5):  
    prob = binomial_pmf(k, n, p)
    print(f"P(X = {k}) = {prob:.4f}")
    total_probability += prob

print(f"\nTotal Probability of getting between 2 and 4 heads: {total_probability:.4f}")
