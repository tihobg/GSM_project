class Call:

    def __init__(self,
                 _from,
                 _to,
                 data='',
                 start_time='',
                 duration_time=0):
        self._from = _from
        self._to = _to
        self._data = data
        self._start_time = start_time
        self._duration_time = duration_time

    @property
    def caller(self):
        return self._from

    @property
    def to(self):
        return self._to

    @property
    def data(self):
        return self._data

    @property
    def start_time(self):
        return self._start_time

    @property
    def duration_time(self):
        return self._duration_time