from seasons import age_in_mins
import pytest


def test_invalid_date():
    with pytest.raises(SystemExit):
        assert age_in_mins("Harry Potter")
        assert age_in_mins("31-04-2009")
