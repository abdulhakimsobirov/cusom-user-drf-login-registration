from .responses import ResponseSuccess


class ListAPIViewResponseMixin:
    

    def list(self, request, *args, **kwargs):
        result = super().list(request, *args, **kwargs)
        return ResponseSuccess(result.data)


class RetrieveAPIViewResponseMixin:
    

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)
        return ResponseSuccess(result.data)


class CreateAPIViewResponseMixin:
    object_id = None

    def perform_create(self, serializer):
        result = super().perform_create(serializer)
        self.object_id = serializer.instance.id
        return result

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return ResponseSuccess({
            "id": self.object_id
        })


class UpdateAPIViewResponseMixin:
    ield = '-'

    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        return ResponseSuccess({})

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        return ResponseSuccess({})


class DestroyAPIViewResponseMixin:
    

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return ResponseSuccess()