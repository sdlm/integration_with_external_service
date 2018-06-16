import datetime

import re


dateutil_available = False
try:
    from dateutil import parser
    dateutil_available = True
except ImportError:
    dateutil_available = False


# From Django
_iso8601_re = re.compile(
    r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})'
    r'[T ](?P<hour>\d{1,2}):(?P<minute>\d{1,2})'
    r'(?::(?P<second>\d{1,2})(?:\.(?P<microsecond>\d{1,6})\d{0,6})?)?'
    r'(?P<tzinfo>Z|[+-]\d{2}(?::?\d{2})?)?$'
)


def from_iso_datetime(datestring, use_dateutil=True):
    """Parse an ISO8601-formatted datetime string and return a datetime object.

    Use dateutil's parser if possible and return a timezone-aware datetime.
    """
    if not _iso8601_re.match(datestring):
        raise ValueError('Not a valid ISO8601-formatted datetime string')
    # Use dateutil's parser if possible
    if dateutil_available and use_dateutil:
        return parser.parse(datestring)
    else:
        # Strip off timezone info.
        return datetime.datetime.strptime(datestring[:19], '%Y-%m-%dT%H:%M:%S')


def from_iso_time(timestring, use_dateutil=True):
    """Parse an ISO8601-formatted datetime string and return a datetime.time
    object.
    """
    if dateutil_available and use_dateutil:
        return parser.parse(timestring).time()
    else:
        if len(timestring) > 8:  # has microseconds
            fmt = '%H:%M:%S.%f'
        else:
            fmt = '%H:%M:%S'
        return datetime.datetime.strptime(timestring, fmt).time()


def from_iso_date(datestring, use_dateutil=True):
    if dateutil_available and use_dateutil:
        return parser.parse(datestring).date()
    else:
        return datetime.datetime.strptime(datestring[:10], '%Y-%m-%d').date()
