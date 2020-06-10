corr_ans=['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
with open('answers.txt') as f:
    f = list(map(lambda x: x[0].upper(), f.readlines()))
score = 0
for i in range(20):
    if corr_ans[i]==f[i]: score+=1
if score>=15: print('Passed')
else: print('Failed')


'''
Implementataion in a function
def driver(filename='answers.txt):
   corr_ans=['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    with open('answers.txt') as f:
        f = list(map(lambda x: x[0].upper(), f.readlines()))
    score = 0
    for i in range(20):
        if corr_ans[i]==f[i]: score+=1 
    return 'Passed' if score >=15 else 'Failed
'''