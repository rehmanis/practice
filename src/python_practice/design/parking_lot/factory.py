class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key: str, builder):

        if key in self._builders:
            raise ValueError(key)

        self._builders[key] = builder

    def create(self, key: str, **kwargs):
        builder = self._builders.get(key)

        if not builder:
            raise ValueError(key)

        return builder(**kwargs)

    def batch_create(self, key: str, freq: int, **kwargs):
        return [self.create(key, **kwargs) for _ in range(freq)]
