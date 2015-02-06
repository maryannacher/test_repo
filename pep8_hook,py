import test1
import subprocess
import sys

str_error = test1.pep8_error()
list_error = str_error.splitlines( )


def error_string(error):
    spliting = error.split(':')
    zero_elem = spliting[0]
    file_name = zero_elem[2:]
    file_name_slash = file_name.replace('\\','/')
    return file_name_slash


commit = subprocess.check_output(['git','diff','--cached','--name-only'])
commit = commit.splitlines( )

A = False
for i in list_error:
    string_name = error_string(i)
    if string_name in commit:
        A = True
        print (i)

if A:
    sys.exit(1)
