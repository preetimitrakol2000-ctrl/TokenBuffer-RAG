import ctypes
import os
import sys

class CompactorBridge:
    def __init__(self):
        if not os.path.exists("./libcompactor.so") and not os.path.exists("./libcompactor.dll"):
            if sys.platform.startswith("win"):
                os.system("gcc -shared -o libcompactor.dll token_compactor.c")
                lib_path = "./libcompactor.dll"
            else:
                os.system("gcc -shared -fPIC -o libcompactor.so token_compactor.c")
                lib_path = "./libcompactor.so"
        else:
            lib_path = "./libcompactor.dll" if sys.platform.startswith("win") else "./libcompactor.so"

        self.lib = ctypes.CDLL(lib_path)
        self.lib.init_stack_buffer.restype = ctypes.c_void_p
        self.lib.push_and_compact.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.lib.push_and_compact.restype = ctypes.c_int
        self.lib.expose_prompt.argtypes = [ctypes.c_void_p]
        self.lib.expose_prompt.restype = ctypes.c_char_p
        
        self.buffer_ptr = self.lib.init_stack_buffer()

    def append_context(self, text: str) -> int:
        return self.lib.push_and_compact(self.buffer_ptr, text.encode('utf-8'))

    def retrieve_final_prompt_string(self) -> str:
        return self.lib.expose_prompt(self.buffer_ptr).decode('utf-8')
