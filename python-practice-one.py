def score(dice):
    num_count = [0,0,0,0,0,0] # 1's, 5's, 6's, 4's, 3's, 2's
    num_check = False
    fin_count = 0

    for i in dice: 
        if i == 1:
            if num_count[0] == 2 and num_check != True:
                fin_count = fin_count - 300 + 1000
                fin_count = fin_count +  100
                num_check = True
                num_count[0] += 1
            else: 
                num_count[0] = num_count[0] + 1
                fin_count += 100
        if i == 5: 
             if num_count[1] == 2 and num_check != True:
                fin_count = fin_count - 150 + 500
                fin_count = fin_count + 50
                num_check = True
                num_count[1] += 1 
             else:
               fin_count = fin_count + 50
               num_count[1] += 1
        if i == 6:   
                if num_count[2] == 2: 
                    fin_count = fin_count + 600
                num_count[2] += 1
        if i == 4:
                if num_count[3] == 2:
                    fin_count = fin_count + 400
                num_count[3] += 1
        if i == 3:
                if num_count[4] == 2:
                    fin_count = fin_count + 300
                num_count[4] = num_count[4] + 1
        if i == 2:
                if num_count[5] == 2: 
                    fin_count = fin_count + 200
                num_count[5] += 1        

    return fin_count


def main():
        print(score([2,3,4,6,2]))
        print(score([1,1,1,1,1]))
        print(score([2,4,4,5,4]))
        return 0

main()