from .BaseDoc import BaseDoc


class RGSSP(BaseDoc):
    def __init__(self):
        self.digits = list(range(10))
        self.dsc = 0

    def rg_validate(rg) -> bool:
        if str(sum(map(lambda x: (x[0] + 2) * int(x[1]),
                       enumerate(rg[-2::-1]))) % 11).replace('10', 'X') == rg[-1].upper():
            return True
        else:
            return False
