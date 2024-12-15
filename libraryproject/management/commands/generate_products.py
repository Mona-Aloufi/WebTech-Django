import os
from django.core.management.base import BaseCommand
from faker import Faker
from libraryproject.models import Product  
from urllib.request import urlretrieve

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake products with images'

    def handle(self, *args, **kwargs):
        # Number of fake products to create
        num_products = 10

        # Example dummy image URL
        dummy_image_url = "https://dummyimage.com/300x300/000/fff"

        for _ in range(num_products):
            name = fake.word().capitalize()
            description = fake.text(max_nb_chars=200)
            
            # Download the image from dummyimage.com
            image_name = f"{name.lower()}_image.jpg"
            image_path = os.path.join('media/product_images/', image_name)
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            urlretrieve(dummy_image_url, image_path)
            
            # Save the product in the database
            Product.objects.create(
                name=name,
                description=description,
                image=f"product_images/{image_name}"
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {num_products} products!"))
