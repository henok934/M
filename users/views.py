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
    return render(request, 'users/profile.html')
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
def offers(request):
    buschanges = Buschange.objects.all()
    buschanges_count = buschanges.count()
    des = City.objects.all()
    context = {
        'des': des,
    }

    if buschanges_count > 0:
        context['buschanges_count'] = buschanges_count
    return render(request, 'users/cheeckrout.html', context)


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

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in

            # Redirect based on role
            if role == 'user':
                return render(request, 'users/profile.html', {'user': user})  # Redirect to the admin page
            elif role == 'worker':
                try:
                    worker = Worker.objects.get(username=username)
                    routes = Route.objects.filter(side_no=worker.side_no)
                    return render(request, 'users/rooteee.html', {'routes': routes})
                except Worker.DoesNotExist:
            
                    return render(request, 'users/login.html', {'error': 'This username Worker not found', 'buschanges_count': buschanges_count})
            

            """
            elif role == 'user':
                return render(request, 'users/profile.html', {'user': user})
            
            else:
                return render(request, 'users/login.html', {'error': 'Invalid role specified', 'buschanges_count': buschanges_count})
            """


        else:
            # Invalid username or password
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

def ticket(request):
    des = City.objects.all()
    bus = Bus.objects.all()
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
        #print("Received data:", request.POST)
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
        ticket = Ticket.objects.create(
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
        ticket.save()
        return render(request, 'users/ticket.html', {
            'bus': bus,
            'des': des,
            'success': 'Ticket booked successfully!'
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
            return render(request, 'users/tickets.html', {'ticket': ticket, 'success': "Your Ticket is:"})
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



"""
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from geopy.distance import distance as geopy_distance
from geopy.exc import GeocoderTimedOut

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_distance_calculator")
    try:
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        return None
def calculate_distance(request):
    if request.method == 'GET':
        city1 = request.GET.get('city1')
        city2 = request.GET.get('city2')
        coords1 = get_coordinates(city1)
        coords2 = get_coordinates(city2)

        if coords1 and coords2:
            distance_value = geopy_distance(coords1, coords2).kilometers
            return JsonResponse({'distance': distance_value})
        else:
            return JsonResponse({'error': 'Could not find coordinates for one or both city names.'}, status=400)

from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import distance as geopy_distance
from geopy.exc import GeocoderTimedOut
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_distance_calculator")
    try:
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except GeocoderTimedOut:
        return None
def calculate_distance(request):
    distance_value = None
    error_message = None
    city1 = None
    city2 = None
    if request.method == 'POST':
        city1 = request.POST.get('city1')
        city2 = request.POST.get('city2')
        coords1 = get_coordinates(city1)
        coords2 = get_coordinates(city2)

        if coords1 and coords2:
            distance_value = geopy_distance(coords1, coords2).kilometers
        else:
            error_message = "Could not find coordinates for one or both city names."
    return render(request, 'users/route.html', {
        'distance': distance_value,
        'city1': city1,
        'city2': city2,
        'error_message': error_message,
    })
"""





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

"""
def delete_tickets(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        #no_seat = request.POST.get('no_seat')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        #price = request.POST.get('price')

        deleted_count, _ = Ticket.objects.filter(
            plate_no=plate_no,
            #side_no=side_no,
            date=date,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            #price=price,
            #no_seat=no_seat,
            depcity=depcity,
            descity=descity
        ).delete()
        print(depcity, descity, firstname,lastname, phone,date,depcity,descity,plate_no)
        route = Ticket.objects.filter(depcity=depcity,descity=descity,plate_no=plate_no,date=date)
        if deleted_count > 0:
            return render(request, 'users/deleteticket.html',{'success': 'Ticket Deleted successfully.', 'route': route})

        #else:
        #   return render(request, 'users/error.html', {'error': 'No ticket found to delete.'})
    return render(request, 'users/deleteticket.html', {'route': route})
"""

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

        print(f"Attempting to delete ticket with: {date}, {plate_no}, {firstname}, {lastname}, {phone}, {depcity}, {descity}")

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




"""
from django.shortcuts import render
from .models import City, Route, Bus, Ticket  # Adjust based on your actual model imports

def book(request):
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

            return render(request, 'users/roote.html', {'routes': routes, 'success': "Routes info---"})
        else:
            return render(request, 'users/cheeckroutee.html', {'des': des, 'error': "There is no Travel for this information!"})
    
    return render(request, 'users/cheeckroutee.html', {'des': des})



def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date, plate_no=plate_no)
        route_info = []
        bus_full = False
        total_seats = 0  # Initialize total_seats

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

                if remaining_seats <= 0:
                    bus_full = True

                route_info.append({
                    'route': route,
                    'remaining_seats': remaining_seats if remaining_seats > 0 else "Full"
                })

            except Bus.DoesNotExist:
                continue

        # Return the appropriate response based on bus_full status
        if bus_full:
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'routes': route_info  # Pass the same routes for display
            })

        all_seats = list(range(1, total_seats + 1))  # Generate all seat numbers
        unbooked_seats = [seat for seat in all_seats if seat not in booked_seats]

        return render(request, 'users/ticket.html', {
            'routes': route_info,
            'remaining_seats': len(unbooked_seats),
            'unbooked_seats': unbooked_seats,
            'booked_seats': booked_seats,
            'all_seats': all_seats
        })
    return render(request, 'users/roote.html', {})
"""











"""
def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        # Fetch all routes based on depcity, descity, and date
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)
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

                # Check if the bus is full
                if remaining_seats <= 0:
                    bus_full = True

                # Append route info regardless of bus fullness
                route_info.append({
                    'route': route,
                    'remaining_seats': remaining_seats if remaining_seats > 0 else "Full"
                })
            except Bus.DoesNotExist:
                continue

        # Render the template with all route information
        return render(request, 'users/ticket.html', {
            'routes': route_info,
            'bus_full': bus_full,  # Indicate if any bus is full
            'total_routes': len(route_info)  # Total number of routes found
        })
    return render(request, 'users/roote.html', {})
"""






"""
def calculate_seat_info(route):
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

        return total_seats, booked_seats, remaining_seats, unbooked_seats

    except Bus.DoesNotExist:
        return 0, set(), 0, []  # Default values if no bus found
def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        route_info = []
        bus_full = False
        total_seats = 0  # Initialize total_seats

        for route in routes:
            total_seats, booked_seats, remaining_seats, unbooked_seats = calculate_seat_info(route)

            if route.plate_no == plate_no and remaining_seats <= 0:
                bus_full = True

            route_info.append({
                'route': route,
                'remaining_seats': remaining_seats if remaining_seats > 0 else "Full"
            })
        if bus_full:
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'routes': route_info
            })
        if total_seats > 0:
            routes = Route.objects.filter(depcity=depcity, descity=descity, date=date, plate_no=plate_no)
            all_seats = list(range(1, total_seats + 1))  # Generate all seat numbers
            return render(request, 'users/ticket.html', {
                'routes': routes,
                'remaining_seats': len(unbooked_seats),
                'unbooked_seats': unbooked_seats,
                'booked_seats': booked_seats,
                'all_seats': all_seats
            })
    return render(request, 'users/roote.html', {})
"""







"""
def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        route_info = []
        bus_full = False
        total_seats = 0  # Initialize total_seats

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
        
        if bus_full:
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'routes': route_info
            })

        if total_seats > 0:
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
            routes = Route.objects.filter(depcity=depcity, descity=descity, date=date, plate_no=plate_no)
            all_seats = list(range(1, total_seats + 1))  # Generate all seat numbers
            return render(request, 'users/ticket.html', {
                'routes': routes,
                'remaining_seats': len(unbooked_seats),
                'unbooked_seats': unbooked_seats,
                'booked_seats': booked_seats,
                'all_seats': all_seats
            })
    return render(request, 'users/roote.html', {})

"""








"""
def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)

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

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date,plate_no=plate_no)
        if bus_full:
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'routes': routes
            })

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)
        all_seats = list(range(1, total_seats + 1))  # Generate all seat numbers

        return render(request, 'users/ticket.html', {
            'routes': routes,
            'remaining_seats': remaining_seats,
            'unbooked_seats': unbooked_seats,
            'booked_seats': booked_seats,
            'all_seats': all_seats  # Send all seats for rendering
        })
    return render(request, 'users/roote.html', {})
"""



"""
def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date)

        route_info = []
        bus_full = False

        for route in routes:
            try:
                bus = Bus.objects.get(plate_no=route.plate_no)
                total_seats = int(bus.no_seats)

                # Fetch booked tickets for the current route
                booked_tickets = Ticket.objects.filter(
                    depcity=route.depcity,
                    descity=route.descity,
                    date=route.date,
                    plate_no=route.plate_no
                ).values_list('no_seat', flat=True)

                # Convert booked tickets to a set of integers
                booked_seats = set(int(seat) for seat in booked_tickets)
                booked_seat_count = len(booked_seats)

                # Calculate remaining seats
                remaining_seats = total_seats - booked_seat_count

                # Create a list of unbooked seats
                unbooked_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

                # Check if the specific bus is full
                if route.plate_no == plate_no and remaining_seats <= 0:
                    bus_full = True

                # Append route information
                route_info.append({
                    'route': route,
                    'remaining_seats': remaining_seats if remaining_seats > 0 else "Full"
                })

            except Bus.DoesNotExist:
                continue  # Skip routes with no associated bus

        # Debugging output
        print(f"Route Information: {route_info}")

        # Handle the case where the bus is full
        if bus_full:
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'routes': route_info
            })

        # Fetch routes again for the specific plate number
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date, plate_no=plate_no)

        # Render the ticket page with the relevant data
        return render(request, 'users/ticket.html', {
            'routes': routes,
            'remaining_seats': remaining_seats,
            'unbooked_seats': unbooked_seats,
            'booked_seats': booked_seats
        })
    return render(request, 'users/roote.html', {})
"""





"""
from django.shortcuts import render
from .models import City, Route, Bus, Ticket

def book(request):
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
                    total_seats = int(bus.no_seats)
                except Bus.DoesNotExist:
                    total_seats = 0

                booked_tickets = Ticket.objects.filter(
                    depcity=route.depcity,
                    descity=route.descity,
                    date=route.date,
                    plate_no=route.plate_no
                ).count()
                remaining_seats = max(0, total_seats - booked_tickets)

                # Update remaining_seats to "Full" if no seats available
                if remaining_seats == 0:
                    remaining_seats = "Full"

                routes.append({
                    'route': route,
                    'remaining_seats': remaining_seats
                })

            return render(request, 'users/roote.html', {'routes': routes, 'success': "Routes info---"})
        else:
            return render(request, 'users/cheeckroutee.html', {'des': des, 'error': "There is no Travel for this information!"})

    return render(request, 'users/cheeckroutee.html', {'des': des})

def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        try:
            bus = Bus.objects.get(plate_no=plate_no)
            total_seats = int(bus.no_seats)
        except Bus.DoesNotExist:
            return render(request, 'users/roote.html', {
                'error': 'Bus not found!',
                'routes': []
            })

        booked_tickets = Ticket.objects.filter(
            depcity=depcity,
            descity=descity,
            date=date,
            plate_no=plate_no
        ).values_list('no_seat', flat=True)

        # Ensure seat numbers are integers
        booked_seats = set(int(seat) for seat in booked_tickets)

        # Count of booked seats
        booked_seat_count = len(booked_seats)

        # Calculate remaining seats
        remaining_seats = total_seats - booked_seat_count

        if remaining_seats <= 0:
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'remaining_seats': "Full",
                'routes': []
                print(f"Remaining Seats: {remaining_seats}")
                print(f"Routes: {routes}")
            })

        # Calculate unbooked seats
        unbooked_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

        # Fetch routes based on the criteria
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date, plate_no=plate_no)

        if routes.exists():
            return render(request, 'users/ticket.html', {
                'remaining_seats': remaining_seats,
                'unbooked_seats': unbooked_seats,
                'routes': routes
            })
    return render(request, 'users/roote.html', {})
def Select(request):
    if request.method == 'POST':
        plate_no = request.POST.get('plate_no')
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')

        try:
            bus = Bus.objects.get(plate_no=plate_no)
            total_seats = int(bus.no_seats)
        except Bus.DoesNotExist:
            return render(request, 'users/roote.html', {
                'error': 'Bus not found!',
                'routes': []
            })

        # Fetch booked seats
        booked_tickets = Ticket.objects.filter(
            depcity=depcity,
            descity=descity,
            date=date,
            plate_no=plate_no
        ).values_list('no_seat', flat=True)

        # Ensure seat numbers are integers
        booked_seats = set(int(seat) for seat in booked_tickets)

        # Count of booked seats
        booked_seat_count = len(booked_seats)

        # Calculate remaining seats
        remaining_seats = total_seats - booked_seat_count

        # Fetch routes based on the criteria
        routes = Route.objects.filter(depcity=depcity, descity=descity, date=date, plate_no=plate_no)

        # Debugging information
        print(f"Remaining Seats: {remaining_seats}")
        print(f"Routes: {routes}")

        if remaining_seats <= 0:
            # If the bus is full, prepare to show the route as full
            full_route_info = {
                'route': {
                    'depcity': depcity,
                    'descity': descity,
                    'date': date,
                    'plate_no': plate_no
                },
                'remaining_seats': "Full"
            }
            return render(request, 'users/roote.html', {
                'error': 'This Bus is Full!',
                'routes': [full_route_info]  # Display the full route
            })

        if routes.exists():
            return render(request, 'users/ticket.html', {
                'remaining_seats': remaining_seats,
                'unbooked_seats': [seat for seat in range(1, total_seats + 1) if seat not in booked_seats],
                'routes': [{'route': route, 'remaining_seats': remaining_seats} for route in routes]
            })
    return render(request, 'users/roote.html', {})
"""



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



"""
def updatebus(request):
    buses = Bus.objects.all()  # Fetch all bus records
    if request.method == "POST":
        plate_no = request.POST.get('plate_no')
        new_sideno = request.POST.get('new_sideno')
        sideno = request.POST.get('sideno')  # Wrap 'sideno' in quotes
        no_seats = request.POST.get('no_seats')
        try:
            bus = Bus.objects.get(plate_no=plate_no)  # Assuming plate_no is unique
            if Bus.objects.filter(sideno=new_sideno).exists():
                return render(request, 'users/busupdate.html', {
                    'error': 'The new Side No is already reserved for another bus.',
                    'buses': buses
                })
            bus.sideno = new_sideno
            bus.no_seats = no_seats
            bus.save()
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
"""



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


            """

            if Bus.objects.filter(plate_no=plate_no,no_seats=no_seats,sideno=new_sideno).exists():
                 return render(request, 'users/busupdate.html', {
                    'error1': 'No change the same as the first side No.',
                    'buses': buses
                })

            
            if Bus.objects.filter(sideno=new_sideno).exists():
                return render(request, 'users/busupdate.html', {
                'error': 'The new Side No is already reserved for another bus.',
                'buses': buses
                })

            if Bus.objects.filter(plate_no=plate_no, no_seats=no_seats, sideno=new_sideno).exists():
                return render(request, 'users/busupdate.html', {
                'error': 'No change; the same as the first side No.',
                'buses': buses
                })
            """

            """
            error = []  # Initialize an empty list to hold error messages

            # Check if the new side number is already reserved for another bus
            if Bus.objects.filter(sideno=new_sideno).exists():
                error.append('The new Side No is already reserved for another bus.')

            # Check if the new side number is the same as the existing bus
            if Bus.objects.filter(plate_no=plate_no, no_seats=no_seats, sideno=new_sideno).exists():
                error.append('No change; the same as the first side No.')

            # If there are any errors, render the template with the error messages
            if error:
                return render(request, 'users/busupdate.html', {
                'error': error,  # Pass the list of errors to the template
                'buses': buses
                })
            """


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



"""
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from .models import Bus, Route, Ticket, Buschange

def changebus(request):
    # Get all routes and buses
    routes = Route.objects.all()
    buses = Bus.objects.all()

    if request.method == "POST":
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')
        side_no = request.POST.get('side_no')
        new_side_no = request.POST.get('new_side_no')

        try:
            # Get bus information based on the new side number
            bus_info = Bus.objects.filter(sideno=new_side_no).first()

            if not bus_info:
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'Invalid side number selected.'
                })
        

            new_plate_no = bus_info.plate_no  # Assuming Bus model has a plate_no field
            total_seats = bus_info.no_seats  # Assuming Bus model has a no_seats field

            # Check if the new route already exists
            if Route.objects.filter(plate_no=new_plate_no, side_no=new_side_no).exists():
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': "Can't change b/c there is already a route with this combination."
                })

            booked_tickets_count = Ticket.objects.filter(
                date=date,
                side_no=side_no
            ).count()

            # Check for available seats
            if booked_tickets_count > total_seats:
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'Not enough seats available for this change.'
                })

            # Update the route information
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

                Buschange.objects.create(
                    plate_no=side_no,
                    side_no=side_no,
                    new_plate_no=new_plate_no,
                    new_side_no=new_side_no,
                    date=(timezone.datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'),
                    depcity=descity,
                    descity=depcity
                )

            # Update tickets for the old route
            Ticket.objects.filter(
                date=date,
                side_no=side_no
            ).update(
                plate_no=new_plate_no,
                side_no=new_side_no
            )

            # Log the bus change
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
                'success': 'Bus changed successfully.'
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
"""




"""
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
            bus_info = Bus.objects.filter(sideno=new_side_no).first()
            if not bus_info:
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'Invalid side number selected.'
                })

            new_plate_no = bus_info.plate_no
            total_seats = int(bus_info.no_seats) if bus_info.no_seats else 0

            if Route.objects.filter(plate_no=new_plate_no, side_no=new_side_no).exists():
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': "Can't change b/c this bus is has route for this date."
                })

            booked_tickets_count = Ticket.objects.filter(
                date=date,
                side_no=side_no
            ).count()

            # Check for available seats
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

                Buschange.objects.create(
                    plate_no=side_no,
                    side_no=side_no,
                    new_plate_no=new_plate_no,
                    new_side_no=new_side_no,
                    date=(timezone.datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'),
                    depcity=descity,
                    descity=
            for ticket in booked_tickets:
                # Assuming seat_no is a field in the Ticket model
                # Change the seat number based on the new bus's total seats
                #new_seat_no = (ticket.no_seat % total_seats) if total_seats > 0 else None
                new_seat_no = (int(ticket.seat_no) % total_seats) if total_seats > 0 else None
                ticket.plate_no = new_plate_no
                ticket.side_no = new_side_no
                ticket.no_seat = new_seat_no
                ticket.save()
                
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
                'success': 'Bus changed successfully.'
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
"""







"""
from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from .models import City, Bus, Route, Ticket, Buschange
def changebus(request):
    routes = Route.objects.all()  # Get all routes
    buses = Bus.objects.all()
    if request.method == "POST":
        depcity = request.POST.get('depcity')
        descity = request.POST.get('descity')
        date = request.POST.get('date')
        plate_no = request.POST.get('plate_no')
        side_no = request.POST.get('side_no')
        new_side_no = request.POST.get('new_side_no')
        new_plate_no = request.POST.get('new_plate_no')
        try:

            if Route.objects.filter(side_no=new_side_no, date=date, plate_no=new_plate_no).exists():
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'This bus is already reserved for route for this date.'
                })
            booked_tickets_count = Ticket.objects.filter(
                date=date,
                plate_no=plate_no,
                side_no=side_no
            ).count()
            total_seats = Bus.objects.filter(
                plate_no=new_plate_no,
                sideno=new_side_no  
            ).values_list('no_seats', flat=True).first()
            if total_seats is None:
                total_seats = 0
            try:
                total_seats = int(total_seats)
            except ValueError:
                total_seats = 0
            if booked_tickets_count > total_seats:
                return render(request, 'users/buschange.html', {
                    'buses': buses,
                    'routes': routes,
                    'error': 'There are not enough seats available for this change.'
                })
            route = Route.objects.get(depcity=depcity, descity=descity, date=date, plate_no=plate_no, side_no=side_no)
            route.plate_no = new_plate_no
            route.side_no = new_side_no
            route.save()
            if depcity.strip() == "Addisababa":
                reciprocal_route = Route.objects.get(
                    depcity=descity,
                    descity=depcity,
                    date=(timezone.datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'),
                    plate_no=plate_no,
                    side_no=side_no
                )
                reciprocal_route.plate_no = new_plate_no
                reciprocal_route.side_no = new_side_no
                reciprocal_route.save()

                Buschange.objects.create(
                    plate_no=plate_no,
                    side_no=side_no,
                    new_plate_no=new_plate_no,
                    new_side_no=new_side_no,
                    date=(timezone.datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d'),
                    depcity=descity,
                    descity=depcity
                )

            Ticket.objects.filter(
                date=date,
                plate_no=plate_no,
                side_no=side_no
            ).update(
                plate_no=new_plate_no,
                side_no=new_side_no
            )
            Buschange.objects.create(
                plate_no=plate_no,
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
                'success': 'Bus changed successfully.'
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
"""




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
