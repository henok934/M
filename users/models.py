# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta




"""
class CustomUser(AbstractUser):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )
    def __str__(self):
        return f"{self.username} - {self.email} - {self.fname} - {self.lname} - {self.gender} - {self.phone}"

class Fedback(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=50, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='fedback_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='fedback_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} {self.message}"


class Bus(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    sideno = models.CharField(max_length=50, null=True, blank=True)
    no_seats = models.CharField(max_length=50, null=True, blank=False)

    # Adding unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='bus_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='bus_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.plate_no} - {self.sideno} - {self.no_seats}"    

class City(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    # Adding unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='city_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='city_permissions_set',  # Unique related name
        blank=True
    )
    def __str__(self):
        return f"{self.depcity}"

class Route(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    kilometer = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='route_set',  # Unique related name
    blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='route_permissions_set',  # Unique related name
        blank=True
    )
    def __str__(self):
        return f"{self.depcity} - {self.descity}, {self.plate_no} - {self.side_no} - {self.kilometer} - {self.price} - {self.date}"

class Worker(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password
    side_no = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='worker_set',
        blank=True
    )
    worker_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='worker_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.fname} - {self.lname} - {self.gender} - {self.plate_no} - {self.side_no} - {self.phone}"
"""






import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.email} - {self.fname} - {self.lname} - {self.gender} - {self.phone} - {self.registration_id} - {self.registered_time}"




import uuid
from django.db import models
class Feedback(models.Model):
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)  # Increased length for messages

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='feedback_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='feedback_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone} - {self.message} - {self.registration_id} - {self.registered_time}"


import uuid
from django.db import models
class Bus(models.Model):
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    plate_no = models.CharField(max_length=50, null=True, blank=True)
    sideno = models.CharField(max_length=50, null=True, blank=True)
    no_seats = models.CharField(max_length=50, null=True, blank=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='bus_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='bus_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.plate_no} - {self.sideno} - {self.no_seats} - {self.registration_id} - {self.registered_time}"



import uuid
from django.db import models

class City(models.Model):
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    depcity = models.CharField(max_length=50, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='city_set',  # Unique related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='city_permissions_set',  # Unique related name
        blank=True
    )

    def __str__(self):
        return f"{self.depcity} - {self.registration_id} - {self.registered_time}"


import uuid
from django.db import models
class Route(models.Model):
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    kilometer = models.CharField(max_length=50, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=50, null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='route_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='route_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.depcity} - {self.descity}, {self.plate_no} - {self.side_no} - {self.kilometer} - {self.price} - {self.date} - {self.registration_id} - {self.registered_time}"


import uuid
from django.db import models
from django.utils import timezone

class Worker(models.Model):
    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registered_time = models.DateTimeField(auto_now_add=True)

    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password
    side_no = models.CharField(max_length=50, null=True, blank=True)
    plate_no = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='worker_set',
        blank=True
    )
    worker_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='worker_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.username} - {self.fname} - {self.lname} - {self.gender} - {self.plate_no} - {self.side_no} - {self.phone} - {self.registration_id} - {self.registered_time}"



class Admin(models.Model):
    #id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)

    registration_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # Registration time
    registered_time = models.DateTimeField(auto_now_add=True)


    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True
    )
    admin_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True
    )

    def formatted_registered_time(self):
        # Convert registered_time to the current timezone
        local_registered_time = self.registered_time.astimezone(timezone.get_current_timezone())
        return local_registered_time.strftime('%m,%d,%Y %I:%M %p')

    def save(self, *args, **kwargs):
        # Populate date and time components before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.fname} - {self.lname} - {self.gender} - {self.password} - {self.phone} - {self.registration_id} - {self.registered_time}"


import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta
import random
import os
import string
class Ticket(models.Model):
    # Unique ticket ID
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    pnr = models.CharField(max_length=6, unique=True, editable=False)

    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    no_seat = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)
    plate_no = models.CharField(max_length=20, null=True, blank=True)
    
    booked_time = models.DateTimeField(default=timezone.now)
    #booked_time = models.DateTimeField(default=timezone.now() + timedelta(minutes=5, seconds=30))
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ticket_set',
        blank=True
    )
    worker_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ticket_permissions_set',
        blank=True
    )

    from django.utils import timezone

    def formatted_booked_time(self):
        local_booked_time = self.booked_time.astimezone(timezone.get_current_timezone())
        return local_booked_time.strftime('%m,%d,%Y %I:%M %p')
   

    def __str__(self):
        barcode_image = self.generate_barcode()
        return f"{self.firstname} - {self.phone} - {self.lastname} - {self.pnr} - {self.price}, {self.descity} - {self.depcity} - {self.no_seat} - {self.plate_no} - {self.side_no} - {self.date}, {self.barcode_image}, {self.ticket_id}"



    def generate_barcode(self):
        """Generate a barcode image for the ticket ID."""
        barcode_format = 'code128'
        barcode_value = str(self.ticket_id)
        barcode_image = barcode.encode(barcode_format, barcode_value, writer=ImageWriter())

        barcode_path = f'static/barcodes/{barcode_value}.png'
        if not os.path.exists('static/barcodes'):
            os.makedirs('static/barcodes')
    
            barcode_image.save(barcode_path)
            return barcode_path

    def save(self, *args, **kwargs):
        # Generate a unique PNR if not already set
        if not self.pnr:
            self.pnr = self.generate_pnr()
        super().save(*args, **kwargs)

    def generate_pnr(self):
        """Generate a random PNR consisting of 6 lowercase characters."""
        return ''.join(random.choices(string.ascii_uppercase, k=6))









"""
class Ticket(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    no_seat = models.CharField(max_length=20, null=True, blank=True)
    price = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)
    plate_no = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ticket_set',  # Unique related name
        blank=True
    )
    worker_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ticket_permissions_set',  # Unique related name
        blank=True
    )
    def __str__(self):
        return f"{self.firstname} - {self.phone}, {self.lastname} - {self.price}, {self.descity} - {self.depcity} {self.no_seat} - {self.plate_no} - {self.side_no} - {self.date}"
"""



"""
class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True
    )
    admin_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True
    )
    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username} - {self.password}"
"""



"""
from django.db import models

class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password

    groups = models.ManyToManyField('auth.Group', related_name='admin_set', blank=True)
    admin_permissions = models.ManyToManyField('auth.Permission', related_name='admin_permissions_set', blank=True)

    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username}"
"""






"""
from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    # Remove username and password as they are inherited from AbstractUser
    # username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    # password = models.CharField(max_length=128)  # Not needed

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='admin_set',
        blank=True
    )
    admin_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='admin_permissions_set',
        blank=True
    )

    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username}"
"""




"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(models.Model):
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)  # Store hashed password

    groups = models.ManyToManyField('auth.Group', related_name='admin_set', blank=True)
    admin_permissions = models.ManyToManyField('auth.Permission', related_name='admin_permissions_set', blank=True)

    def __str__(self):
        return f"{self.fname} - {self.phone} - {self.lname} - {self.gender} - {self.email} - {self.username} - {self.password}"
"""

class Buschange(models.Model):
    new_side_no = models.CharField(max_length=50, null=True, blank=True)
    new_plate_no = models.CharField(max_length=50, null=True, blank=True)
    depcity = models.CharField(max_length=50, null=True, blank=True)
    descity = models.CharField(max_length=50, null=True, blank=True)
    date = models.CharField(max_length=50, null=True, blank=True)
    side_no = models.CharField(max_length=20, null=True, blank=True)
    plate_no = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='buschange_set',
        blank=True
    )
    buschange_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='buschange_permissions_set',
        blank=True
    )
    def __str__(self):
        return f"{self.depcity} - {self.descity}, {self.new_side_no} - {self.new_plate_no}, - {self.plate_no} - {self.side_no} - {self.date}"

