from django.db import models
from django.conf import settings
from .utils import upload_image_to_imgbb
from django.utils import timezone
from django.utils.text import slugify
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    cateImage = models.ImageField(upload_to='cate_img/', blank=True, null=True, verbose_name='Category Image')
    imgbb_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)
        
        if self.cateImage and not self.imgbb_url:
            imgbb_url = upload_image_to_imgbb(self.cateImage.path, settings.IMGBB_API_KEY)
            if imgbb_url:
                self.imgbb_url = imgbb_url
                super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = HTMLField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

    def __str__(self):
        # return f"Product : {self.name}"
        return ''

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_img/', blank=True, null=True)
    imgbb_url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.image:  # Only proceed if an image is provided
            super().save(*args, **kwargs)  # Save the model instance first to generate the ID
            imgbb_url = upload_image_to_imgbb(self.image.path, settings.IMGBB_API_KEY)
            if imgbb_url:
                self.imgbb_url = imgbb_url
                super().save(*args, **kwargs)  # Save the model instance again to update imgbb_url
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Image : {self.product.name}"

class Banner(models.Model):
    banner = models.ImageField(upload_to='banner_img/', blank=True, null=True)
    imgbb_url = models.URLField(blank=True, null=True)
    def save(self, *args, **kwargs):
        if self.banner:  # Only proceed if an image is provided
            super().save(*args, **kwargs)  # Save the model instance first to generate the ID
            imgbb_url = upload_image_to_imgbb(self.banner.path, settings.IMGBB_API_KEY)
            if imgbb_url:
                self.imgbb_url = imgbb_url
                super().save(*args, **kwargs)  # Save the model instance again to update imgbb_url
        else:
            super().save(*args, **kwargs)

class Order(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Reseller")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)

    profit = models.PositiveIntegerField(default=0)
    sell_price = models.DecimalField(max_digits=10, decimal_places=0)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=0, default=120)
    adv = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Advance")
    cod = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Cash on Delivery")
    quantity = models.PositiveIntegerField(default=1)

    trxid = models.CharField(max_length=100, verbose_name="TrxID")
    bKash = models.CharField(max_length=20, default='0')
    amount = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    reference = models.CharField(max_length=255, default='0')

    invoice_no = models.CharField(max_length=100, unique=True)
    invoice_date = models.DateTimeField(default=timezone.now)

    PROFIT_STATUS_CHOICES = [
        ('PAID', 'Paid'),
        ('UNPAID', 'Unpaid'),
    ]
    
    profit_status = models.CharField(
        max_length=15,
        choices=PROFIT_STATUS_CHOICES,
        default='UNPAID',
    )
    
    ORDER_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
    ]
    
    order_status = models.CharField(
        max_length=15,
        choices=ORDER_STATUS_CHOICES,
        default='PENDING',
    )

    DELIVERY_STATUS_CHOICES = [
        ('PROCESSING', 'Processing'),
        ('DELIVERED', 'Deliverd'),
        ('RETURNED', 'Returned'),
    ]
    
    delivery_status = models.CharField(
        max_length=15,
        choices=DELIVERY_STATUS_CHOICES,
        default='PROCESSING',
    )

    def __str__(self):
        return self.invoice_no

