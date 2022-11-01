from rest_framework.response import Response


class ResponseFail(Response):
    def __init__(self, data="", status=200):
        data = {"status": "fail", "data": data}
        self.__init__ = super().__init__(data, status=status)


class ResponseSuccess(Response):
    def __init__(self, data="", code=200, headers=None):
        if isinstance(data, Response):
            data = data.data

        data = { "data": data}
        if headers:
            super().__init__(data, status=code, headers=headers)
        else:
            super().__init__(data, status=code)