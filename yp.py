import argparse
import pprint
import sys

import jmespath
import yaml

USAGE = "Evaluate JMESPath ``expression`` against YAML from stdin."


def main():
    argp = argparse.ArgumentParser(usage=USAGE)
    argp.add_argument('expression')
    sys.stdout.write(
        pprint.pformat(
            jmespath.search(
                argp.parse_args().expression,
                yaml.load(
                    sys.stdin.read()
                )
            )
        )
    )
