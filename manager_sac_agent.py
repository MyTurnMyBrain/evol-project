import importlib.util

def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

sac_agent0 = _load_module("sac_agent", "sac_agent.pyc")

sac_agent = sac_agent0.sac_agent

