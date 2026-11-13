from hypothesis import given, strategies as st
from credit_card_rewards_parser import mask_card_number, parse_transaction, parse_statement_total

@given(st.text() | st.none())
def test_mask_card_number_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_parse_transaction_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass

@given(st.text() | st.none())
def test_parse_statement_total_no_crash(s):
    # To-Do: Using try and except complete this function.
    pass
