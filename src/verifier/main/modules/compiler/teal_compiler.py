from algosdk.v2client import algod
from verifier.settings import env

algod_client = algod.AlgodClient(env('ALGOD_TOKEN'), env('NODE_API'))

class TealCompiler():
    def compile(self, source: str, opts = {}) -> str:
        response = algod_client.compile(source)
        return response.get('result')
