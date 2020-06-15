# Wltr Doc Validate
<a href="https://pypi.org/project/wltr-doc-validate/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/wltr-doc-validate">
</a>

[![Build Status](https://travis-ci.com/walteravelino/Projetos.svg?branch=master)](https://travis-ci.com/walteravelino/Projetos)
<img src = "https://img.shields.io/github/languages/top/walteravelino/wltr-doc-validate">
<a href="https://github.com/walteravelino/Projetos/blob/master/LICENSE"><img src = "https://img.shields.io/github/license/walteravelino/Projetos"></a>

## Autor

👤 **Walter Avelino**

- StackOverFlow [@walteravelino](https://stackoverflow.com/users/13001807/walter-avelino)
- Github: [@walteravelino](https://github.com/walteravelino)
- Linkedin: [@walteravelino](https://linkedin.com/in/walter-avelino-434197105)
- DEV: [@walteravelino](https://dev.to/walteravelino)


## 📝 Licença

Copyright © 2020 [Walter Avelino](https://github.com/walteravelino). <br />
Os projetos estão sob a licença [MIT](https://github.com/walteravelino/Projetos/blob/master/LICENSE).

Pacote para validação de documentos

## Instalação do Wltr Doc Validate

Para instalar o pacote:

```bash
pip install wltr-doc-validate
```

# Métodos
Os documentos possuem os mesmos métodos de chamada.

------------
## Validação
Valida o documento passado como argumento. Retorna um `bool`, `True` caso seja válido, `False` caso contrário . Recebe os parâmetros:

| Parâmetro | Tipo | Valor Padrão | Requerido | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `doc` | `str`| `''` | X | O documento a ser validado. |

```python
from wltr_doc_validate import CPF

cpf = CPF()

# Validar CPF
cpf.validate("012.345.678-90")  # True
cpf.validate("012.345.678-91")  # False
```

### Caso Especial de CPF
Os CPFs de 000.000.000-00 até 999.999.999-99 são considerados válidos pois, em alguns casos, existem pessoas vinculadas a eles. Foi utilizada a base de dados [Coleção de CNPJs e CPFs brasileiros do Brasil.IO](https://brasil.io/dataset/documentos-brasil/documents) para verificar esses documentos:

| CPF | Pessoa | Consulta |
| --- | ------ | -------- |
| 000.000.000-00 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=00000000000&document_type=CPF&document=&name=&sources=` |
| 111.111.111-11 | AKA CENTRAL PARK - NEW YORK | `https://brasil.io/dataset/documentos-brasil/documents?search=11111111111&document_type=CPF&document=&name=&sources=` |
| 222.222.222-22 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=22222222222&document_type=CPF&document=&name=&sources=` |
| 333.333.333-33 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=33333333333&document_type=CPF&document=&name=&sources=` |
| 444.444.444-44 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=44444444444&document_type=CPF&document=&name=&sources=` |
| 555.555.555-55 | ISAEL HERMINIO DA SILVA | `https://brasil.io/dataset/documentos-brasil/documents?search=55555555555&document_type=CPF&document=&name=&sources=` |
| 666.666.666-66 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=66666666666&document_type=CPF&document=&name=&sources=` |
| 777.777.777-77 | ANTONIO GONÇALO DA SILVA | `https://brasil.io/dataset/documentos-brasil/documents?search=77777777777&document_type=CPF&document=&name=&sources=` |
| 888.888.888-88 | - | `https://brasil.io/dataset/documentos-brasil/documents?search=88888888888&document_type=CPF&document=&name=&sources=` |
| 999.999.999-99 | JOAQUIM ROCHA MATOS | `https://brasil.io/dataset/documentos-brasil/documents?search=99999999999&document_type=CPF&document=&name=&sources=` |

Para não validar esses CPFs, utilize o parâmetro `repeated_digits` (por padrão é `False`) da classe `CPF` ou mudar a variável de mesmo nome no objeto criado.
```python
from wltr_doc_validate import CPF

cpf = CPF(repeated_digits=True)

# Validar CPF
cpf.validate("111.111.111-11")  # True

# Não aceitando entradas de 000.000.000-00 até 999.999.999-99
cpf.repeated_digits = False

# Validar CPF
cpf.validate("111.111.111-11")  # False
```

------------
## Validar uma Lista

Valida uma lista de documentos passado como argumento. Retorna uma lista de `bool`, `True` caso seja válido, `False` caso contrário. Recebe os parâmetros:

| Parâmetro | Tipo | Valor Padrão | Requerido | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `docs` | `List[str]`| `[]` | X | A lista de documentos para validar. |

```python
from wltr_doc_validate import CPF

cpf = CPF()

# Validar CPFs
cpf.validate_list(["012.345.678-90", "012.345.678-91"])  # [True, False]
```

------------
## Gerar Documento
Gera um novo documento, retorna em formato de `str`. Recebe os parâmetros:

| Parâmetro | Tipo | Valor Padrão | Requerido | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `mask` | `bool` | `False` | - | Quando possui o valor `True`, o documento retornado estará formatado. |

```python
from wltr_doc_validate import CPF

cpf = CPF()

# Gerar novo CPF
new_cpf_one = cpf.generate()  # "01234567890"
new_cpf_two = cpf.generate(True)  # "012.345.678-90"
```

------------
## Gerar Lista de Documentos
Gera uma lista de documentos `list` com elementos `str`. Aceita os parâmetros:

| Parâmetro | Tipo | Valor Padrão | Requerido | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `n` | `int` | `1` | X | Quantidade de documentos que serão gerados. |
| `mask` | `bool` | `False` | - | Aplicar máscara aos documentos gerados. |
| `repeat` | `bool` | `False` | - | Aceitar repetiçõe de documentos. |

```python
from wltr_doc_validate import CPF

cpf = CPF()

# Gerar lista de CPFs
cpfs_one = cpf.generate_list(2)  # [ "85215667438", "28293145811" ]
cpfs_two = cpf.generate_list(2, True)  # [ "852.156.674-38", "282.931.458-11" ]
```

------------
## Máscara
Aplicar mascára ao documento passado como argumento. Retorna o domumento mascarado como `str`. Aceita os parâmetros:

| Parâmetro | Tipo | Valor Padrão | Requerido | Descrição |
| --------- | ---- | ----------- | ------------ | --------- |
| `doc` | `str`| `''` | X | Documento que receberá a máscara. |

```python
from wltr_doc_validate import CPF

cpf = CPF()

cpf_me = "01234567890"

# Mascara o CPF
cpf.mask(cpf_me)  # "012.345.678-90"
```
