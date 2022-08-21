import binascii
from algosdk.v2client import algod
from verifier.settings import env

algod_client = algod.AlgodClient(env('ALGOD_TOKEN'), env('NODE_API'))

class Utils():
    @classmethod
    def fetch_decompiled_code(self, code):
        response = algod_client.algod_request('POST', '/teal/disassemble', None, binascii.a2b_base64(code))
        return response.get('result')