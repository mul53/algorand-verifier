import importlib
import uuid
import os
from pyteal import Mode, compileTeal
import importlib.util
from .teal_compiler import TealCompiler
from ...models import SourcePyTealMode

class PyTealCompiler():
    def get_mode(self, value: str):
        if value == SourcePyTealMode.APPLICATION:
            return Mode.Application
        elif value == SourcePyTealMode.SIGNATURE:
            return Mode.Signature

    def compile(self, source: str, opts = {}) -> str:
        mode = self.get_mode(opts.get('mode')) if opts.get('mode') else Mode.Application 
        version = opts.get('version') if opts.get('version') else 2
        file_path = "./{}.py".format(uuid.uuid1())

        with open(file_path, 'w') as file:
            file.write(source)
            file.close()

            spec = importlib.util.spec_from_file_location("xyz", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            app_approval = compileTeal(module.approval_program(), mode, version=version)
            compiled_app_approval = TealCompiler().compile(app_approval)

            app_clear = compileTeal(module.clear_state_program(), mode, version=version)
            compiled_app_clear = TealCompiler().compile(app_clear)

        os.remove(file_path)

        return { "app_approval": compiled_app_approval, "app_clear": compiled_app_clear }
