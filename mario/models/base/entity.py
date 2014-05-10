class EntityModel(object):
    """The base class of entity model."""

    key_fields = ['id']

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.id == other.id

    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.id != other.id

    def __hash__(self):
        return hash((self.__class__, self.id))

    def __str__(self):
        instance_label = '{class_}:{id_} at {hex_}'.format(
            class_=self.__class__.__name__, id_=self.id, hex_=hex(id(self)))
        field_labels = ['%s:%s' % (name, get_attr_repr(self, name))
                        for name in self.key_fields if name != 'id']

        sum_len = sum(len(label) for label in [instance_label] + field_labels)
        if sum_len > 55:
            joined_label = '\n    '.join([''] + field_labels)
        else:
            joined_label = ' '.join([''] + field_labels)

        return '<{0}{1}>'.format(instance_label, joined_label)

    def __unicode__(self):
        return str(self).decode('utf-8')

    def __repr__(self):
        fields = ['%s=%s' % (name, get_attr_repr(self, name))
                  for name in self.key_fields]
        return '{0}({1})'.format(self.__class__.__name__, ', '.join(fields))


def human_readable_repr(value):
    """The ``repr`` alternative implementation which show string literal as
    human-readable format just like the Python 3.
    """
    if isinstance(value, bytes):
        return "b'%s'" % value
    if isinstance(value, unicode):
        return "u'%s'" % value.encode('utf-8')
    return repr(value)


def get_attr_repr(instance, name):
    value = getattr(instance, name, NotImplemented)
    return human_readable_repr(value)
