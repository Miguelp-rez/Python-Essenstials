# Section 8: useful exceptions

# ImportError
# This exception is raised when an import operations fails

try:
    import cde
except ImportError:
    print('May be wrong module name')
