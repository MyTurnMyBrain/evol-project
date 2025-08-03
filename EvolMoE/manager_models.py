import importlib.util

def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# 加载 pyc 模块
models = _load_module("models", "models.pyc")

# 导出你希望暴露的内容
actor_critic_net = models.actor_critic_net

