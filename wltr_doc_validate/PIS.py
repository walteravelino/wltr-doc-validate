from .BaseDoc import BaseDoc
from random import sample
from typing import Union


class PIS(BaseDoc):

    def __init__(self):
        self.digits = list(range(10))

    def validate(self, doc: str = '') -> bool:
        doc = self._only_digits(doc)

        if len(doc) != 11 or self._is_repeated_digits(doc):
            return False

        digit = self._generate_digit(doc)

        return digit == doc[10]

    def generate(self, mask: bool = False) -> str:
        pis = [str(sample(self.digits, 1)[0]) for i in range(10)]
        pis.append(self._generate_digit(pis))

        pis = ''.join(pis)
        return self.mask(pis) if mask else pis

    def mask(self, doc: str = '') -> str:
        return "{}.{}.{}-{}".format(doc[:3], doc[3:8], doc[8:10], doc[10:])

    def _generate_digit(self, doc: Union[str, list]) -> str:
        multipliers = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        summation = 0

        for position in range(0, 10):
            summation += int(doc[position]) * multipliers[position]
        
        module = summation % 11
        digit = 0

        if module >= 2:
            digit = 11 - module

        return str(digit)

    def _is_repeated_digits(self, doc: str) -> bool:
        return len(set(doc)) == 1
