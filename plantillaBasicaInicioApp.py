import logging
import sys

print("Esta linea es la primera que se ejecuta")


def main(argv):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"
    )

    log = logging.getLogger(__name__)
    log.info(argv)


"""
By doing the main check, you can have that code only execute when you want to run the module as a program
    python client2.py
and not have it execute when someone just wants to import your module and call your functions themselves.
more info:
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do

Incluso podemos modificar el call a main() para lograr un codigo 100% testeable como propone este articulo
    https://medium.com/opsops/how-to-test-if-name-main-1928367290cb
    https://www.journaldev.com/17752/python-main-function
    https://medium.com/opsops/how-to-test-if-name-main-1928367290cb

"""


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))


init()
