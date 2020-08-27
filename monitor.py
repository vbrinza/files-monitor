import glob
import json_logging
import logging
import sys
import time
import os


def load_config(config_property):
    try:
        return os.environ[config_property]
    except KeyError:
        print(f"Please set the {config_property} first")
        sys.exit(1)


if __name__ == "__main__":
    check_interval = load_config("CHECK_INTERVAL")
    monitored_paths_tmp = load_config("MONITORED_PATHS")
    monitored_paths = monitored_paths_tmp.split()
    json_logging.init_non_web(enable_json=True)
    logger = logging.getLogger("path-monitor")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.info(f"Check interval is {check_interval}")
    while True:
        time.sleep(int(check_interval))
        for path in monitored_paths:
            if os.path.exists(path):
                files = glob.glob(path + '/' + '*', recursive=True)
                if files:
                    logger.info(f"{path} Folder is not empty")
                    logger.info(f"Total files in {path} : {str(len(files))}")
                    logger.info(files)
            else:
                logger.error(f"{path} path does not exist")
