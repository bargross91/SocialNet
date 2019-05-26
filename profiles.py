# Finding a profile
def find_profile(user):
    user_profile = {}
    for profile in profiles:
        if profile['username'] == user:
            user_profile = profile

    return user_profile


# Profile list
profiles = [
  {
    'id': 1,
    'username': 'rachel_g',
    'first_name': 'Rachel',
    'last_name': 'Green',
    'picture': 'https://www.jetss.com/wp-content/uploads/2019/02/rachel-green-best-outfits-friends-11.jpg',
    'friends': [2, 5, 9],
  },
  {
    'id': 2,
    'username': 'ross_g',
    'first_name': 'Ross',
    'last_name': 'Geller',
    'picture': 'https://www.cheatsheet.com/wp-content/uploads/2018/09/Ross-Geller.png',
    'friends': [1, 8, 9],
  },
  {
    'id': 5,
    'username': 'phoebe_b',
    'first_name': 'Phoebe',
    'last_name': 'Buffay',
    'picture': 'https://i.pinimg.com/originals/8f/63/12/8f631249393db12cc105bd62ef017315.jpg',
    'friends': [1, 2, 9, 8],
  },
  {
    'id': 9,
    'username': 'joey_t',
    'first_name': 'Joey',
    'last_name': 'Tribbiani',
    'picture': 'https://imgix.bustle.com/rehost/2016/9/13/63de791f-8f44-4b24-8b07-43cf1f558406.png?w=970&h=546&fit=crop&crop=faces&auto=format&q=70',
    'friends': [2, 8, 1],
  },
 {
    'id': 8,
    'username': 'monica_g',
    'first_name': 'Monica',
    'last_name': 'Geller',
    'picture': 'https://imgix.bustle.com/rehost/2016/9/13/04a388e1-335b-4fad-969f-383866bddab7.png?w=970&h=546&fit=crop&crop=faces&auto=format&q=70',
    'friends': [2, 1],
  },
]

