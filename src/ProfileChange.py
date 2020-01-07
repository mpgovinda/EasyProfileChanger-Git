import subprocess, sys

# Simple profile changer for my github accounts!.

current_gloabl_username = subprocess.call("git config --global user.name", shell=True)
current_gloabl_email = subprocess.call("git config --global user.email", shell=True)

profiels = [
    {
        'username': '',
        'email': '',
        'state': 'personal'
    },
    {
        'username': '',
        'email': '',
        'state': 'work'
    },
]

decision = input('Do you want to change the the profile? (y/N)')

if decision == ('y' or 'Y'):
    next_username = input('Enter username: ')
    for p in profiels:
        if p['username'] == next_username:
            profile = p

    subprocess.run(["git", "config", "--global", "user.name", "\"{}\"".format(profile['username'])])
    subprocess.run(["git", "config", "--global", "user.email", "\"{}\"".format(profile['email'])])

else:
    print('Profile didn\'t changed.\nExit!')