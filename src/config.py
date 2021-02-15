
common_config = {
    'data_dir': 'data/UPTI',
    'img_width': 100,
    'img_height': 32,
    'map_to_seq_hidden': 64,
    'rnn_hidden': 256,
    'leaky_relu': False,
}

train_config = {
    'epochs': 1,
    'train_batch_size': 64,
    'eval_batch_size': 512,
    'lr': 0.0005,
    'show_interval': 500,
    'valid_interval': 20000,
    'save_interval': 100,
    'cpu_workers': 4,
    'reload_checkpoint': None,
    'valid_max_iter': 100,
    'decode_method': 'greedy',
    'beam_size': 10,
    'checkpoints_dir': 'checkpoints/'
}
train_config.update(common_config)

evaluate_config = {
    'eval_batch_size': 256,
    'cpu_workers': 4,
    'reload_checkpoint': 'checkpoints/crnn.pth',
    'decode_method': 'greedy',
    'beam_size': 10,
}
evaluate_config.update(common_config)
