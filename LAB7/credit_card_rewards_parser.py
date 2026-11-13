
def mask_card_number(number):
    """
    Hides all but the last four digits of a card number.
    Handles None and unexpected inputs safely.
    """
    if number is None:
        return "************"

    digits = str(number).replace(' ', '').replace('-', '')

    if len(digits) <= 4:
        return "************"

    return '*' * 12 + digits[-4:]


def parse_transaction(line):
    """
    Parses 'date,category,amount' into a (category, amount) tuple.
    Handles missing fields and invalid amounts safely.
    """
    if line is None:
        return ("", 0)

    parts = str(line).split(',')

    if len(parts) < 3:
        return ("", 0)

    category = parts[1].strip().lower()

    try:
        amount = int(parts[2].strip())
    except (ValueError, TypeError):
        return ("", 0)

    return (category, amount)


def parse_statement_total(text):
    """
    Reads the amount from a line such as 'Total: 12,500'.
    Handles missing colons and invalid amounts safely.
    """
    if text is None:
        return 0

    text = str(text)

    if ':' not in text:
        return 0

    amount = text.split(':', 1)[1]
    amount = amount.replace(',', '').strip()

    try:
        return int(amount)
    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running mask_card_number ====")
    value = input(
        "Enter a card number (e.g. 4111 1111 1111 1234): "
    )
    print("Masked card number:", mask_card_number(value))

    print("\n==== Running parse_transaction ====")
    value = input(
        "Enter a transaction as DATE,CATEGORY,AMOUNT "
        "(e.g. 2026-11-05,dining,1550): "
    )
    print("Category and amount:", parse_transaction(value))

    print("\n==== Running parse_statement_total ====")
    value = input(
        "Enter the statement total line (e.g. Total: 12,500): "
    )
    print("Statement total:", parse_statement_total(value))


if __name__ == "__main__":
    main()
