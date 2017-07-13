import collections
import pytest

from tdd import dictregister as dr


def test_init():
    dr.DictRegister()


def test_mutable_sequence():
    # test our class behaves like a mutable sequence (a list)
    assert isinstance(dr.DictRegister(), collections.MutableSequence)


def test_append_works():
    d = dr.DictRegister()

    d.append({'a': 1, 'b': 2})

    assert len(d) == 1
    assert d[0] == {'a': 1, 'b': 2}


def test_append_checks_if_mapping():
    d = dr.DictRegister()

    # if the code raises TypeError exception
    with pytest.raises(TypeError):
        d.append([1, 2, 3, 4])


@pytest.fixture
def simple_dict():
    return {'a': 1, 'b': 2}


def test_init_with_list_of_dicts(simple_dict):
    d = dr.DictRegister([simple_dict])

    assert len(d) == 1


def test_find_single_key():
    d = dr.DictRegister([
        {'a': 1, 'b': 2},
        {'a': 5, 'c': 6},
        {'b': 3, 'c': 9}
    ])

    assert d.find('a') == \
        dr.DictRegister([{'a': 1, 'b': 2}, {'a': 5, 'c': 6}])
