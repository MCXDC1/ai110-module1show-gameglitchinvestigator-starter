from logic_utils import check_guess, check_in_range, get_range_for_difficulty, parse_guess, update_score
# updated imports for new functions: check_in_range


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


#testing that the ranges are equivalent to what buttons are pressed

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_range_unknown_defaults_to_100():
    assert get_range_for_difficulty("Unknown") == (1, 100)


# value testing

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_empty_string():
    ok, _, err = parse_guess("")
    assert ok is False
    assert err == "Enter a guess."

def test_parse_none():
    ok, _, err = parse_guess(None)
    assert ok is False
    assert err == "Enter a guess."

def test_parse_non_number():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err == "That is not a number."

def test_parse_float_string():
    ok, value, _ = parse_guess("7.9")
    assert ok is True
    assert value == 7



# test ranges, make sure that the correct message is being shown

def test_in_range_valid():
    ok, err = check_in_range(10, 1, 20)
    assert ok is True
    assert err is None

def test_in_range_boundary_low():
    ok, _ = check_in_range(1, 1, 20)
    assert ok is True

def test_in_range_boundary_high():
    ok, _ = check_in_range(20, 1, 20)
    assert ok is True

def test_below_range():
    ok, err = check_in_range(0, 1, 20)
    assert ok is False
    assert "1" in err and "20" in err

def test_above_range():
    ok, err = check_in_range(21, 1, 20)
    assert ok is False
    assert "1" in err and "20" in err

def test_out_of_range_does_not_count_as_attempt():
    _, err = check_in_range(99, 1, 20)
    assert "does not count as an attempt" in err


# testing attempts will win, lose
# testing score

def test_win_on_first_attempt():
    # attempt_number=1: points = 100 - 10*(1+1) = 80
    result = update_score(0, "Win", 1)
    assert result == 80

def test_win_minimum_points():
    # attempt_number=10: 100 - 110 = -10 → clamped to 10
    result = update_score(0, "Win", 10)
    assert result == 10

def test_too_high_even_attempt_adds_points():
    # attempt_number=2 (even): +5
    result = update_score(50, "Too High", 2)
    assert result == 55

def test_too_high_odd_attempt_subtracts_points():
    # attempt_number=3 (odd): -5
    result = update_score(50, "Too High", 3)
    assert result == 45

def test_too_low_subtracts_points():
    result = update_score(50, "Too Low", 1)
    assert result == 45

def test_unknown_outcome_unchanged():
    result = update_score(50, "Something else", 1)
    assert result == 50


