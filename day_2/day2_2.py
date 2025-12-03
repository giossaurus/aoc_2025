# --- Part Two ---
# The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

# From the same example as before:

# 11-22 still has two invalid IDs, 11 and 22.
# 95-115 now has two invalid IDs, 99 and 111.
# 998-1012 now has two invalid IDs, 999 and 1010.
# 1188511880-1188511890 still has one invalid ID, 1188511885.
# 222220-222224 still has one invalid ID, 222222.
# 1698522-1698528 still contains no invalid IDs.
# 446443-446449 still has one invalid ID, 446446.
# 38593856-38593862 still has one invalid ID, 38593859.
# 565653-565659 now has one invalid ID, 565656.
# 824824821-824824827 now has one invalid ID, 824824824.
# 2121212118-2121212124 now has one invalid ID, 2121212121.
# Adding up all the invalid IDs in this example produces 4174379265.

# What do you get if you add up all of the invalid IDs using these new rules?

def is_repeated_pattern(product_id):
    """
    Verifica se um ID é formado por um padrão repetido PELO MENOS 2 vezes.

    A estratégia é: testar todos os tamanhos possíveis de padrão.
    Se o ID tem 6 dígitos, testamos padrões de tamanho 1, 2 e 3.
    (tamanhos maiores que a metade não fazem sentido)

    Exemplos detalhados:
        111 (3 dígitos):
            - Testa padrão tamanho 1: "1" * 3 = "111" ✓ MATCH! → INVÁLIDO

        123123 (6 dígitos):
            - Testa padrão tamanho 1: "1" * 6 = "111111"  não bate
            - Testa padrão tamanho 2: "12" * 3 = "121212"  não bate
            - Testa padrão tamanho 3: "123" * 2 = "123123" ✓ MATCH! → INVÁLIDO

        1234 (4 dígitos):
            - Testa padrão tamanho 1: "1" * 4 = "1111"  não bate
            - Testa padrão tamanho 2: "12" * 2 = "1212" não bate
            - Nenhum match → VÁLIDO

    Args:
        product_id: O número do ID a ser verificado

    Returns:
        True se o ID tem padrão repetido (é INVÁLIDO)
        False se o ID não tem padrão repetido (é VÁLIDO)
    """
    id_as_string = str(product_id)
    total_length = len(id_as_string)

    # Testa todos os tamanhos possíveis de padrão
    # Exemplo: se o ID tem 6 dígitos, testa padrões de tamanho 1, 2 e 3
    # (não precisa testar 4, 5 ou 6 porque não daria pelo menos 2 repetições)
    for pattern_size in range(1, total_length // 2 + 1):

        # O padrão só funciona se o tamanho total for divisível pelo tamanho do padrão
        # Exemplo: 7 dígitos com padrão de tamanho 2 não funciona (7 não é divisível por 2)
        if total_length % pattern_size != 0:
            continue  # Pula para o próximo tamanho

        # Pega o padrão (os primeiros N caracteres)
        pattern = id_as_string[:pattern_size]

        # Calcula quantas vezes o padrão deveria repetir
        num_repetitions = total_length // pattern_size

        # Reconstrói o ID usando o padrão repetido
        reconstructed = pattern * num_repetitions

        # Se o ID reconstruído é igual ao original, encontramos um padrão!
        if reconstructed == id_as_string:
            return True  # É INVÁLIDO!

    # Se nenhum padrão funcionou, é VÁLIDO
    return False


def find_and_sum_invalid_ids(id_ranges):
    """
    Procura todos os IDs inválidos nos ranges fornecidos e soma eles.

    Args:
        id_ranges: Lista de strings no formato "inicio-fim" (ex: ["11-22", "95-115"])

    Returns:
        A soma de todos os IDs inválidos encontrados
    """
    total_sum = 0
    invalid_ids_found = []  # Para debug

    for range_string in id_ranges:
        # Remove espaços e pula ranges vazios
        range_string = range_string.strip()
        if not range_string:
            continue

        # Separa o range "11-22" em start=11 e end=22
        start_id, end_id = range_string.split('-')
        start_id = int(start_id)
        end_id = int(end_id)

        # Testa cada ID nesse range
        for current_id in range(start_id, end_id + 1):
            if is_repeated_pattern(current_id):
                total_sum += current_id
                invalid_ids_found.append(current_id)

    # Debug: mostra quantos IDs inválidos foram encontrados
    print(f"Total de IDs inválidos encontrados: {len(invalid_ids_found)}")

    # Se não for muito, mostra alguns exemplos
    if len(invalid_ids_found) <= 30:
        print(f"IDs inválidos: {invalid_ids_found}")
    else:
        print(f"Primeiros 10 IDs inválidos: {invalid_ids_found[:10]}")
        print(f"Últimos 10 IDs inválidos: {invalid_ids_found[-10:]}")

    return total_sum


def test_examples():
    """
    Testa alguns exemplos para garantir que a lógica está correta.
    """
    print("="*60)
    print("TESTANDO EXEMPLOS:")
    print("="*60)

    test_cases = [
        # (ID, esperado_invalido, descrição)
        (11, True, "11 = '1' * 2"),
        (99, True, "99 = '9' * 2"),
        (111, True, "111 = '1' * 3"),
        (6464, True, "6464 = '64' * 2"),
        (123123123, True, "123123123 = '123' * 3"),
        (1111111, True, "1111111 = '1' * 7"),
        (1212121212, True, "1212121212 = '12' * 5"),
        (565656, True, "565656 = '56' * 3"),
        (123, False, "123 não tem padrão"),
        (1234, False, "1234 não tem padrão"),
        (101, False, "101 não tem padrão"),
    ]

    all_passed = True
    for id_num, expected_invalid, description in test_cases:
        result = is_repeated_pattern(id_num)
        status = "✓ PASS" if result == expected_invalid else "✗ FAIL"
        all_passed = all_passed and (result == expected_invalid)
        print(f"{status} | ID {id_num:>10} | Inválido? {result:5} | {description}")

    print("="*60)
    if all_passed:
        print("✓ TODOS OS TESTES PASSARAM!")
    else:
        print("✗ ALGUNS TESTES FALHARAM!")
    print("="*60)
    print()


if __name__ == "__main__":
    # Primeiro, roda os testes para validar a lógica
    test_examples()

    # Lê o arquivo com os ranges
    with open("day2_input.txt") as f:
        input_data = f.read().strip()

    # Separa os ranges pela vírgula
    ranges_list = input_data.split(',')

    # Calcula o resultado
    print("\nPROCESSANDO OS RANGES DO ARQUIVO...")
    print("="*60)
    result = find_and_sum_invalid_ids(ranges_list)

    print("="*60)
    print(f"\n🎯 RESPOSTA FINAL: {result}")
    print("="*60)
