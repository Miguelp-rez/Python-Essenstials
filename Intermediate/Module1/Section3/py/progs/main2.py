import sys

# A package can be distributed as a folder or a zip file, but
# make sure your package is in the path

# Search this folder
sys.path.append("C:/Users/Sindro86/py/packages/") 
# Search this zip file
sys.path.append("C:/Users/Sindro86/py/packages/extrapack.zip")

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())


