class DataItem:
    """
    Base class for a single data item factory.
    Implementations should provide a `get()` method that returns the item.
    """

    def get(self):
        raise NotImplementedError
