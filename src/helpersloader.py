import os
import sys

from datetime import datetime
from subprocess import Popen

from caches import get_helpers_collection
from caches import clear_helpers_collection

def load_helpers():
    helpers_dir = 'helpers'
    helpers_prefix = 'hlp'

    list_of_helpers = get_helpers_collection()

    helpers = []

    for helper in list_of_helpers:
        if helpers_prefix in helper:
            helpers.append(os.path.abspath(os.path.join(os.path.dirname(__file__), helpers_dir, helper)))

    return helpers

def get_plugin_name(helper: str):
    if isinstance(helper, str):
        return helper.split('/')[-1][:-3]

def run_helpers():
    helpers = load_helpers()
    for helper in helpers:
        print("[h] Run helper: {}".format(helper))

        proc = '{0} {1}'.format(sys.executable, helper)

        plugin_process = Popen(proc, shell=True, preexec_fn=os.setsid).wait()

        print("[h] Complete helper: {}".format(helper))

    clear_helpers_collection()


def test_helpers():
    from caches import push_helpers_collection
    
    collection = [
        "hlp_helper_1.py",
        "hlp_helper_2.py",
        "hlp_helper_3.py"
    ]

    push_helpers_collection(collection)

    run_helpers()

test_helpers()