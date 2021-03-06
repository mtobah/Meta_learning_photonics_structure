AVAILABLE_EXPS = {'forward_model', 'inverse_model',
                  'tandem_net', 'vae', 'gan', 'inn'}


def get_configs(experiment):
    if experiment not in AVAILABLE_EXPS:
        raise NotImplementedError

    configs = {
        'forward_model':
        {'model_name': 'forward_model',
         'input_dim': 4,
         'output_dim': 3,
         'epochs': 100,
         'weight_decay': 1e-5,
         'learning_rate': 1e-3},

        'inverse_model':
        {'model_name': 'inverse_net',
         'input_dim': 3,
         'output_dim': 4,
         'epochs': 100,
         'weight_decay': 1e-5,
         'learning_rate': 1e-3},

        'tandem_net':
        {'model_name': 'tandem_net',
         'input_dim': 3,
         'output_dim': 3,
         'epochs': 100,
         'weight_decay': 1e-5,
         'learning_rate': 1e-3},

        'vae':
        {'model_name': 'vae',
         'input_dim': 4,
         'latent_dim': 5,
         'epochs': 500,
         'weight_decay': 1e-5,
         'learning_rate': 1e-3},

         'gan':
        {'model_name': 'gan',
         'input_dim': 3,
         'hidden_dim': 128,
         'output_dim': 4,
         'noise_dim': 1,
         'epochs': 500,
         'weight_decay': 1e-5,
         'g_learning_rate': 1e-3,
         'd_learning_rate': 1e-4},

         'inn':
        {'model_name': 'inn',
         'input_dim': 4,
         'hidden_dim': 128,
         'output_dim': 3,
         'latent_dim': 2, 
         'ndim_total': 16,
         'epochs': 2000,
         'weight_decay': 1e-5,
         'learning_rate': 5e-4},

    }

    return configs[experiment]

    
                