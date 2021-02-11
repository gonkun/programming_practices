import statsd
import get_prefix


def Counter(name):
    return statsd.Counter("%s.%s" % (get_prefix(), name))
