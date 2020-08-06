import random

from faker import Faker

from .vcr import vcr

fake = Faker(locale='pt_BR')


@vcr.use_cassette()
def generate_address():
    addr, district, complement = fake.address().replace('-', '').split('\n')
    number = ''
    if ',' in addr:
        addr, number = addr.split(',')

    data = {
        'address_street': addr,
        'address_number': number,
        'address_zip_code': complement[:8],
        'address_district': district,
        'address_city': complement[9:][:-5],
        'address_state': complement[-2:]
    }
    return data


def generate_cpf():
    cpf = [random.randint(0, 9) for x in range(9)]

    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11

        cpf.append(11 - val if val > 1 else 0)

    return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)


def generate_cnpj():
    def calculate_special_digit(l):
        digit = 0

        for i, v in enumerate(l):
            digit += v * (i % 8 + 2)

        digit = 11 - digit % 11

        return digit if digit < 10 else 0

    cnpj = [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]

    for _ in range(2):
        cnpj = [calculate_special_digit(cnpj)] + cnpj

    return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])


address_data = generate_address()
