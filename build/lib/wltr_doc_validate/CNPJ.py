from .BaseDoc import BaseDoc
from random import sample
from typing import Union


class CNPJ(BaseDoc):

    def __init__(self):
        self.digits = list(range(10))
        self.weights_first = list(range(5, 1, -1)) + list(range(9, 1, -1))
        self.weights_second = list(range(6, 1, -1)) + list(range(9, 1, -1))

    def validate(self, doc: str = '') -> bool:
        doc = self._only_digits(doc)

        if len(doc) != 14:
            return False

        for i in range(10):
            if doc.count("{}".format(i)) == 14:
                return False

        return self._generate_first_digit(doc) == doc[12]\
               and self._generate_second_digit(doc) == doc[13]

    def generate(self, mask: bool = False) -> str:
        cnpj = [str(sample(self.digits, 1)[0]) for i in range(12)]

        cnpj.append(self._generate_first_digit(cnpj))
        cnpj.append(self._generate_second_digit(cnpj))

        cnpj = "".join(cnpj)

        return self.mask(cnpj) if mask else cnpj

    def mask(self, doc: str = '') -> str:
        return "{}.{}.{}/{}-{}".format(doc[:2], doc[2:5], doc[5:8], doc[8:12], doc[-2:])

    def _generate_first_digit(self, doc: Union[str, list]) -> str:
        sum = 0

        for i in range(12):
            sum += int(doc[i]) * self.weights_first[i]

        sum = sum % 11

        if sum < 2:
            sum = 0
        else:
            sum = 11 - sum

        return str(sum)

    def _generate_second_digit(self, doc: Union[str, list]) -> str:
        sum = 0

        for i in range(13):
            sum += int(doc[i]) * self.weights_second[i]

        sum = sum % 11

        if sum < 2:
            sum = 0
        else:
            sum = 11 - sum

        return str(sum)
