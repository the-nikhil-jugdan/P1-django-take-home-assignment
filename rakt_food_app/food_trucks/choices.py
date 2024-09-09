from django.db.models import TextChoices


class StatusChoices(TextChoices):
    Approved = ("APPROVED", "Approved")
    Requested = ("REQUESTED", "Requested")
    Pending = ("SUSPEND", "Pending")
    Expired = ("EXPIRED", "Expired")
    Issued = ("ISSUED", "Issued")
