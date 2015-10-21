# -*- coding: utf-8 -*-

# --------------- basic list serialization ---------------------------------- #
import cPickle
pickled_string = cPickle.dumps([1, 2, 3, "a", "b", "c"])
print cPickle.loads(pickled_string)

