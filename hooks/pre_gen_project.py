#!/usr/bin/env python

"""
Code to run before generating the project.

Adapted from https://github.com/cthoyt/cookiecutter-snekpack/blob/main/hooks/pre_gen_project.py. # noqa: E501
"""

import re
import sys

MODULE_REGEX = re.compile('^[_a-zA-Z][_a-zA-Z0-9]+$')

module_name = '{{ cookiecutter.package_name}}'

if not MODULE_REGEX.match(module_name):
    error_string = ' '.join(
        [
            'ERROR: {module_name} is not a valid Python module name.',
            'Please do not use a - and use _ instead',
        ],
    )

    print(error_string.format(module_name=module_name))  # noqa: WPS421

    # Exit to cancel project
    sys.exit(1)
