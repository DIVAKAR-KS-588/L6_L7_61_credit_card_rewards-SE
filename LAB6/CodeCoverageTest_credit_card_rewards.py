import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# ---------------------------------
# TESTS FOR REWARD POINTS
# ---------------------------------

def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_gold_grocery():
    assert reward_points("gold", 250, "grocery", False) == 4


def test_platinum_grocery():
    assert reward_points("platinum", 250, "grocery", False) == 8


def test_dining_category():
    assert reward_points("classic", 250, "dining", False) == 4


def test_travel_category():
    assert reward_points("gold", 250, "travel", False) == 8


def test_fuel_category():
    assert reward_points("gold", 500, "fuel", False) == 0


def test_weekend_gold_card():
    assert reward_points("gold", 100, "grocery", True) == 52


def test_weekend_platinum_card():
    assert reward_points("platinum", 100, "grocery", True) == 54


def test_weekend_classic_card():
    assert reward_points("classic", 100, "grocery", True) == 1


def test_unknown_card_tier():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("silver", 1000, "grocery", False)


def test_zero_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("gold", 0, "grocery", False)


def test_negative_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("gold", -100, "grocery", False)


# ---------------------------------
# TESTS FOR LATE PAYMENT FEE
# ---------------------------------

def test_paid_on_time():
    assert late_payment_fee(5000, 0) == 0


def test_zero_outstanding():
    assert late_payment_fee(0, 10) == 0


def test_negative_outstanding():
    assert late_payment_fee(-500, 10) == 0


def test_fee_below_1000():
    assert late_payment_fee(500, 10) == 100


def test_fee_at_1000():
    assert late_payment_fee(1000, 10) == 100


def test_fee_between_1000_and_10000():
    assert late_payment_fee(5000, 10) == 500


def test_fee_at_10000():
    assert late_payment_fee(10000, 10) == 500


def test_fee_above_10000():
    assert late_payment_fee(15000, 10) == 1000


def test_fee_more_than_30_days_late():
    assert late_payment_fee(5000, 31) == 1250


def test_fee_exactly_30_days_late():
    assert late_payment_fee(5000, 30) == 500


# ---------------------------------
# TESTS FOR CARD STATUS
# ---------------------------------

def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"


def test_blocked_card():
    assert card_status(50, 3, False) == "blocked"


def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


def test_watch_high_utilisation():
    assert card_status(50, 0, False) == "watch"


def test_watch_missed_payment():
    assert card_status(20, 1, False) == "watch"


def test_good_card_status():
    assert card_status(20, 0, False) == "good"