from django.test import TestCase

# Create your tests here.
def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)