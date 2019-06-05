import logging, os, sys
from pathlib import Path

def handler_stop_signals(signum, frame):
    logging.info("Caught Terminate signal - exiting")
    logging.debug("Signal %d received" % signum)
    sys.exit(0)

if __name__ == "__main__":
    print("This file is not meant to be run directly")
