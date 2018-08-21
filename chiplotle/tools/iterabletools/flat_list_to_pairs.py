from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import zip
from future import standard_library

standard_library.install_aliases()


def flat_list_to_pairs(lst):
    """Returns a list of pairs created from consecutive elements of the given
    flat list `lst`.

    Example::

        >>> flat_list_to_pairs([1,2,3,4,5,6])
        [(1, 2), (3, 4), (5, 6)]
        """

    if len(lst) % 2 != 0:
        raise ValueError("List must have a pair number of elements.")

    result = []
    for x, y in zip(lst[0:-1:2], lst[1::2]):
        result.append((x, y))
    return result
