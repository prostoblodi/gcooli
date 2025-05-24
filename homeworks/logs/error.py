import logging

logging.basicConfig(level=logging.ERROR,
                    filename="logs.log", filemode="a",
                    format="%(asctime)s:%(levelname)s-%(message)s"
                    )

try:
    import verycoollibary
except Exception as e:
    logging.error(e)
