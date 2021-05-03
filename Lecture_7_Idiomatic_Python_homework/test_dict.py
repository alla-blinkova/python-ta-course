import pytest

from bad import create_country_make_dict as bad_dict
from good import create_country_make_dict as good_dict

REQUEST_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_dict_length(dict_func):
    dict_length = len(dict_func(REQUEST_URL))
    assert dict_length == 79, f"Expected length to be 79, but got {dict_length} instead"


@pytest.mark.parametrize(
    "country,result_count",
    [
        ("UNITED STATES (USA)", 14866),
        ("RUSSIA", 22),
    ],
)
def test_dict_content_length(country, result_count):
    actual_dict = good_dict(REQUEST_URL)
    assert (
        len(actual_dict[country]) == result_count
    ), f"Expected length to be {result_count}, but got {len(actual_dict[country])} instead"


def test_dict_content():
    expected_names = ["Kiverco Ltd.", "RJC GLASS LIMITED-TOUGHGLASS"]
    actual_names = bad_dict(REQUEST_URL)["IRELAND"]
    assert all([a == b for a, b in zip(actual_names, expected_names)])
