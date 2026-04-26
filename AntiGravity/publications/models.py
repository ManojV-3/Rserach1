from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.designation}"

class Publication(models.Model):
    PUB_TYPES = [
        ('Journal', 'Journal'),
        ('Conference', 'Conference'),
        ('Book Chapter', 'Book Chapter'),
        ('Book', 'Book'),
    ]
    
    MONTHS = [
        ('January', 'January'), ('February', 'February'), ('March', 'March'),
        ('April', 'April'), ('May', 'May'), ('June', 'June'),
        ('July', 'July'), ('August', 'August'), ('September', 'September'),
        ('October', 'October'), ('November', 'November'), ('December', 'December'),
    ]

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='publications')
    pub_type = models.CharField(max_length=50, choices=PUB_TYPES, verbose_name="Publication Type")
    title = models.CharField(max_length=500)
    venue_name = models.CharField(max_length=500, verbose_name="Journal/Conference/Book Name")
    issn_isbn = models.CharField(max_length=100, blank=True, null=True, verbose_name="ISSN / ISBN")
    month = models.CharField(max_length=20, choices=MONTHS, blank=True, null=True)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.year})"
