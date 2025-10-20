"""
8-13. User Profile: 

Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('john', 'doe',
                             location='harvard',
                             field='quantum physics',
                             hobby='magic')
print(user_profile)
