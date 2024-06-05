import random
import math
def regression_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
    num_samples = int(num_samples)
    loss_sum = 0
    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)
        
        loss = 0
        if (loss_name == 'MAE'):
            loss = abs(pred - target)
        elif (loss_name == 'MSE' or loss_name == 'RMSE'):
            loss = (pred - target) ** 2
        loss_sum += loss

        print('loss name: {}, sample: {}, pred: {}, target: {}, loss: {}'.format(loss_name, i, pred, target, loss))
    
    if (loss_name == 'RMSE'):
        print('final {}: {}'.format(math.sqrt(loss_name, loss_sum/num_samples)))
    else: 
        print('final {}: {}'.format(loss_name, loss_sum/num_samples))

num_samples = input('Input number of samples ( integer number ) which are generated : ')
loss_name = input('Enter the loss name (MAE, MSE, RMSE): ')
regression_loss(num_samples, loss_name)
