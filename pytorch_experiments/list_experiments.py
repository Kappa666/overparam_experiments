'''
Module that has the list of names of the experiments to process for making figures.
'''

def experiment_RLNL_RL():
    '''
    Experiment where we pre-trained on RL then NL different degrees of corruption.
    Last point is the RL points, trained only on RL.
    '''
    RL_str = ''
    list_names = []
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_NL_only_1st_layer_BIAS_True_batch_size_train_1024_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.0001_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.001_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.01_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.1_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.2_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.5_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.75_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    ### list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_1.0_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    ### list_names.append('flatness_June_label_corrupt_prob_1.0_exptlabel_RLInits_only_1st_layer_BIAS_True_batch_size_train_1024_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #list_names.append('flatness_June_label_corrupt_prob_1.0_exptlabel_RL_only_1st_layer_BIAS_True_batch_size_train_1024_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #RL_str ='debug'
    #RL_str = 'RL_point_'
    #RL_str = 'RL_point_and_0NL_'
    RL_str = 'Only_0NL_'
    return list_names, RL_str

def experiment_BigInits_MNIST():
    '''
    Experiment where we pre-trained on RL then NL different degrees of corruption.
    Last point is the RL points, trained only on RL.
    '''
    RL_str = ''
    list_names = []
    list_names.append('flatness_July_label_corrupt_prob_0.0_exptlabel_NL_24_units_2_layers_only_1st_layer_BIAS_True_data_set_mnist_reg_param_0.0_means_[0,0,0]_stds_[0.001,0.001,0.001]_batch_size_train_1024_lr_0.01_momentum_0.9_epochs_600')
    list_names.append('flatness_July_label_corrupt_prob_0.0_exptlabel_NL_24_units_2_layers_only_1st_layer_BIAS_True_data_set_mnist_reg_param_0.0_means_[0,0,0]_stds_[0.05,0.05,0.05]_batch_size_train_1024_lr_0.01_momentum_0.9_epochs_600')
    #list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.001_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.01_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.1_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.2_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.5_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    #list_names.append('flatness_June_label_corrupt_prob_0.0_exptlabel_RLNL_0.75_only_1st_layer_BIAS_True_batch_size_train_256_lr_0.01_momentum_0.9_scheduler_milestones_200,250,300_gamma_1.0')
    RL_str = 'debug'
    #RL_str = 'RL_point_'
    #RL_str = 'RL_point_and_0NL_'
    #RL_str = 'Only_NL_'
    return list_names, RL_str