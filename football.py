import random
direc=['left','center','right']
random.choice(direc)

score_you=0
score_com=0

for i in range(5):
    print('===ROUND %d —You Kick ! ==='%(i+1))
    print('left,center,right')
    you=input()
    print('you kicked '+you)
    com=random.choice(direc)
    print('computer saved '+com)
    if you!=com:
        print('Goal!')
        score_you+=1
    else:
        print('oops...')
    print('score: %d(you)-%d(com)\n'%(score_you,score_com))

    print('===ROUND %d —You Save !==='%(i+1))
    print('choice one side to save:')
    print('left,center,right')
    you=input()
    print('you saved '+you)
    com=random.choice(direc)
    print('computer kicked '+com)
    if you==com:
        print('Saved !')
    else:
        print('oops...')
        score_com += 1
    print('score: %d(you)-%d(com)\n'%(score_you,score_com))
