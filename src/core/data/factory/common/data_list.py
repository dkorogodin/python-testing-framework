class DataList:
    """
    Base class for a list-based data factory.
    Implementations should provide a `get_all()` method that returns a list of items.
    """

    def get_all(self):
        raise NotImplementedError
