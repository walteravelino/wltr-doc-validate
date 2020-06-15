from abc import ABC
from typing import List


class BaseDoc(ABC):
    """Classe base para as classes CNH, CNPJ, CNS, CPF, PIS, TituloEleitoral, RGSSP"""

    def validate(self, doc: str = '') -> bool:
        # Método para validar o documento desejado
        pass

    def validate_list(self, docs: List[str]) -> List[bool]:
        return [self.validate(doc) for doc in docs]

    def generate(self, mask: bool = False) -> str:
        pass

    def generate_list(self, n: int = 1, mask: bool = False, repeat: bool = False) -> list:
        doc_list = []

        if n <= 0:
            return doc_list

        for i in range(n):
            doc_list.append(self.generate(mask))

        while not repeat:
            doc_set = set(doc_list)
            unique_values = len(doc_set)

            if unique_values < n:
                doc_list = list(doc_set) + self.generate_list((n - unique_values), mask, repeat)
            else:
                repeat = True

        return doc_list

    def mask(self, doc: str = '') -> str:
        pass

    def _only_digits(self, doc: str = '') -> str:
        return "".join([x for x in doc if x.isdigit()])
