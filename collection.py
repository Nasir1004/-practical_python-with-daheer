from collections import Counter

text = "we hope to one day become the world's leader in free education resources we are constantly "\
       "discovering and adding more free content to the webside every day there is already an enarmous"\
       "amount of resources online that can be acessed for free by anyone in the world the main issue"\
       "rigt now is that very little of it is organize or structure in any way . we whant to be the "\
       "solution to that problem"

words = text.split()
 
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
