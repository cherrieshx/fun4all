from django.db import models

# Create your models here.

class Location(models.Model):
    nome = models.CharField(max_length=50)
    proprietario = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='locations')
    luogo = models.CharField(max_length=100)
    capienza = models.PositiveIntegerField()
    costo = models.PosotiveIntegerField()
    data_appertura = models.DateField()
    data_chiusura = models.DateField()
    
    Stato =[
        ('A', 'Attivo'),
        ('I', 'Inattivo'),
    ]

    stato = models.CharField(max_length=1, choices=Stato, default='A')

    def __str__(self):
        return self.nome


