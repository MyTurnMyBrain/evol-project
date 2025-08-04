import importlib.util

def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

models = _load_module("models", "models.pyc")

actor_critic_net = models.actor_critic_net

