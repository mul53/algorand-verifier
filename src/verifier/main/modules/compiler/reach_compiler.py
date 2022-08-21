import os
import re
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve

class ReachCompiler():
    def extract_key_value(self, file_path: str, key: str):
        output = os.popen("awk '/{}/ {{print}}' {}".format(key, file_path)).read()
        return re.search(r'`(.+)`', output).group(1)

    def download_compiler(self, dir_path: str):
        urlretrieve('https://docs.reach.sh/reach', dir_path)
        os.system("chmod +x {}".format(dir_path))

    def compiler_path(self, dir: str):
        return "{}/reach".format(dir)

    def source_path(self, dir: str):
        return "{}/index.rsh".format(dir)

    def build_path(self, dir: str):
        return "{}/build/index.main.mjs".format(dir)

    def write_source(self, source: str, source_path: str):
        f = open(source_path, 'w')
        f.write(source)
        f.close()

    def compile(self, source: str, opts = {}):
        dirname = os.getcwd()
        
        with TemporaryDirectory(dir=dirname) as compile_dir:
            compiler_path = self.compiler_path(compile_dir)
            source_path = self.source_path(compile_dir)
            build_path = self.build_path(compile_dir)

            self.download_compiler(compiler_path)
            self.write_source(source, source_path)
            
            os.chdir("./{}".format(compile_dir.split('/')[-1]))
            os.system("./reach compile")
            os.chdir("../")

            app_approval =  self.extract_key_value(build_path, "appApproval")
            app_clear = self.extract_key_value(build_path, "appClear")

        if app_approval == None:
            raise Exception('Failed to compile')

        if app_clear == None:
            raise Exception('Failed to compile')

        return { 'app_approval': app_approval, 'app_clear': app_clear }
