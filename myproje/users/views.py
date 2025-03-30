from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import CustomUser
from .models import Feedback
from .models import Bus
from .models import Route
from django.db import IntegrityError
from .models import City
from .models import Worker
from .models import Buschange
from .models import Admin
from .models import Ticket
from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import render
from .models import Buschange, City  # Ensure you import your models

def custom_csrf_failure_view(request, reason=""):
    return render(request, 'users/csrf_failure.html', {'reason': reason})


def home(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()
    
    des = City.objects.all()
    
    # Prepare context
    context = {
        'des': des,
    }
    
    # Only add buschanges_count if it's greater than 0
    if buschanges_count > 0:
        context['buschanges_count'] = buschanges_count    
    return render(request, 'users/index.html', context)


def profile(request):
    user_id = request.session.get('user_id')  # Retrieve the user ID from the session
    user = None
    if user_id:
        user = CustomUser.objects.get(id=user_id)
    return render(request, 'users/profile.html', {'user': user})
def about(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()
    context = {}
    # Only add buschanges_count if it's greater than 0
    if buschanges_count > 0:
        context['buschanges_count'] = buschanges_count

    return render(request, 'users/about.html', context)
def driver(request):
    driver = Worker.objects.all()
    return render(request, 'users/drivers.html', {'driver': driver})


"""
import uuid
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import CustomUser, Worker  # Adjust import based on your project structure

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')  # Get the selected user type

        try:
            # Adjust the query based on user type
            if user_type == 'user':
                user = CustomUser.objects.get(email=email, is_staff=False)  # Regular users
            elif user_type == 'driver':
                user = Worker.objects.get(email=email, is_staff=True)  # Assuming drivers are staff
            else:
                return render(request, 'users/forgot_password.html', {'error': 'Invalid user type.'})

            # Generate a reset token
            token = str(uuid.uuid4())
            user.profile.reset_token = token  # Assuming you have a profile model to store this
            user.profile.save()

            # Send email
            reset_link = f'http://yourdomain.com/reset-password/{token}/'
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                'from@example.com',
                [email],
                fail_silently=False,
            )

            # Redirect to a page informing the user that the email has been sent
            return render(request, 'users/forgot_password.html', {'message': 'Password reset link sent! Check your email.'})
        except (CustomUser.DoesNotExist, Worker.DoesNotExist):
            return render(request, 'users/forgot_password.html', {'error': 'Email not found for the selected user type.'})
    return render(request, 'users/forgot_password.html')

import uuid
from django.core.mail import send_mail
from django.shortcuts import render

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')  # Get the selected user type

        try:
            if user_type == 'user':
                user = CustomUser.objects.get(email=email, is_staff=False)
            elif user_type == 'driver':
                user = Worker.objects.get(email=email, is_staff=True)
            else:
                return render(request, 'users/forgot_password.html', {'error': 'Invalid user type.'})

            # Generate a reset token and save it in CustomUser
            token = str(uuid.uuid4())
            user.reset_token = token
            user.save()

            reset_link = f'http://yourdomain.com/reset-password/{token}/'
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                'from@example.com',
                [email],
                fail_silently=False,
            )

            return render(request, 'users/forgot_password.html', {'message': 'Password reset link sent! Check your email.'})
        except (CustomUser.DoesNotExist, Worker.DoesNotExist):
            return render(request, 'users/forgot_password.html', {'error': 'Email not found for the selected user type.'})
    return render(request, 'users/forgot_password.html')





from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

def reset_password(request, token):
    User = get_user_model()

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate the passwords match
        if new_password == confirm_password:
            try:
                user = User.objects.get(reset_token=token)
                user.set_password(new_password)  # Set the new password
                user.reset_token = ''  # Clear the reset token
                user.save()  # Save the user instance
                messages.success(request, 'Your password has been reset successfully. You can now log in.')
                return redirect('login')  # Redirect to the login page
            except User.DoesNotExist:
                messages.error(request, 'Invalid reset token.')
                return redirect('forgot_password')  # Redirect to the forgot password page
    return render(request, 'users/reset_password.html', {'token': token})



def reset_password(request, token):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate the password and confirm_password match
        if new_password == confirm_password:
            try:
                user_profile = Profile.objects.get(reset_token=token)  # Adjust based on how you store the token
                user = user_profile.user
                user.set_password(new_password)
                user_profile.reset_token = ''  # Clear the token
                user_profile.save()
                user.save()
                return redirect('login')  # Redirect to login after successful reset
            except Profile.DoesNotExist:
                return render(request, 'users/reset_password.html', {'error': 'Invalid token.'})

    return render(request, 'users/reset_password.html', {'token': token})
"""







"""
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import User
import uuid


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')  # Get the selected user type
        try:
            # Adjust the query based on user type
            if user_type == 'user':
                user = CustomUser.objects.get(email=email, is_staff=False)  # Regular users
            elif user_type == 'driver':
                user = Worker.objects.get(email=email, is_staff=True)  # Assuming drivers are staff

            token = str(uuid.uuid4())
            user.profile.reset_token = token  # Assuming you have a profile model to store this
            user.profile.save()

            # Send email (you'll need to configure your email settings)
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: yourdomain.com/reset-password/{token}/',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return render(request, 'users/forgot_password.html', {'message': 'Password reset link sent!'})
        except User.DoesNotExist:
            return render(request, 'users/forgot_password.html', {'error': 'Email not found for the selected user type.'})

    return render(request, 'users/forgot_password.html')
"""









from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from .models import Buschange, Worker, Route

def login(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        #user = authenticate(request, username=username, password=password)

        #if user is not None:
        #   auth_login(request, user)  # Log the user in
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in

            # Store user information in the session
            request.session['user_id'] = user.id
            request.session['username'] = user.username  # Add other user information as needed

            if role == 'user':
                return redirect('profile')
                #return render(request, 'users/profile.html', {'user': user})  # Redirect to the admin page

            elif role == 'worker':
                try:
                    worker = Worker.objects.get(username=username)
                    routes = Route.objects.filter(side_no=worker.side_no)
                    return render(request, 'users/rooteee.html', {'routes': routes})
                except Worker.DoesNotExist:
            
                    return render(request, 'users/login.html', {'error': 'This username Worker not found', 'buschanges_count': buschanges_count})

        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password', 'buschanges_count': buschanges_count})
    return render(request, 'users/login.html', {'buschanges_count': buschanges_count})



def root(request):
    return render(request, 'users/checkroot.html')
def logout(request):
    return render(request, 'users/login.html')
def users(request):
    users = CustomUser.objects.all()
    return render(request, 'users/users.html',{'users': users})
def comments(request):
    comments = Feedback.objects.all()
    return render(request, 'users/comments.html',{'comments': comments})
def routes(request):
    routes = Route.objects.all()
    return render(request, 'users/routes.html',{'routes': routes})
def selectbus(request):
    return render(request, 'users/route.html')

from django.shortcuts import render
from .models import Ticket  # Ensure you have the Ticket model imported
#from .forms import TicketForm  # Ensure you have a TicketForm if you're using it
from .models import City, Bus  # Assuming you have City and Bus models

def ticket(request):
    des = City.objects.all()  # Assuming you have a City model
    bus = Bus.objects.all()    # Assuming you have a Bus model

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        depcity = request.POST['depcity']
        descity = request.POST['descity']
        date = request.POST['date']
        no_seat = request.POST['no_seat']
        price = request.POST['price']
        side_no = request.POST['side_no']
        plate_no = request.POST['plate_no']

        if no_seat == "FULL":
            return render(request, 'users/ticket.html', {
                'bus': bus,
                'des': des,
                'error': 'Cannot book ticket: the bus is already full.'
            })

        existing_ticket = Ticket.objects.filter(
            firstname=firstname,
            lastname=lastname,
            depcity=depcity,
            descity=descity,
            date=date,
            plate_no=plate_no,
            side_no=side_no
        ).exists()

        if existing_ticket:
            return render(request, 'users/ticket.html', {
                'bus': bus,
                'des': des,
                'error': 'This person has already booked a ticket for this route.'
            })

        # Create the Ticket instance
        ticket_instance = Ticket(
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            depcity=depcity,
            descity=descity,
            date=date,
            no_seat=no_seat,
            price=price,
            side_no=side_no,
            plate_no=plate_no
        )
        ticket_instance.save()  # Save the ticket to generate the ticket ID

        # Generate QR code and save it
        ticket_instance.qr_code = ticket_instance.generate_qr_code()
        ticket_instance.save(update_fields=['qr_code'])  # Save the QR code back to the database

        return render(request, 'users/ticket.html', {
            'bus': bus,
            'des': des,
            'success': 'Ticket booked successfully!',
            'qr_code': ticket_instance.qr_code,
            'ticket': ticket_instance  # Pass the ticket instance for further details
        })

    return render(request, 'users/ticket.html', {'bus': bus, 'des': des})

def businsert(request):
    if request.method == 'POST':
        plate_no = request.POST['plate_no']
        sideno = request.POST['sideno']
        no_seats = request.POST['no_seats']

        if Bus.objects.filter(plate_no=plate_no).exists():
            return render(request, 'users/Businsert.html', {'error': 'plate_no already exists.'})

        if Bus.objects.filter(sideno=sideno).exists():
            return render(request, 'users/Businsert.html', {'error': 'Side_no already exists.'})
        bus = Bus.objects.create(
            plate_no=plate_no,
            sideno=sideno,
            no_seats=no_seats
        )
        bus.save()
        return render(request, 'users/Businsert.html', {'success': 'Bus registored'})
    return render(request, 'users/Businsert.html')

def comment(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        comment = Feedback(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        try:
            comment.save()
        except IntegrityError:
            return render(request, 'comment.html', {'error': 'An error occurred while saving.', 'buschanges_count':  buschanges_count})
        return render(request, 'users/comment.html',{'success': 'Comment submited Successfully.','buschanges_count':  buschanges_count})
    return render(request, 'users/comment.html',{'buschanges_count':  buschanges_count})

def get_ticket(request):
    des = City.objects.all()
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()

    if request.method == 'POST':
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        ticket = Ticket.objects.filter(
            depcity=depcity,
            descity=descity,
            date=date,
            firstname=firstname,
            lastname=lastname
        )
        if ticket.exists():
            qr_code_path = ticket.first().generate_qr_code()
            return render(request, 'users/tickets.html', {'ticket': ticket, 'qr_code_path': qr_code_path, 'success': "Your Ticket is:"})
        elif depcity == descity:
            return render(request, 'users/error1.html', {'error': "Try Again. Entered Departure and Destination is the Same!"})
        elif firstname == lastname:
            return render(request, 'users/error1.html', {'error': "Try Again. Entered Firstname AND Lastname The Same!"})
        else:
            return render(request, 'users/error1.html', {'error': "Try Again. There is no Ticket Booked info for the entered details!"})
    return render(request, 'users/getticket.html', {'des': des,'buschanges_count':buschanges_count})


def worker_view(request):
    des = City.objects.all()
    bus = Bus.objects.all()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')
        if Worker.objects.filter(username=username).exists():
            return render(request, 'users/worker.html', {'bus': bus, 'des': des, 'error': 'Username already exists.'})
        if Worker.objects.filter(plate_no=plate_no).exists():
            return render(request, 'users/worker.html', {'bus': bus, 'des': des, 'error': 'This bus already has a Driver.'})
        if Worker.objects.filter(phone=phone).exists():
            return render(request, 'users/worker.html', {'bus': bus, 'des': des, 'error': 'Phone already exists.'})
        worker = Worker.objects.create(
            username=username,
            plate_no=plate_no,
            side_no=side_no,
            password=password,
            phone=phone,
            fname=fname,
            lname=lname,
            gender=gender
        )
        return render(request, 'users/worker.html', {'bus': bus, 'des': des, 'success': 'Driver registered successfully.'})
    return render(request, 'users/worker.html', {'bus': bus, 'des': des})


from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from .models import City, Bus, Route
def route(request):
    des = City.objects.all()
    dep = City.objects.all()
    bus = Bus.objects.all()

    if request.method == 'POST':
        descity = request.POST.get('descity')
        depcity = request.POST.get('depcity')
        print(depcity)
        print(descity)
        date = request.POST.get('date')
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')
        price = request.POST.get('price')
        kilometer = request.POST.get('kilometer')
        if depcity.strip() == descity.strip():
            return render(request, 'users/route.html', {'bus': bus, 'des': des, 'dep': dep, 'error': 'Departure and Destination cannot be the same!'})
        if Route.objects.filter(depcity=depcity, descity=descity, plate_no=plate_no, side_no=side_no, date=date).exists():
            return render(request, 'users/route.html', {'bus': bus, 'des': des, 'dep': dep, 'error': 'route already exists.'})
        if Route.objects.filter(side_no=side_no, date=date, plate_no=plate_no).exists():
            return render(request, 'users/route.html', {'bus': bus, 'des': des, 'dep': dep, 'error': 'This bus is already reserved for another route for this date'})

        route = Route.objects.create(
            depcity=depcity,
            descity=descity,
            kilometer=kilometer,
            plate_no=plate_no,
            side_no=side_no,
            price=price,
            date=date
        )
        print(depcity)
        if depcity.strip() == "Addisababa":
            date = timezone.datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)
            date = date.strftime('%Y-%m-%d')
            depcity, descity = descity, depcity
            Route.objects.create(
                depcity=depcity,
                descity=descity,
                kilometer=kilometer,
                plate_no=plate_no,
                side_no=side_no,
                price=price,
                date=date
            )
        return render(request, 'users/route.html', {'bus': bus, 'des': des, 'dep': dep, 'success': 'Route registered successfully!'})
    return render(request, 'users/route.html', {'bus': bus, 'des': des, 'dep': dep})

def city_view(request):
    if request.method == 'POST':
        depcity = request.POST['depcity']
        if City.objects.filter(depcity=depcity).exists():
            return render(request, 'users/city.html', {'error': 'This city already exists.'})
        city = City.objects.create(
            depcity=depcity,
        )
        city.save()
        return render(request, 'users/city.html', {'success': 'City registored Successfully!'})
    return render(request, 'users/city.html')


from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Admin, City, Bus
def admins(request):
    des = City.objects.all()  # Fetch all cities
    bus = Bus.objects.all()    # Fetch all buses
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        if Admin.objects.filter(username=username).exists():
            return render(request, 'users/admin.html', {'bus': bus, 'des': des, 'error': 'Username Already Exists.'})
        if Admin.objects.filter(email=email).exists():
            return render(request, 'users/admin.html', {'bus': bus, 'des': des, 'error': 'This Admin already Exists.'})
        if Admin.objects.filter(phone=phone).exists():
            return render(request, 'users/admin.html', {'bus': bus, 'des': des, 'error': 'Phone already Exists.'})

        # Create the admin with a hashed password
        admin = Admin.objects.create(
            username=username,
            fname=fname,
            lname=lname,
            password=password,  # Hash the password
            phone=phone,
            email=email,
            gender=gender
        )
        return render(request, 'users/admin.html', {'bus': bus, 'des': des, 'success': 'Admin Created Successfully.'})
    return render(request, 'users/admin.html', {'bus': bus, 'des': des})  # Render on GET request


def ad(request):
    return render(request, 'users/ad.html')
def get_user(request):
    return render(request, 'users/checkuser.html')

def get_route(request):
    des = City.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)         
        if routes.exists():
            return render(request, 'users/checkroot.html', {'routes': routes, 'success': "Routes info---"})
        else:
            return render(request, 'users/index.html', {'des': des, 'error': "Try Again! There is no route information!"})
    return render(request, 'users/index.html', {'des': des}) 

def ticketinfo(request):
    des = City.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        if routes.exists():
            return render(request, 'users/rootee.html', {'routes': routes, 'success': "Routes info---"})
        if depcity == descity:
            des = City.objects.all()
            return render(request, 'users/cheeckrouteee.html', {'error': 'You Entered Departure and Destination is The same!', 'des':des})
        else:
            des = City.objects.all()
            return render(request, 'users/cheeckrouteee.html', {'error': 'There is no route for this route', 'des':des})
    return render(request, 'users/cheeckrouteee.html', {'des':des})


def delete_ticket(request):
    des = City.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        if routes.exists():
            return render(request, 'users/rooteeee.html', {'routes': routes, 'success': "Routes info---"})
        if depcity == descity:
            des = City.objects.all()
            return render(request, 'users/cheeckrouteeee.html', {'error': 'You Entered Departure and Destination is The same!', 'des':des})
        else:
            des = City.objects.all()
            return render(request, 'users/cheeckrouteeee.html', {'error': 'There is no route for this route', 'des':des})
    return render(request, 'users/cheeckrouteeee.html', {'des':des})

def delete_tickets(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')  # Uncomment if needed
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        deleted_count, _ = Ticket.objects.filter(
            plate_no=plate_no,
            date=date,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            depcity=depcity,
            descity=descity
        ).delete()
        route = Ticket.objects.filter(depcity=depcity, descity=descity, plate_no=plate_no, date=date)
        if deleted_count > 0:
            return render(request, 'users/deleteticket.html', {'success': 'Ticket Deleted successfully.', 'route': route})
        else:
            return render(request, 'users/deleteticket.html', {'error': 'No ticket found to delete.', 'route': route})
    route = Ticket.objects.all()
    return render(request, 'users/deleteticket.html', {'route': route})


def delete_ticketss(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        route = Ticket.objects.filter(plate_no=plate_no,date=date,depcity=depcity,descity=descity)
        routes = Route.objects.filter(date=date, depcity=depcity, descity=descity)
        if route.exists():
            return render(request, 'users/deleteticket.html', {'route': route})
        else:
            return render(request, 'users/rooteeee.html',{'error': 'No booked tickets for this travel', 'routes': routes})
    return render(request, 'users/rooteeee.html', {'routes': routes})


def Selectbus(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        route = Ticket.objects.filter(plate_no=plate_no, date=date,depcity=depcity,descity=descity)

        routes = Route.objects.filter(date=date, depcity=depcity, descity=descity)
        if route.exists():
            return render(request, 'users/ticketoch.html', {'route': route})
        else:
            return render(request, 'users/rootee.html',{'error': 'No booked tickets for this travel', 'routes': routes})

    return render(request, 'users/rootee.html')


from django.shortcuts import render
from .models import City, Route, Bus, Ticket  # Adjust based on your actual model imports
def book(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()

    des = City.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        rout = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        routes = []

        if rout.exists():
            for route in rout:
                try:
                    bus = Bus.objects.get(plate_no=route.plate_no)
                    total_seats = int(bus.no_seats)  # Ensure total_seats is an integer
                except Bus.DoesNotExist:
                    total_seats = 0

                booked_tickets = Ticket.objects.filter(
                    depcity=route.depcity,
                    descity=route.descity,
                    date=route.date,
                    plate_no=route.plate_no
                ).count()
                remaining_seats = max(0, total_seats - booked_tickets)
                if remaining_seats == 0:
                    remaining_seats = "Full"
                routes.append({
                    'route': route,
                    'remaining_seats': remaining_seats
                }) 
            return render(request, 'users/roote.html', {'routes': routes, 'buschanges_count': buschanges_count})
        else:
            return render(request, 'users/cheeckroutee.html', {'des': des,'buschanges_count': buschanges_count, 'error': "There is no Travel for this  information!"})
    return render(request, 'users/cheeckroutee.html', {'des': des, 'buschanges_count': buschanges_count})




def Select(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date,plate_no=plate_no)
        route_info = []
        bus_full = False
        for route in routes:
            try:
                bus = Bus.objects.get(plate_no=route.plate_no)
                total_seats = int(bus.no_seats)

                booked_tickets = Ticket.objects.filter(
                    depcity=route.depcity,
                    descity=route.descity,
                    date=route.date,
                    plate_no=route.plate_no
                ).values_list('no_seat', flat=True)
                booked_seats = set(int(seat) for seat in booked_tickets)
                booked_seat_count = len(booked_seats)        
                remaining_seats = total_seats - booked_seat_count
                unbooked_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
                if route.plate_no == plate_no and remaining_seats <= 0:
                    bus_full = True
                    route_info.append({
                    'route': route,
                    'remaining_seats': remaining_seats if remaining_seats > 0 else "Full"
                    })
            except Bus.DoesNotExist:
                continue
        route = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        if bus_full:
            return render(request, 'users/roote.html', {
            'error': 'This Bus is Full!',
            'routes': route,'buschanges_count': buschanges_count})
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date,plate_no=plate_no)
        all_seats = list(range(1, total_seats + 1))  # Generate all seat numbers
        return render(request, 'users/ticket.html', {
            'routes': routes, 'remaining_seats': len(unbooked_seats),
            'buschanges_count': buschanges_count,
            'unbooked_seats': unbooked_seats, 'booked_seats': booked_seats, 'all_seats':  all_seats
        })


    return render(request, 'users/roote.html', {})

def details(request):
    return render(request, 'users/details.html')

def admindelete(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        row_count = CustomUser.objects.count()
        if row_count <= 1:
            admins = CustomUser.objects.all()
            return render(request, 'users/admindelet.html', {
                'admins': admins,
                'error': "Cannot delete admin. At least one account must exist."
            })
        deleted_count, _ = CustomUser.objects.filter(fname=fname, lname=lname, username=username).delete()
        if deleted_count > 0:
            admins = CustomUser.objects.all()
            return render(request, 'users/admindelet.html', {
                'admins': admins,
                'success': "Admin deleted successfully."
            })
        else:
            admins = CustomUser.objects.all()
            return render(request, 'users/admindelet.html', {
                'admins': admins,
                'error': "No admin found with the provided information."
            })
    admins = CustomUser.objects.all()
    if admins:
        return render(request, 'users/admindelet.html', {'admins': admins})
    else:
        return render(request, 'users/error.html', {'error': "There are no admins to delete."})
    return render(request, 'users/admindelet.html',{'admins': admins})



def delete(request):
    return render(request, 'users/admindelet.html')

def routedelete(request):
    routes = Route.objects.all()
    if request.method == 'POST':
        depcity = request.POST['depcity']
        descity = request.POST['descity']
        date = request.POST['date']
        plate_no = request.POST['plate_no']
        side_no = request.POST['side_no']

        booked_tickets = Ticket.objects.filter(
            depcity=depcity,
            descity=descity,
            date=date,
            plate_no=plate_no,
            side_no=side_no
        ).count()
        if booked_tickets > 0:
            return render(request, 'users/routedelete.html', {'routes': routes, 'error': "This Routes has booked Tickets.!!"})
        rows_deleted, _ = Route.objects.filter(
            depcity=depcity,
            descity=descity,
            date=date,
            plate_no=plate_no,
            side_no=side_no
        ).delete()
        routes = Route.objects.all()
        if rows_deleted > 0:
            return render(request, 'users/routedelete.html', {'routes': routes, 'success': "Route Deleted Successfully!"})
        else:
            return render(request, 'users/routedelete.html', {'routes': routes})
    routes = Route.objects.all()
    if routes.exists():
        return render(request, 'users/routedelete.html', {'routes': routes})
    else:
        return render(request, 'users/error.html', {'error': "There are no routes to delete."})

def buses(request):
    buses = Bus.objects.all()
    return render(request, 'users/buses.html',{'buses': buses})

def workerdelete(request):
    driver = Worker.objects.all()
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        try:
            worker = Worker.objects.get(plate_no=plate_no, side_no=side_no, fname=fname,lname=lname)
            worker.delete()
            return render(request, 'users/driverdelete.html', {
                'driver': driver,
                'success': 'Driver Deleted Successfully'
            })
        except Worker.DoesNotExist:
            return render(request, 'users/error.html',
                    {'error': 'There is No drivers for Deletion'})
        return render(request, 'users/error.html', {'error': 'there is no driver for delete'})
    return render(request, 'users/driverdelete.html',{'driver': driver})



def Showtickets(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')
        date = request.POST.get('date')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        route = Ticket.objects.filter(
            plate_no=plate_no,
            side_no=side_no,
            date=date,
            depcity=depcity,
            descity=descity
        )
        routes = Route.objects.filter(side_no=side_no)
        if route.exists():
            return render(request, 'users/ticketoche.html', {'route': route})
        else:
            return render(request, 'users/rooteee.html', {'error': 'There are no booked tickets for this route', 'routes': routes})
    return render(request, 'users/ticketoche.html')


def busdelete(request):
    buses = Bus.objects.all()
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('sideno')
        no_seats = request.POST.get('no_seats')

        try:
            bus = Bus.objects.get(plate_no=plate_no, sideno=side_no, no_seats=no_seats)
            bus.delete()
            return render(request, 'users/busdelet.html', {
                'buses': buses,
                'success': 'Bus Deleted Successfully'
            })
        except Bus.DoesNotExist:
            return render(request, 'users/busdelet.html', {
                'buses': buses,
                'error': 'There is No bus for Deletion'
            })
    return render(request, 'users/busdelet.html', {'buses': buses})

def citydelete(request):
    cities = City.objects.all()
    if request.method == 'POST':
        depcity = request.POST.get('depcity')
        try:
            dep = City.objects.get(depcity=depcity)
            dep.delete()
            cities = City.objects.all()
            return render(request, 'users/citydelet.html', {
                'cities': cities,
                'success': 'City Deleted Successfully'
            })
        except Fedback.DoesNotExist:
            return render(request, 'users/citydelet.html', {
                'cities': cities,
                'error': 'There is No city for Deletion'
            })
    return render(request, 'users/citydelet.html',{'cities': cities})

def commentdelete(request):
    comments = Feedback.objects.all()  # Always fetch comments at the start
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        try:
            comment = Feedback.objects.get(name=name, email=email, phone=phone)
            comment.delete()
            comments = Feedback.objects.all()
            return render(request, 'users/commentdelet.html', {
                'comments': comments,
                'success': 'Comment Deleted Successfully'
            })
        except Feedback.DoesNotExist:
            return render(request, 'users/commentdelet.html', {
                'comments': comments,
                'error': 'There is No comment for Deletion'
            })
    return render(request, 'users/commentdelet.html', {'comments': comments})



def updatebus(request):
    buses = Bus.objects.all()  # Fetch all bus records

    if request.method == "POST":
        plate_no = request.POST.get('plate_no')
        new_sideno = request.POST.get('new_sideno')
        no_seats = request.POST.get('no_seats')
        sideno = request.POST.get('sideno')
        try:
            bus = Bus.objects.get(plate_no=plate_no)  # Assuming plate_no is unique
            
            if Bus.objects.filter(sideno=new_sideno).exists():
                return render(request, 'users/busupdate.html', {
                    'error1': 'This side no is already exist.',
                    'buses': buses
                })


            # Update the bus side number and no_seats
            bus.sideno = new_sideno
            bus.no_seats = no_seats
            bus.save()

            # Update side number for all workers associated with this bus
            Worker.objects.filter(plate_no=plate_no).update(side_no=new_sideno)
            Route.objects.filter(plate_no=plate_no).update(side_no=new_sideno)

            return render(request, 'users/busupdate.html', {
                'success': 'Side No changed successfully!',
                'buses': buses
            })

        except Bus.DoesNotExist:
            return render(request, 'users/busupdate.html', {
                'error': 'Bus not found.',
                'buses': buses
            })
    return render(request, 'users/busupdate.html', {'buses': buses})




from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from .models import Bus, Route, Ticket, Buschange

def changebus(request):
    routes = Route.objects.all()
    buses = Bus.objects.all()

    if request.method == "POST":
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')
        side_no = request.POST.get('side_no')
        new_side_no = request.POST.get('new_side_no')

        try:
            if Route.objects.filter(side_no=new_side_no, date=date).exists():
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'This bus is already reserved for route for this date.'
                })
            bus_info = Bus.objects.filter(sideno=new_side_no).first()
            if not bus_info:
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'Invalid side number selected.'
                })

            new_plate_no = bus_info.plate_no
            total_seats = int(bus_info.no_seats) if bus_info.no_seats else 0

            booked_tickets_count = Ticket.objects.filter(
                date=date,
                side_no=side_no
            ).count()
            if booked_tickets_count > total_seats:
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'Not enough seats available for this change.'
                })

            route = Route.objects.get(depcity=depcity, descity=descity, date=date, side_no=side_no)
            route.plate_no = new_plate_no
            route.side_no = new_side_no
            route.save()

            # Handle reciprocal route updates if necessary
            if depcity.strip() == "Addisababa":
                reciprocal_route = Route.objects.get(
                    depcity=descity,
                    descity=depcity,
                    date=(timezone.datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'),
                    side_no=side_no
                )
                reciprocal_route.plate_no = new_plate_no
                reciprocal_route.side_no = new_side_no
                reciprocal_route.save()

            # Update tickets with the new bus details
            Ticket.objects.filter(
                date=date,
                side_no=side_no
            ).update(
                plate_no=new_plate_no,
                side_no=new_side_no
            )

            # Get booked seats and calculate available seats
            booked_tickets = Ticket.objects.filter(
                date=date,
                side_no=new_side_no
            ).values_list('no_seat', flat=True)
            booked_seats = set(int(seat) for seat in booked_tickets)
            booked_seat_count = len(booked_seats)
            remaining_seats = total_seats - booked_seat_count
            unbooked_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

            Buschange.objects.create(
                plate_no=side_no,
                side_no=side_no,
                new_plate_no=new_plate_no,
                new_side_no=new_side_no,
                date=date,
                depcity=depcity,
                descity=descity
            )

            return render(request, 'users/buschange.html', {
                'routes': routes,
                'buses': buses,
                'success': 'Bus changed successfully.',
                'total_seats': total_seats,
                'booked_seats': booked_seat_count,
                'remaining_seats': remaining_seats,
                'unbooked_seats': unbooked_seats,
                'booked_seat_list': booked_seats
            })
        except Route.DoesNotExist:
            return render(request, 'users/buschange.html', {
                'routes': routes,
                'buses': buses,
                'error': "The specified route does not exist."
            })

    return render(request, 'users/buschange.html', {
        'routes': routes,
        'buses': buses
    })

def changebus_redirect(request):
    return redirect('changebus')

def changebuses(request):
    des = City.objects.all()
    if request.method == 'POST':
        date = request.POST.get('date')
        buschanges = Buschange.objects.filter(date=date)
        if buschanges.exists():
            count = Buschange.objects.filter(date=date).count()
            return render(request, 'users/busschange.html', {'count': count, 'buschange': buschanges})  # Pass the queryset
        else:
            buschanges = Buschange.objects.all()
            buschanges_count = buschanges.count()
            return render(request, 'users/index.html', {'buschanges_count': buschanges_count, 'error1': "NO change buses for this travel date!",'des': des})
    return render(request, 'users/index.html')



from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser  # Adjust the import as necessary
import re

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


"""
def change_password_view(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        re_new_password = request.POST.get('reNewPassword')

        # Authenticate the user with the current password
        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            # Check if new password and confirm password match
            if new_password == re_new_password:
                user.set_password(new_password)  # Set the new password securely
                user.save()  # Save the user instance
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, "Your password has been changed successfully.")
                #return redirect(request, 'users/profile2.html', {'success': 'Your password has been changed successfully.'})  # Redirect to a success page
            else:
                messages.error(request, "New passwords do not match.")
                #return render(request, 'users/profile2.html', {'error': 'Passwords do not match.'})
        else:
            #return render(request, 'users/change_password.html', {'error': 'Current password is incorrect.'})
            messages.error(request, "Current password is incorrect.")
    return render(request, 'users/profile2.html')
"""


"""
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        re_new_password = request.POST.get('reNewPassword')

        # Authenticate the user with the current password
        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            # Check if new password and confirm password match
            if new_password == re_new_password:
                user.set_password(new_password)  # Set the new password securely
                user.save()  # Save the user instance
                update_session_auth_hash(request, user)  # Important!
                #messages.success(request, "Your password has been changed successfully.")
                return redirect(request, 'users/profile.html', {'success': 'Your password has been changed successfully.'})  # Redirect to a success page
            else:
                messages.error(request, "New passwords do not match.")
                #return render(request, 'users/profile2.html', {'error': 'Passwords do not match.'})
        else:
            return render(request, 'users/change_password.html', {'error': 'Current password is incorrect.'})
            #messages.error(request, "Current password is incorrect.")
    return render(request, 'users/profile2.html')
"""



from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        re_new_password = request.POST.get('reNewPassword')

        # Authenticate the user with the current password
        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            # Check if new password and confirm password match
            if new_password == re_new_password:
                # Check if the new password is the same as the current password
                if current_password == new_password:
                    messages.error(request, "New password cannot be the same as the current password.")
                else:
                    user.set_password(new_password)  # Set the new password securely
                    user.save()  # Save the user instance
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(request, "Your password has been changed successfully.")

                    # Redirect to the profile page after successful password change
                    return redirect('profile')  # Change this to 'profile' to redirect to the profile view
            else:
                messages.error(request, "New passwords do not match.")
        else:
            messages.error(request, "Current password is incorrect.")

    return render(request, 'users/profile2.html')  # Render the change password form if GET request












"""
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        re_new_password = request.POST.get('reNewPassword')

        # Authenticate the user with the current password
        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            # Check if new password and confirm password match
            if new_password == re_new_password:
                user.set_password(new_password)  # Set the new password securely
                user.save()  # Save the user instance
                update_session_auth_hash(request, user)  # Important!
                #messages.success(request, "Your password has been changed successfully.")
                return render(request, 'users/profile.html', {
                    'success': 'Your password has been changed successfully.'  # Use your actual context variable
                })
                print(success)
                #return redirect('profile')  # Redirect to a success page (change 'profile' to your actual URL name)
            else:
                return render(request, 'users/profile2.html', {
                    'error': 'New passwords do not match.'# Use your actual context variable
                })
                #messages.error(request, "New passwords do not match.")
        else:
            return render(request, 'users/profile2.html', {
                    'error': 'Current password is incorrect.'# Use your actual context variable
                })
            #messages.error(request, "Current password is incorrect.")
    return render(request, 'users/profile2.html')  # Render the change password template
"""

# views.py
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import render
from django.conf import settings
#from .forms import UsernameEmailForm

def password_reset_request(request):
    if request.method == 'POST':
        form = UsernameEmailForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            user = None

            if username:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = None

            if email:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    user = None

            if user:
                # Send password reset email
                subject = "Password Reset Requested"
                email_template_name = "users/password_reset_email.html"
                c = {
                    "email": user.email,
                    'domain': request.META['HTTP_HOST'],
                    'site_name': 'Your Site Name',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [user.email])
                
                return render(request, 'users/password_reset_done.html')  # Create this template

    form = UsernameEmailForm()
    return render(request, 'users/password_reset.html', {'form': form})




def registor(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()

    des = City.objects.all()  # Fetch all cities
    bus = Bus.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        if password1 != password2:
            return render(request, 'users/register.html', {'error': 'Passwords do not match.','buschanges_count': buschanges_count})
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'Username already exists.','buschanges_count': buschanges_count})
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'users/register.html', {'error': 'Email already exists.','buschanges_count': buschanges_count})
        if CustomUser.objects.filter(phone=phone).exists():
            return render(request, 'users/register.html', {'error': 'Phone already exists.','buschanges_count': buschanges_count})
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password1,
            phone=phone,
            fname=fname,
            lname=lname,
            gender=gender
        )
        user.save()
        return render(request, 'users/register.html', {'success': 'User registored Successfully.','buschanges_count': buschanges_count})
    return render(request, 'users/register.html',{'buschanges_count': buschanges_count, 'bus': bus, 'des': des})
