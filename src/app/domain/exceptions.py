class DomainError(Exception):
    """Base class for business-rule errors."""


class EmailAlreadyRegisteredError(DomainError):
    pass
