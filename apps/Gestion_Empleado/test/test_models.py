from django.test import TestCase
from apps.Gestion_Empleado.models import Cargo


class CargoTest(TestCase):

    def setUp(self):
        Cargo.objects.create( Nombre='Cargo Prueba', Estado=1, Valor_cargo=2300000)
    def test_Cargo(self):
        cargo1 = Cargo.objects.get(Nombre='Cargo Prueba')
        self.assertAlmostEqual(cargo1.Valor_cargo,2300000)
