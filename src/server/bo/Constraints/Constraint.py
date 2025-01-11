from abc import ABC, abstractmethod
# from src.server.bo.BusinessObject import BusinessObject

# unvollständiger Code. Es ist nur da, um die anderen Klassen auf diese zu referieren. Lösche später diesen Kommentar,
# wenn der Code vollständig ist

class Constraint(ABC): # oder BusinessObject, je nachdem.
    def __init__(self):
        pass

    def validate(self):
        pass