import importlib.util

def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

utils = _load_module("utils", "utils.pyc")

env_wrapper = utils.env_wrapper
get_action_info = utils.get_action_info
reward_recorder = utils.reward_recorder
loss_checker = utils.loss_checker
replay_buffer = utils.replay_buffer
soft_clamp = utils.soft_clamp

