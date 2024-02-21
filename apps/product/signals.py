from product.models import Product
from client.models import Purchase
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Product)
def recalculate_bill_total_after_update_price_product(sender, instance, *args, **kwargs):
    for purchase in Purchase.objects.filter(item=instance.pk):
        purchase.save()
