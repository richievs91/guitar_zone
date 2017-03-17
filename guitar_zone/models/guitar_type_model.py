from django.db import models

class GuitarType(models.Model):
    """
    Stores a single product type, "label_name"
    author: Richie Van Sickle
    """
    label_name = models.CharField(max_length=55)

    def get_guitar_type_label(self):
        """
        Returns the label_name
        author: Richie Van Sickle
        """
        return self.label_name 

    def __str__(self):
        return '{}'.format(self.label_name)
