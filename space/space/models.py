from django.db import models

class Space_Credentials(models.Model):
    token = models.TextField()
    def __str__(self):
        template = '{0.token}'
        return template.format(self)

class space_api_to_get(models.Model):
    space_api = models.TextField()

    def __str__(self):
        template = '{0.space_api}'
        return template.format(self)

class space_api_output(models.Model):
    space_api_output = models.TextField()

    def __str__(self):
        template = '{0.space_api_output}'
        return template.format(self)