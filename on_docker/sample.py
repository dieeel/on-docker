import sys
from on_docker.utils.logger import get_logger


logger = get_logger()


def main() -> None:
    logger.info(f"argv0: {sys.argv[0]}, argv1: {sys.argv[1]}.")


if __name__ == '__main__':
    main()

