from pydantic import BaseModel, Field
from typing import List, Optional

class Syscall(BaseModel):
    esoteric: bool
    file: str
    good_location: bool
    grepped_location: bool
    index: Optional[int]
    kconfig: Optional[str]
    line: Optional[str]
    name: str
    number: int
    origname: str
    signature: Optional[List[str]]
    symbol: str

class KernelABI(BaseModel):
    calling_convention: dict
    name: str

class KernelArchitecture(BaseModel):
    bits: int
    name: str

class Kernel(BaseModel):
    abi: KernelABI
    architecture: KernelArchitecture
    syscall_table_symbol: str
    version: str
    version_source: str

class RootModel(BaseModel):
    kernel: Kernel
    syscalls: List[Syscall]

    class Config:
        allow_population_by_field_name = True
