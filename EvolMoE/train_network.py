import torch
import numpy as np
import random
import gymnasium as gymn
import metaworld
from arguments import get_args
from manager_sac_agent import sac_agent
from manager_utils import env_wrapper

if __name__ == '__main__':
    args = get_args()
    # build the environment
    env = gymn.make_vec('Meta-World/MT10', vector_strategy='sync', seed=args.seed)
    env = env_wrapper(env, args)
    # create the eval env
    # eval_env = gymn.make_vec('Meta-World/MT10', vector_strategy='sync', seed=args.seed, render_mode='human')
    eval_env = gymn.make_vec('Meta-World/MT10', vector_strategy='sync', seed=args.seed)
    eval_env = env_wrapper(eval_env, args)
    # set seeds
    np.random.seed(args.seed)
    random.seed(args.seed)
    # set the seed of torch
    torch.manual_seed(args.seed)
    if args.cuda:
        torch.cuda.manual_seed(args.seed)
    # create the agent
    torch.autograd.set_detect_anomaly(True)
    sac_trainer = sac_agent(env, eval_env, args)
    sac_trainer.learn()
