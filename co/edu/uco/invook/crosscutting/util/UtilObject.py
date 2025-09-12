class UtilObject:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UtilObject, cls).__new__(cls)
        return cls._instance

    def is_null(self, obj) -> bool:
        return obj is None

    def get_default(self, obj, default_obj):
        return default_obj if self.is_null(obj) else obj
