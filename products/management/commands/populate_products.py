from django.core.management.base import BaseCommand
from products.models import Product, Category
from django.utils.text import slugify
import os


def create_category(category_name):
    # Creates a category object, handling potential duplicates.
    # Assigns a default category if the name is not found.
    category, created = Category.objects.get_or_create(name=category_name)
    if not created:
        print(f"Category '{category_name}' already exists. Skipping.")
    return category
    


categories = [
    {'name': 'Fresh Produce'},
    {'name': 'Meat, Poultry, and Seafood'},
    {'name': 'Dairy and Eggs'},
    {'name': 'Pantry'},
    {'name': 'Baked Goods'},
    {'name': 'International and Specialty'},
    {'name': 'Beverages'},
    {'name': 'Non Food Supplies'},
    {'name': 'Health and Wellness'},
    {'name': 'Pet Food'},
    {'name': 'Condiments and Sauces'},
    {'name': 'Oils and Vinegars'},
    {'name': 'Spices and Herbs'},
    {'name': 'Breakfast Foods'},
    {'name': 'Frozen Foods'},
    {'name': 'Snack Foods'},
    {'name': 'Baby and Childcare'},
    {'name': 'Household Essentials'},
    
    # ... add more categories as needed
]

products = [
    {
        'name': 'Assorted-Spices',
        'description': 'Elevate your culinary creations with this exquisite selection of premium assorted spices sourced from the heart of Nigeria, meticulously chosen to enhance the flavors and aromas of your favorite dishes.',
        'price': 1000,
        'image': 'Assorted-Spices.webp',
        'category': categories[12]
    },
    {
        'name': 'Cow-Head',
        'description': 'Immerse yourself in the rich traditions of Nigerian cuisine with our fresh and tender cow head meat, perfect for crafting traditional delicacies that celebrate authentic flavors and cultural heritage.',
        'price': 4000,
        'image': 'Cow-Head.webp',
        'category': categories[1]
    },
   {
        'name': 'Egusi',
        'description': 'Experience the true essence of Nigerian cooking with our top-grade Egusi seeds, designed to bring depth and richness to iconic dishes like Egusi soup, beloved across generations.',
        'price': 1600,
        'image': 'Egusi.webp',
        'category': categories[3]
    },
    {
        'name': 'Goat-Head',
        'description': 'Discover the true taste of Nigeria with our premium goat head meat, handpicked for its succulent texture and bold flavors that capture the essence of local gastronomy.',
        'price': 5000,
        'image': 'Goat-Head.webp',
        'category': categories[1]
    },
    {
        'name': 'Honey-Beans',
        'description': 'Elevate your meals with the wholesome goodness of our handpicked honey beans, prized for their nutritional value and culinary flexibility in creating authentic Nigerian dishes.',
        'price': 2400,
        'image': 'Honey-Beans.webp',
        'category': categories[3]
    },
    {
        'name': 'Maize-Flour',
        'description': 'Transform your kitchen with our premium maize flour, a staple ingredient in Nigerian cooking that promises authenticity and convenience in preparing classic dishes such as Akara and Ogi.',
        'price': 2000,
        'image': 'Maize-Flour.webp',
        'category': categories[3]
    },
    {
        'name': 'Mangala-Fish',
        'description': 'Dive into a world of flavor with our fresh Mangala fish, sourced locally to deliver the authentic taste of Nigerian seafood, perfect for enriching your culinary creations.',
        'price': 3600,
        'image': 'Mangala-Fish.webp',
        'category': categories[1]
    },
    {
        'name': 'Natural-Refined-Honey',
        'description': 'Experience the purity and sweetness of our natural refined honey, a premium ingredient imbued with natural goodness to enhance the flavors of your favorite Nigerian recipes and beverages.',
        'price': 3000,
        'image': 'Natural-Refined-Honey.webp',
        'category': categories[8]
    },
    {
        'name': 'Ogbono',
        'description': 'Unveil the rich and nutty undertones of Nigerian cuisine with our superior Ogbono seeds, meticulously selected to create the iconic Ogbono soup, a cherished dish in Nigerian homes.',
        'price': 2500,
        'image': 'Ogbono.webp',
        'category': categories[3]
    },
    {
        'name': 'Palm-Oil',
        'description': 'Add depth and color to your dishes with our top-quality Nigerian palm oil, a versatile culinary essential crafted to infuse traditional dishes with authenticity and flavor.',
        'price': 2200,
        'image': 'Palm-Oil.webp',
        'category': categories[11]
    },
    {
        'name': 'Red-Garri',
        'description': 'Experience the vibrancy of Nigerian cuisine with our premium red garri, a beloved staple that captures the essence of local culture and tradition, perfect for creating classic Garri soakings.',
        'price': 1800,
        'image': 'Red-Garri.webp',
        'category': categories[3]
    },
    {
        'name': 'Roasted-Catfish',
        'description': 'Indulge in the smoky goodness of our expertly roasted catfish, a flavorful delicacy in Nigerian cuisine that promises a burst of authentic flavors in every bite.',
        'price': 4000,
        'image': 'Roasted-Catfish.webp',
        'category': categories[1]
    },
    {
        'name': 'Roasted-Titus-Fish',
        'description': 'Savor the tender and aromatic flavors of our roasted Titus fish, expertly prepared to bring out the distinctive taste of Nigerian seafood, perfect for elevating your culinary creations.',
        'price': 3800,
        'image': 'Roasted-Titus-Fish.webp',
        'category': categories[1]
    },
    {
        'name': 'Stock-Fish',
        'description': 'Elevate your cooking with our premium stock fish, a key ingredient in traditional Nigerian dishes that promises rich and robust flavors, essential for creating iconic recipes like Banga stew and Edikang Ikong soup.',
        'price': 2800,
        'image': 'Stock-Fish.webp',
        'category': categories[1]
    },
    {
        'name': 'Tomatoes-Paste',
        'description': 'Enhance the depth of your dishes with our premium tomatoes paste, expertly crafted to unlock the richness of Nigerian flavors in stews, soups, and sauces for a gourmet culinary experience.',
        'price': 2000,
        'image': 'Tomatoes-Paste.webp',
        'category': categories[3]
    },
    {
        'name': 'Ugwu',
        'description': 'Discover the nutritional benefits and exquisite taste of Nigerian ugwu leaves, a versatile ingredient beloved in Nigerian cuisine for preparing dishes such as egusi soup and vegetable sauce with an authentic touch.',
        'price': 1500,
        'image': 'Ugwu.webp',
        'category': categories[0]
    },
    {
        'name': 'White-Garri',
        'description': 'Embrace the versatility and nutritional value of our White Garri, a quintessential ingredient in Nigerian cuisine, ideal for preparing staples like Eba and Garri soakings with a touch of authenticity and flavor.',
        'price': 1200,
        'image': 'White-Garri.webp',
        'category': categories[3]
    },
    {
        'name': 'Yellow-Garri',
        'description': 'Experience the rich flavor and aroma of our Yellow Garri, a Nigerian staple made from fermented cassava, perfect for creating traditional dishes like Eba and Garri soakings.',
        'price': 1000,
        'image': 'Yellow-Garri.webp',
        'category': categories[3]
    },

    
    # ... (rest of the products)
]

IMAGE_DIR = 'C:\\Users\\Ikoni\\Desktop\\djan1_30\\djan003\\mymart2\\media\\products\\items1.1'

# To access an image path, use os.path.join(IMAGE_DIR, product['image'])
class Command(BaseCommand):
    help = 'Upload products to existing categories'

    def handle(self, *args, **options):
        # Create categories
        for category_data in categories:
            Category.objects.get_or_create(name=category_data['name'], defaults={'slug': slugify(category_data['name'])})

    
        # Create products
        for product_data in products:
            try:
                category_name = product_data['category']['name']
                category = Category.objects.get(name=category_name)
                image_path = os.path.join(IMAGE_DIR, product_data['image'])
                slug = slugify(product_data['name'])
                if Product.objects.filter(slug=slug).exists():
                    slug += '-' + ''.join(random.choices(string.ascii_lowercase, k=6))
                Product.objects.create(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    image=image_path,
                    category=category,
                    slug=slug
                )
                print(f"Successfully created product: {product_data['name']}")
            except Category.DoesNotExist:
                print(f"Error creating product: {product_data['name']}, Category '{category_name}' does not exist.")
            except Exception as e:
                print(f"Error creating product: {product_data['name']}, Error: {e}")

                
        """
        for product_data in products:
            try:
                category = Category.objects.get(name=product_data['category_name'])
                image_path = os.path.join(IMAGE_DIR, product_data['image'])
                Product.objects.create(
                    name=product_data['name'],
                    description=product_data['description'],
                    price=product_data['price'],
                    image=image_path,
                    category=category
                )
                print(f"Successfully created product: {product_data['name']}")
            except Category.DoesNotExist:
                print(f"Category '{product_data['category_name']}' not found for product {product_data['name']}")
            except Exception as e:
                print(f"Error creating product: {product_data['name']}, Error: {e}")


"""




