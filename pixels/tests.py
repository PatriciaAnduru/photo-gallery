from django.test import TestCase
from .models import Pixel, Category

# Create your tests here.
class TestPixel(TestCase):
    def setUp(self):
        # self.location = Location(name='')
        # self.location.save_location()

        self.category = Category()
        self.category.save_category()

        self.image_test = Pixel(id=1)

    def test_instance(self):
        self.assertTrue(isinstance(Pixel))

    def test_save_image(self):
        self.image_test.save_pixel()
        after = Pixel.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.pixel_test.delete_pixel()
        pixels = Pixel.objects.all()
        self.assertTrue(len(pixels) == 0)

    def test_update_pixel(self):
        self.pixel_test.update_pixel()
        self.pixel_test.update_pixel(self.pixel_test.id, 'pixels/test.jpg')
        changed_img = Pixel.objects.filter(pixel='pixels/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def tearDown(self):
        Pixel.objects.all().delete()
        # Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category()
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)