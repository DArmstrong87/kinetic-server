from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from kineticapi.models import Athlete, Organizer
from rest_framework import status


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of an athlete or organizer
    '''
    username = request.data['username']
    password = request.data['password']
    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)
    # If authentication was successful, respond with their token
    if authenticated_user is not None:

        organizer=None
        try:
            organizer = Organizer.objects.get(user=authenticated_user)
        except:
            pass

        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key,
            'is_athlete': True
        }
        if organizer is not None:
            data['is_athlete'] = False

        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication
    '''
    new_user = User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password'],
        first_name=request.data['firstName'],
        last_name=request.data['lastName']
    )

    # Check if new user is an athlete or organizer and create that instance.
    if request.data['isAthlete']:
        athlete = Athlete.objects.create(
            user=new_user,
            bio=request.data['bio'],
            dob=request.data['dob'],
            sex=request.data['sex'],
            VO2_max=request.data['VO2max'],
            rhr=request.data['rhr'],
            fluid_loss=request.data['fluidLoss'],
            sodium_loss=request.data['sodiumLoss'],
            weight=request.data['weight'],
            height=request.data['height'],
            is_athlete=request.data['isAthlete']
        )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=athlete.user)
        # Return the token to the client
        data = {'token': token.key}
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        organizer = Organizer.objects.create(
            user=new_user,
            organization=request.data['organization'],
            is_athlete=request.data['isAthlete']
        )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=organizer.user)
        # Return the token to the client
        data = {'token': token.key}
        return Response(data, status=status.HTTP_201_CREATED)
