import requests
from syscalls import RootModel
import pickle
import os
from pathlib import Path


#for i in range(20):
#    url = ""
#    if i < 4:
#        version = f'v6.' + str(i)
#        url = f'https://syscalls.mebeim.net/db/arm64/64/aarch64/{version}/table.json'
#        response = requests.get(url)
#        rootModel = RootModel(**response.json())
#        serialized = pickle.dumps(rootModel)
#        if not os.path.exists(directory):
#            os.makedirs(directory)
#        with open(f"{version}", "wb") as f:
#            f.write(serialized)
#
#        
#
#    #url = f'https://syscalls.mebeim.net/db/arm64/64/aarch64/v5.{str(i)}/table.json'
#    #requests.get(url)


archs = [
"arm/32/eabi",
"arm/32/oabi",
"arm64/64/aarch32",
"arm64/64/aarch64",
"mips/32/o32",
"mips/64/n32",
"mips/64/n64",
"mips/64/o32",
"x86/32/ia32",
"x86/64/ia32",
"x86/64/x32",
"x86/64/x64"]

for arch in archs:
    directory = Path(arch)
    if not directory.exists():
        directory.mkdir(parents=True)
    for major in range(4, 7):
        for minor in range(20):
            version = f"v{major}.{minor}"
            print(version)
            url = f'https://syscalls.mebeim.net/db/{arch}/{version}/table.json'
            print(url)
            response = requests.get(url)
            if response.status_code == 200:
                rootModel = RootModel(**response.json())
                serialized = pickle.dumps(rootModel)
                with open(f"{os.path.join(directory, version)}", "wb") as f:
                    f.write(serialized)