from django.dispatch import receiver
from pretix.base.signals import validate_order
from pretix.base.services.orders import OrderError

@receiver(validate_order, dispatch_uid="email_checker_validate_order")
def validate_order_email(sender, **kwargs):
    """
    Validate the order email address
    """
    if 'email' in kwargs:
        email = kwargs['email']
        allowed_domain = "hs-coburg.de"  # Replace with your desired domain
        
        if not email.endswith(allowed_domain):
            raise OrderError(f"Email must end with \"{allowed_domain}\" Please use your hs-coburg.de email address.")
    
    return None
