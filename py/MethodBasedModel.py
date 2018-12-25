def test_read_write_field():
    class A(object):
        pass

    obj = A()
    obj.a = 1
    assert obj.a == 1

    obj.b = 5
    assert obj.a == 1
    assert obj.b == 5

    obj.a = 2
    assert obj.a == 2
    assert obj.b == 5

    # Object model code
    A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("a", 1)
    assert obj.read_attr("a") == 1

    obj.write_attr("b", 5)
    assert obj.read_attr("a") == 1
    assert obj.read_attr("b") == 5

    obj.write_attr("a", 2)
    assert obj.read_attr("a") == 2
    assert obj.read_attr("b") == 5


class Base(object):
    """The base class that all of the object model classes inherit from."""

    def __init__(self, cls, fields):
        """Every object has a class."""
        self.cls = cls
        self._fields = fields

    def read_attr(self, fieldname):
        """read field 'fieldname' out of thr object"""
        return self._read_dict(fieldname)

    def write_attr(self, fieldname, value):
        """write field 'fieldname' into the object."""
        self._write_dict(fieldname, value)

    def isintance(self, cls):
        """return True if the object is an instance of class cls"""
        return self.cls.issubclass(cls)

    def callmethod(self, methname, *args):
        """call method 'methname' with arguments 'args' on object"""
        meth = self.cls._read_from_class(methname)
        return meth(self, *args)

    def _read_dict(self, fieldname):
        """read an field 'fieldname' out of the object's dict """
        return self._fields.get(fieldname, MISSING)

    def _write_dict(self, fieldname, value):
        """write a field 'fieldname' out of the object's dict """
        self._fields[fieldname] = value


MISSING = object()


class Instance(Base):
    """Instance of a user-defined class."""

    def __init__(self, cls):
        assert isinstance(cls, Class)
        Base.__init__(self, cls, {})


class Class(Base):
    """A User-defined class."""

    def __init__(self, name, base_class, fields, metaclass):
        Base.__init__(self, metaclass, fields)
        self.name = name
        self.base_class = base_class


# set up the base hierachy as in Python (the ObjVLisp model)
# the ultimate base class is OBJECT
OBJECT = Class(name="object", base_class=None, fields={}, metaclass=None)
# TYPE is a subclass of OBJECT
TYPE = Class(name="TYPE", base_class=OBJECT, fields={}, metaclass=None)
# TYPE is an instance of itself
TYPE.cls = TYPE
# OBJECT is an instance of TYPE
OBJECT.cls = TYPE


def test_read_write_field_class():
    """
    classes are objects too,
    Python code
    """

    class A(object):
        pass

    A.a = 1
    assert A.a == 1
    A.a = 6
    assert A.a == 6

    # object model code
    A = Class(name="A", base_class=OBJECT, fields={"a": 1}, metaclass=TYPE)
    assert A.read_attr("a") == 1
    A.write_attr("a", 5)
    assert A.read_attr("a") == 5


def test_isinstance():
    """Python code"""

    class A(object):
        pass

    class B(A):
        pass

    b = B()
    assert isinstance(b, B)
    assert isinstance(b, A)
    assert isinstance(b, object)
    assert not isinstance(b, type)

    # object model code
    A = Class(name="A", base_class=OBJECT, fields={}, metaclass=TYPE)
    B = Class(name="B", base_class=A, fields={}, metaclass=TYPE)
    b = Instance(B)
    assert b.isintance(B)
    assert b.isintance(A)
    assert b.isintance(OBJECT)
    assert not b.isintance(TYPE)


class Class(Base):
    ...

    def method_resolution_order(self):
        """compute the method resolution order of the class"""
        if self.base_class is None:
            return [self]
        else:
            return [self] + self.base_class.method_resolution_order()

    def issubclass(self, cls):
        """is self a subclass of cls"""
        return cls in self.method_resolution_order()


def test_callmethod_simple():
    '''python code'''

    class A(object):
        def f(self):
            return self.x + 1

    obj = A()
    obj.x = 1
    assert obj.f() == 2

    class B(A):
        pass

    obj = B()
    obj.x = 1
    assert obj.f() == 2  # works on subclass too

    '''Object model code'''

    def f_A(self):
        return self.read_attr("x") + 1

    A = Class(name="A", base_class=OBJECT, fields={"f": f_A}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("x", 1)
    assert obj.callmethod("f") == 2

    b = Class(name="B", base_class=A, fields={}, metaclass=TYPE)
    obj = Instance(B)
    obj.write_attr("x", 2)
    assert obj.callmethod("f") == 3


class Class(Base):
    ...


def _read_from_class(self, methname):
    for cls in self.method_resolution_order():
        if methname in cls.fields:
            return cls.fields(methname)
        return MISSING


def test_callmeethod_subclassing_and_arguments():
    '''Python code'''

    class A(object):
        def g(self, arg):
            return self.x + arg

    obj = A()
    obj.x = 1
    assert obj.g(4) == 5

    class B(A):
        def g(self, arg):
            return self.x + arg * 2

    obj = B()
    obj.x = 4
    assert obj.g(4) == 12

    # Object model code
    def g_A(self, arg):
        return self.read_attr("x") + arg

    A = Class(name="A", base_class=OBJECT, fields={"g": g_A}, metaclass=TYPE)
    obj = Instance(A)
    obj.write_attr("x", 1)
    assert obj.callmethod("g", 4) == 5

    def g_B(self, arg):
         return self.read_attr("x") + arg * 2

    B = Class(name="B", base_class=A, fields={"g": g_B}, metaclass=TYPE)
    obj = Instance(B)
    obj.write_attr("x", 4)
    assert obj.callmethod("g", 4) == 12
