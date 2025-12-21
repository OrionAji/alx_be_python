import importlib

def test_imports():
    modules = [
        'module1',
        'module2',
        'module3'
    ]
    
    for module in modules:
        try:
            importlib.import_module(module)
        except ImportError:
            assert False, f"Module {module} could not be imported"