import pytest
from long_common_subseq import get_long_common_subseq



@pytest.mark.parametrize('X,Y, expect', [
    (('A', 'B', 'C', 'B', 'D', 'A', 'B'), 
    ('B', 'D', 'C', 'A', 'B', 'A'), 4),
    ((1, 0, 0, 1, 0, 1, 0, 1),
    (0, 1, 0, 1, 1, 0, 1, 1, 0), 5)]
    )
def test_length_common_subseq(X, Y, expect):
    count = get_long_common_subseq(X, Y)
    assert count == expect
    

if __name__ == '__main__':
    pytest.main('-s')

