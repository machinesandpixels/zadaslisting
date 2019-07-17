from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        # Check if user has made inquery
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id,
                user_id=user_id
                )
            if has_contacted:
                messages.error(
                    request, 
                    'You have already made an inquiry for this listing.'
                    )
                # return redirect('/listings/', listing_id=listing_id)
                return redirect('/listings/'+listing_id)

        contact = Contact(

            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id

        )

        contact.save()

        # Send email
        
        # send_mail(
        #     "Zada's Listing Inquery",
        #     'There as been a inquery for ' + listing + '. Sign in for more info ',
        #     'myemail@gmail.com',
        #     [realtor_email, 'forwardemail@gmail.com'],
        #     fail_silently=False
        # )
        # messages.success(request, 'Your message has been sent and a Realtor will contact you shortly')

        # return redirect('/listings/', listing_id=listing_id)
        return redirect('/listings/'+listing_id)
