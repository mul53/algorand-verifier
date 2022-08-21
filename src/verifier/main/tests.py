from turtle import onclick
from django.test import TestCase
from .modules.compiler.reach_compiler import ReachCompiler
from .modules.compiler.pyteal_compiler import PyTealCompiler
from .modules.compiler.teal_compiler import TealCompiler
from .modules.verification import Verification

class MainTestCase(TestCase):
    def test_reach_compile(self):
        with open('./main/fixtures/index.rsh') as file:
            compiled_code = ReachCompiler().compile(file.read())
            self.assertEqual(compiled_code.get('app_approval'), 'BiAKAAEEKCAwCFhgoI0GJgIBAAAiNQAxGEECoSlkSSJbNQEhBls1AjYaABdJQQAHIjUEIzUGADYaAhc1BDYaAzYaARdJgQMMQADOSSQMQABXJBJEJDQBEkQ0BEkiEkw0AhIRRChkSTUDSVcAIDX/JVs1/oAEkSc087AyBjT+D0Q0/zEAEkQ0/zQDIQRbNP40AyEFWzQDVzggNAMhB1syBjQDIQhbQgFFSCQ0ARJENARJIhJMNAISEUQoZEk1AyVbNf9JNQUXNf6ABNQMbNY0/hZQsDIGNP8MRDT+iAH9NP40AyEFWw1EsSKyATQDIQdbsggjshA0A1c4ILIHszQDVwAgNAMhBFs0/zT+MQA0/jIGNAMhCFtCANRJIwxAAFYjEkQjNAESRDQESSISTDQCEhFEKGRJNQNJSVcAIDX/IQRbNf6BOFs1/YAEmouRdLAjNP6IAZ40/zEAEkQ0/zT+NP00AyEFWwg0AyVbNP8iMgY0/UIAeEghCYgBYCI0ARJENARJIhJMNAISEURJNQVJSSJbNf8hBls1/oEQWzX9gAT3cRNNNP8WUDT+FlA0/RZQsCEJiAElsSKyASKyEiSyEDIKshQ0/7IRszEANP8WUDT+FlA0/RZQMgYWUChLAVcAQGdIIzUBMgY1AkIAnDX/Nf41/TX8Nfs1+jX5Nfg0/zT6DkEAKzT4NPkWUDT6FlA0+xZQNPxQNP0WUDT+FlAoSwFXAGhnSCQ1ATIGNQJCAFmxIrIBNP2yCCOyEDT4sgezsSKyASOyEiSyEDT8shQ0+bIRs7EisgEishIkshAyCbIVMgqyFDT5shGzQgAAMRmBBRJEsSKyASKyCCOyEDIJsgkyCrIHs0IABTEZIhJEKTQBFjQCFlBnNAZBAAqABBUffHU0B1CwNABJIwgyBBJEMRYSRCNDMRkiEkRC/98iMTQSRIECMTUSRCIxNhJEIjE3EkQiNQEiNQJC/640AElKIwg1ADgHMgoSRDgQIxJEOAgSRIk0AElKSSMINQA4FDIKEkQ4ECQSRDgRTwISRDgSEkSJ')
            self.assertEqual(compiled_code.get('app_clear'), 'Bg==')


    def test_pyteal_compiler(self):
        with open('./main/fixtures/index.py') as file:
            compiled_code = PyTealCompiler().compile(file.read(), { 'version': 5 })
            self.assertEqual(compiled_code.get('app_clear'), 'BYEBQw==')
            self.assertEqual(compiled_code.get('app_approval'), 'BSADAQAEJgkLYmlkX2FjY291bnQGbmZ0X2lkBnNlbGxlcgpiaWRfYW1vdW50BXN0YXJ0A2VuZA5yZXNlcnZlX2Ftb3VudAttaW5fYmlkX2luYwhudW1fYmlkczEYIxJAAUIxGSMSQACFMRmBBRJAABUxGSISMRmBAhIRMRkkEhFAAAEAI0MyBycEZAxAAEUnBWQyBw5AAAIjQyhkMgMTQAAOKWQqZIgBOipkiAFrIkMrZCcGZA9AABEpZCpkiAEjKGQrZIgBPUL/3ylkKGSIARJC/9UxACpkEjEAMgkSEUQpZCpkiAD8KmSIAS0iQzYaAIAFc2V0dXASQACSNhoAgANiaWQSQAABADIKKWRwADUBNQA0ATQAIw0QJwRkMgcOEDIHJwVkDBAxFiIJOBAiEhAxFiIJOAAxABIQMRYiCTgHMgoSEDEWIgk4CDIADxBEMRYiCTgIK2QnB2QID0AAAiNDKGQyAxNAABorMRYiCTgIZygxFiIJOABnJwgnCGQiCGciQyhkK2SIAHlC/9wyBycEZAxEsSSyEClkshEyCrIUsyJDKjYaAGcpNhoBF2cnBDYaAhdnJwU2GgMXZycGNhoEF2cnBzYaBRdnKDIDZzIHNhoCFww2GgIXNhoDFwwQRCJDNQM1AjIKNAJwADUFNQQ0BUEADbEkshA0ArIRNAOyFbOJNQc1BrEishA0BzIACbIINAayB7OJNQgyCmAjE0EACbEishA0CLIJs4k=')


    def test_teal_compiler(self):
        with open('./main/fixtures/teal') as file:
            compiled_code = TealCompiler().compile(file.read())
            self.assertEqual(compiled_code, 'BSADAQAEJgkLYmlkX2FjY291bnQGbmZ0X2lkBnNlbGxlcgpiaWRfYW1vdW50BXN0YXJ0A2VuZA5yZXNlcnZlX2Ftb3VudAttaW5fYmlkX2luYwhudW1fYmlkczEYIxJAAUIxGSMSQACFMRmBBRJAABUxGSISMRmBAhIRMRkkEhFAAAEAI0MyBycEZAxAAEUnBWQyBw5AAAIjQyhkMgMTQAAOKWQqZIgBOipkiAFrIkMrZCcGZA9AABEpZCpkiAEjKGQrZIgBPUL/3ylkKGSIARJC/9UxACpkEjEAMgkSEUQpZCpkiAD8KmSIAS0iQzYaAIAFc2V0dXASQACSNhoAgANiaWQSQAABADIKKWRwADUBNQA0ATQAIw0QJwRkMgcOEDIHJwVkDBAxFiIJOBAiEhAxFiIJOAAxABIQMRYiCTgHMgoSEDEWIgk4CDIADxBEMRYiCTgIK2QnB2QID0AAAiNDKGQyAxNAABorMRYiCTgIZygxFiIJOABnJwgnCGQiCGciQyhkK2SIAHlC/9wyBycEZAxEsSSyEClkshEyCrIUsyJDKjYaAGcpNhoBF2cnBDYaAhdnJwU2GgMXZycGNhoEF2cnBzYaBRdnKDIDZzIHNhoCFww2GgIXNhoDFwwQRCJDNQM1AjIKNAJwADUFNQQ0BUEADbEkshA0ArIRNAOyFbOJNQc1BrEishA0BzIACbIINAayB7OJNQgyCmAjE0EACbEishA0CLIJs4k=')


    def test_verification_fetch_onchain_code(self):
        verifier = Verification()
        onchain_code = verifier.fetch_onchain_code('94709007')

        self.assertEqual(onchain_code.get('app_clear'), 'BYEB')
        self.assertEqual(onchain_code.get('app_approval'), 'BSAHAAEEBQJlZiYRC3F1b3RlX2Fzc2V0BWZlZV9uBWZlZV9kCnRyYWRlX3R5cGUFb3duZXIFYWRtaW4OdG90YWxfcXVhbnRpdHkDZmVlEWV4ZWN1dGVkX3F1YW50aXR5B2NyZWF0b3IKYWxnb18yX2FzYQphc2FfMl9hbGdvCWFzYV8yX2FzYQpiYXNlX2Fzc2V0CHRyZWFzdXJ5B3ByaWNlX24HcHJpY2VfZCI1CTQJOCAyAxJENAkjCDUJNAkyBAxA/+oiMRgSQAAlMRkiEkAA5zEZIxJAADcxGSEEEkABhDEZJBJAAqoxGSUSQALFACcJMQBnJw42HAFnJwU2HAJnKTYaABdnKjYaARdnQgKuJwo2GgASQAATJws2GgASQAAtJww2GgASQAAkADMACIGwtjwJNQAiJwY0AGY0AClkCypkCjUBIicHNAFmQgAbIicGMwMSZjMDEilkCypkCjUAIicHNABmQgAAIis2GgMXZiIrYiEFEiIrYiEGEhFENhoBFyINRDYaAhciDUQiJwQzAABmIicPNhoBF2YiJxA2GgIXZiInDTYwAGYiKDYwAWYiJwgiZkICBScKNhoAEkAAEycLNhoAEkAAIycMNhoAEkAANAAzAQg1MjMCEjUzMwMINTQzAhEiKGISQgAsMwESNTIzAgg1MzMDEjU0MwERIihiEkRCABIzARI1MjMCEjUzMwMSNTRCALYkNcgiJwRiMwIHEiInBGIzAhQSEUQiJwhiNQAiJwZiNAAJNDI0NAgNRCInB2I0NAk1ASInBzQBZjQANDIINDQINQEiJwg0AWZCANYnCjYaABJAABMnCzYaABJAACcnDDYaABJAADsAMwEINTIzAhI1MzMDCDU0JDXIMwIRIihiEkRCAHkzARI1MjMCCDUzMwMSNTQlNcgzAREiKGISREIAXDMBEjUyMwISNTMzAxI1NCU1yEIAACIrYiEFEiIoYjMBERIQIicNYjMCERIQIitiIQYSIicNYjMBERIQIihiMwIREhARMwERMwIRExBEMRkhBBJAAAcxGSISQP8DIicEYjMCBxIiJwRiMwIUEhEiJwZiIicIYgk0MjQ0CBIQQgAANMg4ECMSNMg4CCISEDTIOAkyAxIQNMg4ACcFZBIQNMg4BycFZBIQRDQyIicPYh01AjUBNDMiJxBiHTUENQM0ATQDEkQ0MjQ0CClkCypkCjQ0EkRCAC0AJwlkMQASRCcONhwBZycFNhwCZyk2GgAXZyo2GgEXZ0IACicJZDEAEkRCAAAjQyJD')

    def test_verification_pyteal_verify_contract(self):
        with open('./main/fixtures/index.py') as file:
            compiled_code = PyTealCompiler().compile(file.read(), { 'version': 5 })

            verifier = Verification()
            verified  = verifier.verify_contract('102166220', compiled_code=compiled_code)
            self.assertTrue(verified)
        