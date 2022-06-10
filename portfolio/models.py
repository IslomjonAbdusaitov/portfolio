from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, help_text="Proyekt nomi")
    description = models.TextField(help_text="Proyekt tavsifi")
    link = models.URLField(help_text="Githubdagi linki", null=True, default=None)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    sender_name = models.CharField(max_length=200, help_text="Xabar yuboruvchining ismi")
    sender_email = models.EmailField(max_length=200, help_text="Xabar yuboruvchining email manzili")
    subject = models.CharField(max_length=200, help_text="Xabar mavzusi")
    text = models.TextField(help_text="Xabar matni")

    def __str__(self) -> str:
        return f"{self.sender_name} -> {self.sender_email} {self.subject}"