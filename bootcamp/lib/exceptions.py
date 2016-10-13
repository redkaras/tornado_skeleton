from __future__ import absolute_import


class BaseServiceError(Exception):
    code = 400


class EntityAlreadyExistsError(BaseServiceError):
    code = 419


class ResourceNotFoundError(BaseServiceError):
    code = 404
