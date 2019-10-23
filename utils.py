import numpy as np

def readProgressLog(out_file, two_tests=True):
    
    prog_log = {keyword:list() for keyword in ['train', 'test']}
    if two_tests:
        prog_log.update({'subset':list()})
    
    with open(out_file, 'r') as fn:
        new_lines = fn.readlines()
        
    cntr = 3
    sub_cnt = None
    if two_tests:
        sub_cnt = 2
        
    for new_line in new_lines:
        
        if cntr == 0:
            prog_log['train'].append(float(new_line.split(',')[0]))
            cntr += 1
        
        elif cntr == 1:
            prog_log['test'].append(float(new_line.split(',')[0]))
            cntr += 1
            
        elif cntr == sub_cnt:
            prog_log['subset'].append(float(new_line.split(',')[0]))
            cntr += 1
        
        if new_line[:5] == 'Epoch':
            cntr = 0
    
    return prog_log

def get_max_index(acc_dict, dataset='test'):
    acc_arr = np.array(acc_dict[dataset])
    acc_max = acc_arr.max()
    return acc_max, np.where(acc_arr == acc_max)

def get_min_index(acc_dict, dataset='test'):
    acc_arr = np.array(acc_dict[dataset])[40:]
    acc_min = acc_arr.min()
    return acc_min, np.where(acc_arr == acc_min)

def readRedundancyProgress(out_file):

    redun_dict = dict()
    cntr = 3
#     set_trace()

    with open(out_file, 'r') as fn:
        new_lines = fn.readlines()
        
    for new_line in new_lines:
        if new_line[:9] == 'cifar_len':
            cifar_len = new_line.split(', ')[0].split(' = ')[1]
            times_cifar = new_line.split(', ')[1].split(' = ')[1]
            tiny_frac = new_line.split(', ')[2].split(' = ')[1].strip()
            if not cifar_len in redun_dict.keys():
                redun_dict[cifar_len] = dict()
            if not times_cifar in redun_dict[cifar_len].keys():
                redun_dict[cifar_len][times_cifar] = dict()
            if not tiny_frac in redun_dict[cifar_len][times_cifar].keys():
                redun_dict[cifar_len][times_cifar][tiny_frac] = dict()
                redun_dict[cifar_len][times_cifar][tiny_frac]['train'] = list()
                redun_dict[cifar_len][times_cifar][tiny_frac]['test'] = list()
        
        if cntr == 0:
            redun_dict[cifar_len][times_cifar][tiny_frac]['train'].append(float(new_line.split(',')[0]))
            cntr += 1
        
        elif cntr == 1:
            redun_dict[cifar_len][times_cifar][tiny_frac]['test'].append(float(new_line.split(',')[0]))
            cntr += 1
        
        if new_line[:5] == 'Epoch':
            cntr = 0

    return redun_dict

def readGradResults(out_file, two_tests=False):
    
    prog_log = {keyword:list() for keyword in ['train', 'test', 'loss']}
    if two_tests:
        prog_log.update({'cifar_test':list()})
    
    with open(out_file, 'r') as fn:
        new_lines = fn.readlines()
        
    cntr = 4
    cifar_cnt = 5
    loss_cnt = 2
    if two_tests:
        cifar_cnt = 2
        loss_cnt = 3
    epoch_arr = []
        
    for new_line in new_lines:
        
        if cntr == 0:
            prog_log['train'].append(float(new_line.split(',')[0]))
            cntr += 1
        
        elif cntr == 1:
            prog_log['test'].append(float(new_line.split(',')[0]))
            cntr += 1
            
        elif cntr == cifar_cnt:
            prog_log['cifar_test'].append(float(new_line.split(',')[0]))
            cntr += 1
            
        elif cntr == loss_cnt:
            prog_log['loss'].append(float(new_line.split(',')[0]))
            cntr += 1
        
        if new_line[:5] == 'Epoch':
            cntr = 0
            epoch_arr.append(new_line.split(' ')[-1])
    
    return prog_log, epoch_arr
