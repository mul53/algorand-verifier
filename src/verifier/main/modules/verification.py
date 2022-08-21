from algosdk.v2client import algod
from main.modules.compiler.reach_compiler import ReachCompiler
from main.modules.compiler.teal_compiler import TealCompiler
from verifier.settings import env
from ..models import SourceType

algod_client = algod.AlgodClient(env('ALGOD_TOKEN'), env('NODE_API'))

class Verification():
    def __init__(self, verificationData):
        self.id = verificationData['id']
        self.source_type = verificationData['source_type']
        self.source_raw = verificationData['source_raw']
        self.source_approval = verificationData['source_approval']
        self.source_clear_state = verificationData['source_clear_state']

    def verify_contract(self):
        if self.source_type == SourceType.TEAL:
            compiled_code = self.fetch_compiled_teal_code()
        elif self.source_type == SourceType.REACH:
            compiled_code = self.fetch_compiled_reach_code()

        onchain_compiled_code = self.fetch_onchain_code(self.id)

        if compiled_code.get('app_approval') != onchain_compiled_code.get('app_approval'):
            return (False, None)

        if compiled_code.get('app_clear') != onchain_compiled_code.get('app_clear'):
            return (False, None)

        return (True, compiled_code)

    def fetch_compiled_teal_code(self):
        compiled_approval_code = TealCompiler().compile(self.source_approval)
        compiled_clear_state_code = TealCompiler().compile(self.source_clear_state)
        return { 'app_approval': compiled_approval_code, 'app_clear': compiled_clear_state_code }

    def fetch_compiled_reach_code(self):
        return ReachCompiler().compile(self.source_raw)

    def fetch_onchain_code(self, app_id: str):
        app_info = algod_client.application_info(app_id)
       
        approval_program = app_info.get('params').get('approval-program')
        clear_program = app_info.get('params').get('clear-state-program')

        return { 'app_approval': approval_program, 'app_clear': clear_program }
        