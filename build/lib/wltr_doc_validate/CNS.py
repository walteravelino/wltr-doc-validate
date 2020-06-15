from .BaseDoc import BaseDoc
from random import sample


class CNS(BaseDoc):

    def __init__(self):
        self.digits = list(range(10))
        self.first_digit = [1, 2, 7, 8, 9]

    def validate(self, doc: str = '') -> bool:
        doc = list(self._only_digits(doc))

        if len(doc) != 15 or int(doc[0]) not in self.first_digit:
            return False

        return self._check_cns_valid(doc)

    def _validate_first_case(self, doc: list) -> bool:
        cns = self._generate_first_case(doc)

        return cns == doc

    def _validate_second_case(self, doc: list) -> bool:
        sum = self._sum_algorithm(doc)

        return sum % 11 == 0

    def generate(self, mask: bool = False) -> str:
        cns = [str(sample(self.first_digit, 1)[0])]

        if cns[0] in ['1', '2']:
            cns = self._generate_first_case(cns, True)
        else:
            cns = self._generate_second_case(cns)

        cns = "".join(cns)

        return self.mask(cns) if mask else cns

    def mask(self, doc: str = '') -> str:
        return "{} {} {} {}".format(doc[:3], doc[3:7], doc[7:11], doc[-4:])

    def _generate_first_case(self, cns: list, generate_random=False) -> list:
        if generate_random:
            cns = cns + [str(sample(self.digits, 1)[0]) for i in range(10)]
        else:
            cns = cns[:11]

        sum = self._sum_algorithm(cns, 11)

        dv = 11 - (sum % 11)

        if dv == 11:
            dv = 0

        if dv == 10:
            sum += 2
            dv = 11 - (sum % 11)
            cns = cns + ['0', '0', '1', str(dv)]
        else:
            cns = cns + ['0', '0', '0', str(dv)]

        return cns

    def _generate_second_case(self, cns: list) -> list:
        cns = cns + [str(sample(list(range(10)), 1)[0]) for i in range(14)]
        sum = self._sum_algorithm(cns)
        rest = sum % 11

        if rest == 0:
            return cns

        diff = 11 - rest

        return self._change_cns(cns, 15 - diff, diff)

    def _change_cns(self, cns: list, i: int, val: int) -> list:
        if val == 0:
            if self._check_cns_valid(cns):
                return cns
            else:
                sum = self._sum_algorithm(cns)
                diff = 15 - (sum % 11)
                return self._change_cns(cns, 15 - diff, diff)

        if 15 - i > val:
            i += 1
            return self._change_cns(cns, i, val)

        if not cns[i] == '9':
            cns[i] = str(int(cns[i]) + 1)
            val -= (15 - i)
        else:
            val += (15 - i)
            cns[i] = str(int(cns[i]) - 1)
            i -= 1

        return self._change_cns(cns, i, val)

    def _sum_algorithm(self, cns: list, n: int = 15) -> int:
        sum = 0
        for i in range(n):
            sum += int(cns[i]) * (15 - i)

        return sum

    def _check_cns_valid(self, cns: list) -> bool:
        if cns[0] in ['1', '2']:
            return self._validate_first_case(cns)
        else:
            return self._validate_second_case(cns)
