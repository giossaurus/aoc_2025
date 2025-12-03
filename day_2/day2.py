# --- Day 2: Gift Shop ---
# You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

# As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

# As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

# They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

# Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.
# Adding up all the invalid IDs in this example produces 1227775554.

# What do you get if you add up all of the invalid IDs?

def is_repeated_pattern(product_id):
    """
    Verifica se um ID é formado por um padrão repetido duas vezes.

    Exemplos:
        11 → "1" + "1" → True (INVÁLIDO)
        6464 → "64" + "64" → True (INVÁLIDO)
        123 → tamanho ímpar → False (VÁLIDO)
        1234 → "12" != "34" → False (VÁLIDO)

    Args:
        product_id: O número do ID a ser verificado

    Returns:
        True se o ID tem padrão repetido (é INVÁLIDO)
        False se o ID não tem padrão repetido (é VÁLIDO)
    """
    id_as_string = str(product_id)
    total_digits = len(id_as_string)

    # Se tem quantidade ímpar de dígitos, não pode ser dividido ao meio
    # Exemplo: "123" tem 3 dígitos, não dá pra dividir em duas partes iguais
    if total_digits % 2 != 0:
        return False

    # Divide ao meio
    middle_point = total_digits // 2
    first_half = id_as_string[:middle_point]    # Primeira metade
    second_half = id_as_string[middle_point:]   # Segunda metade

    # Se as duas metades são iguais, é um padrão repetido (INVÁLIDO)
    return first_half == second_half


def find_and_sum_invalid_ids(id_ranges):
    """
    Procura todos os IDs inválidos nos ranges fornecidos e soma eles.

    Args:
        id_ranges: Lista de strings no formato "inicio-fim" (ex: ["11-22", "95-115"])

    Returns:
        A soma de todos os IDs inválidos encontrados
    """
    total_sum = 0
    invalid_ids_found = []  # Para debug, guarda quais IDs foram encontrados

    for range_string in id_ranges:
        # Separa o range "11-22" em start=11 e end=22
        start_id, end_id = range_string.split('-')
        start_id = int(start_id)
        end_id = int(end_id)

        # Testa cada ID nesse range
        for current_id in range(start_id, end_id + 1):  # +1 porque range() não inclui o último
            if is_repeated_pattern(current_id):
                total_sum += current_id
                invalid_ids_found.append(current_id)

    # Para debug: mostra quantos IDs inválidos foram encontrados
    print(f"Total de IDs inválidos encontrados: {len(invalid_ids_found)}")
    if len(invalid_ids_found) <= 20:  # Se não for muito, mostra quais são
        print(f"IDs inválidos: {invalid_ids_found}")

    return total_sum


if __name__ == "__main__":
    # Lê o arquivo com os ranges
    with open("day2_input.txt") as f:
        input_data = f.read().strip()

    # Separa os ranges pela vírgula
    ranges_list = input_data.split(',')

    # Remove espaços em branco extras (se houver)
    ranges_list = [r.strip() for r in ranges_list if r.strip()]

    # Calcula o resultado
    result = find_and_sum_invalid_ids(ranges_list)

    print(f"\nResposta Final: A soma de todos os IDs inválidos é: {result}")
