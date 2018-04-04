from assertpy import assert_that
import pytest

from primes import is_prime


class TestPrimes(object):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        assert_that(is_prime(5)).is_true()

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        assert_that(is_prime(4), 'Four is not prime!').is_false()

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        assert_that(is_prime(0)).is_false()

    @pytest.mark.parametrize('negative', range(-1, -10, -1))
    def test_negative_number(self, negative):
        """Is a negative number correctly determined not to be prime?"""
        assert_that(is_prime(negative), "negatives could never be primes").is_false()
