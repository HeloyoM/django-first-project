from django.db import models


class TestDocument(models.Model):
    _id = models.CharField(max_length=24, primary_key=True)
    user_id = models.IntegerField()
    id = models.IntegerField()
    title = models.TextField()
    body = models.TextField()

document = TestDocument(
    _id="6336039dbc8b5ff6aceecb11",
    user_id=45,
    id=12,
    title="first django project",
    body="nice",
)

print(document)
'''document.save()'''
