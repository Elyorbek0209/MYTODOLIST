from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def homeView(request):

    context = {
        'items': [
       
        {
        'title':'Gather treats for Dad',
        'description' : 'From cases to steaks and more',
        'image':'https://i5.peapod.com/c/EJ/EJP5U.jpg'
        },

        {
        'title':'Summer is grill season',
        'description' : 'Get grill essentials and get outside',
        'image':'https://i5.peapod.com/c/EF/EF1WD.jpg',
        },
        {
        'title':'Enjoy the season\'s best procude',
        'description' : 'Enjoy juicy tomatoes in June',
        'image':'https://i5.peapod.com/c/PS/PSO1P.jpg',
        },
        ],


        'items1': [
       
        {
        'description' : 'Deli meat & cheese',
        'image':'https://i5.peapod.com/c/EB/EBZ6S.jpg'
        },

        {
        'description' : 'The best seafood, better on the grill',
        'image':'https://i5.peapod.com/c/DA/DAA2B.jpg',
        },
        {
        'description' : 'Get everything for stellar sundaes',
        'image':'https://i5.peapod.com/c/3X/3X4MG.jpg',
        },
         {
        'description' : 'Hydration stations',
        'image':'https://i5.peapod.com/c/O7/O74X3.jpg',
        },
        ],


        'featured_Specials': [
       
        {
        'description' : 'Thomas\' English Muffins',
        'image':'https://i5.peapod.com/c/6O/6OQN9.png',
        'price': '$2.24',
        'date': 'Exp 06/11/2020'
        },

        {
        'description' : 'Kellogg\'s Cereal or Pop-Tarts',
        'image':'https://i5.peapod.com/c/0J/0J7Q4.jpg',
        'price': '$1.77',
        'date': 'Exp 06/11/2020'
        },
        {
        'description' : 'Pepperidge Farm Swirl Bread & More',
        'image':'https://i5.peapod.com/c/AV/AVX77.jpg',
        'price': '$1.99',
        'date': 'Exp 06/11/2020'
        },
        {
        'description' : 'Simply Orange Orange Juice & More',
        'image':'https://i5.peapod.com/c/1G/1GUKQ.jpg',
        'price': '2 for $6',
        'date': 'Exp 06/11/2020'
        },
        {
        'description' : 'Peet\'s coffee',
        'image':'https://i5.peapod.com/c/JL/JLC8R.jpg',
        'price': '$5.99',
        'date': 'Exp 06/11/2020'
        },
        ],

        'recommended': [
       
        {
        'measuredPrice': '1 bunch|$1.99/ea',
        'description' : 'Chiquita Bananas Yellow',
        'image':'https://i5.peapod.com/c/O5/O5SBH.jpg',
        'price': '$1.99',
        
        },

        {
        'measuredPrice': '16 oz pkg|$0.16 / oz',
        'description' : 'Strawberries',
        'image':'https://i5.peapod.com/c/RA/RA5DM.jpg',
        'price': '$1.99',
        },

        {
        'measuredPrice': '1 ea|$1.66/ea',
        'description' : 'Avocados Hass',
        'image':'https://i5.peapod.com/c/7K/7KTON.jpg',
        'price': '$1.66'
        },

        {
        'measuredPrice' : '1 bunch |$1.99/ea',
        'description' : 'Chiquita Bananas Green',
        'image':'https://i5.peapod.com/c/G7/G7U5A.jpg',
        'price': '$1.99',
        },
        {
        'measuredPrice' : 'apx 1 lb|$0.19/oz',
        'description' : 'Red Grapes Seedless',
        'image':'https://i5.peapod.com/c/BX/BX5LD.jpg',
        'price': '$2.99',
        },
        ],
    }

    return render(request, 'homeView.html', context)
