import argparse
import logging
import pkgutil


def main():
    """Entry point"""
    parser = argparse.ArgumentParser(prog="learn_python_by_test")
    version = pkgutil.get_data(__package__, "VERSION.txt").decode(encoding="utf-8")
    parser.add_argument ("-v", "--version", action="version", version=version)
    levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
    parser.add_argument('--log-level', help="setting logging level", default='INFO', choices=levels)

    args = parser.parse_args()

    logging.basicConfig(level=args.log_level, format='%(levelname)s:%(name)s:%(message)s')


if __name__ == "__main__":
    main()
