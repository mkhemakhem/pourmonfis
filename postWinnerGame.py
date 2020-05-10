import shutil
import subprocess
import grilles

shutil.copyfile('data/gagant1.data', 'data/gagant12.data')
subprocess.call(["sed -i -e 's/1/X/g' data/gagant12.data"], shell=True)
subprocess.call(["sed -i -e 's/2/1/g' data/gagant12.data"], shell=True)
subprocess.call(["sed -i -e 's/X/2/g' data/gagant12.data"], shell=True)



shutil.copyfile('data/gagant2.data', 'data/gagant21.data')
subprocess.call(["sed -i -e 's/1/X/g' data/gagant21.data"], shell=True)
subprocess.call(["sed -i -e 's/2/1/g' data/gagant21.data"], shell=True)
subprocess.call(["sed -i -e 's/X/2/g' data/gagant21.data"], shell=True)

grilles.agrege()
subprocess.call(["rm -f data/gagant21.data"], shell=True)
subprocess.call(["rm -f data/gagant12.data"], shell=True)
