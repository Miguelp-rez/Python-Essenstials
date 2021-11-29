# Section two: platform module

from platform import platform, machine, processor, system, version
from platform import python_implementation, python_version_tuple

# If terse = True, it may show only summary information
# If aliased = True, it may show uses aliases
platform(aliased = False, terse = False)

print(platform())
print(platform(1))
print(platform(0, 1))

# This basically shows the generic name of the computer processor
print(machine())

# This shows the full processor name (if possible)
print(processor())

# Generic OS name
print(system())

# OS version
print(version())

# Getting the python implementation
print(python_implementation()) # CPython is the canonical Python branch

# Getting the python version
print(python_version_tuple())
