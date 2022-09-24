"""
network config setting, will be used in train.py and eval.py
"""
from easydict import EasyDict as edict

config_gpu = edict({
    'enable_modelarts': False,

    'random_seed': 1,
    'rank': 0,
    'group_size': 1,
    'work_nums': 8,
    'epoch_size': 250,
    'keep_checkpoint_max': 10,
    'ckpt_path': './',
    'is_save_on_master': 0,

    ### Dataset Config
    'train_batch_size': 128,
    'val_batch_size': 125,

    'num_classes': 1000,

    ### Loss Config
    'label_smooth_factor': 0.1,

    ### Learning Rate Config
    'lr_init': 0.5,

    ### Optimization Config
    'weight_decay': 0.00004,
    'momentum': 0.9,
    'loss_scale': 1,

    ### Cutout Config
    'cutout': True,
    'cutout_length': 56,

})

config_ascend = edict({
    'enable_modelarts': False,

    'random_seed': 1,
    'rank': 0,
    'group_size': 1,
    'work_nums': 8,
    'epoch_size': 300,
    'keep_checkpoint_max': 10,
    'ckpt_path': './',
    'is_save_on_master': 0,

    ### Dataset Config
    'train_batch_size': 96,
    'val_batch_size': 125,

    'num_classes': 1000,

    ### Loss Config
    'label_smooth_factor': 0.1,

    ### Learning Rate Config
    'lr_init': 0.499,

    ### Optimization Config
    'weight_decay': 0.00004,
    'momentum': 0.9,
    'loss_scale': 1,

    ### Cutout Config
    'cutout': True,
    'cutout_length': 56,

})
