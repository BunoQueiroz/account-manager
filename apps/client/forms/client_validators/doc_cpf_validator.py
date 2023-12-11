from validate_docbr import CPF


def cpf_validator(cpf_str: str, errors_list):
    cpf = CPF()
    if cpf_str and not cpf.validate(cpf_str):
        errors_list['cpf'] = 'CPF inválido'
