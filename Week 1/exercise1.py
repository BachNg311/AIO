def exercise1(tp, fp, fn):
    if (type(tp) != int):
        print('tp must be int')
        return
    elif (type(fp) != int):
        print('fp must be int')
        return
    elif (type(fn) != int):
        print('fn should be int')
    
    if (tp < 0 or fp < 0 or fn < 0):
        print('tp and fp and fn must be greater than zero')
        return
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)

    print('precision is {}'.format(precision))
    print('recall is {}'.format(recall))
    print('f1-score is {}'.format(f1))