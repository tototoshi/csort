__version__ = "0.1.1"

class csort(object):

    def __init__(self, lines, field_indices, delimiter="\t"):
        self._lines = lines
        self._field_indices = field_indices
        self._delimiter = delimiter

    def __iter__(self):
        return self

    def next(self):
        fields = self._csort_fields(self._lines.next(),
                                    self._field_indices)
        return self._delimiter.join(fields)

    def _csort_fields(self, line, field_indices):
        line = line.rstrip()
        fields = line.split(self._delimiter)
        return [fields[index] for index in field_indices]

