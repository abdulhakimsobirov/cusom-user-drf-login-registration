from rest_framework.response import Response


class ResponseFail(Response):
    def __init__(self, data="", status=200):
        data = {"status": "fail", "data": data}
        self.__init__ = super().__init__(data, status=status)


# class ResponseSuccess(Response):
#     def __init__(self, data="", code=200, headers=None):
#         if isinstance(data, Response):
#             data = data.data

#         data = {"status": "success", "data": data}
#         if headers:
#             super().__init__(data, status=code, headers=headers)
#         else:
#             super().__init__(data, status=code)

class ResponseSuccess(Response):
    def __init__(self, data="", code=200, filter_fields=None):
        if isinstance(data, Response):
            data = data.data

        data = {"code":code,  "status": "success", "result": data}
        if filter_fields:
            data["filter_fields"] = filter_fields
        super().__init__(data, status=code)