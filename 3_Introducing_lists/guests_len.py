'''
3-9. Dinner Guests:
Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.
'''

DINNER_GUESTS = ['plato', 'socrates', 'aristotle']
INVITE_MSG = ", you've been invited to dinner!"
CANCEL_MSG = ", can't make it to dinner :("
NEW_INVITE_MSG = ", we look forward to having dinner with you!"
UPDATE_INVITE_MSG = ", join us at our big dinner table!"
UNINVITE_MSG = ", I'm sorry to inform you that you're no longer invited for dinner."
FINAL_INVITE_MSG = ", you're still invited for dinner :D"

print("--- Sending out dinner invitations: ---")
print(DINNER_GUESTS[0].title() + INVITE_MSG)
print(DINNER_GUESTS[1].title() + INVITE_MSG)
print(DINNER_GUESTS[2].title() + INVITE_MSG)
print("\nTotal invited guests: " + str(len(DINNER_GUESTS)))

CANCELED_GUEST = DINNER_GUESTS.pop(1)
print("\n--- Change in dinner plans: ---")
print(CANCELED_GUEST.title() + CANCEL_MSG)
print("\nTotal invited guests: " + str(len(DINNER_GUESTS)))

DINNER_GUESTS.append('epictetus')
print("\n--- Sending out new dinner invitations: ---")
print(DINNER_GUESTS[0].title() + NEW_INVITE_MSG)
print(DINNER_GUESTS[1].title() + NEW_INVITE_MSG)
print(DINNER_GUESTS[2].title() + NEW_INVITE_MSG)
print("\nTotal invited guests: " + str(len(DINNER_GUESTS)))

print("\n--- Another change in dinner plans: ---")
print("Exciting news: we've found a bigger dinner table!")

DINNER_GUESTS.insert(0, 'zeno')
DINNER_GUESTS.insert(2, 'aurelius')
DINNER_GUESTS.append('gaius')

print("\n--- Updated dinner guest invitations: ---")
print(DINNER_GUESTS[0].title() + UPDATE_INVITE_MSG)
print(DINNER_GUESTS[1].title() + UPDATE_INVITE_MSG)
print(DINNER_GUESTS[2].title() + UPDATE_INVITE_MSG)
print(DINNER_GUESTS[3].title() + UPDATE_INVITE_MSG)
print(DINNER_GUESTS[4].title() + UPDATE_INVITE_MSG)
print(DINNER_GUESTS[5].title() + UPDATE_INVITE_MSG)
print("\nTotal invited guests: " + str(len(DINNER_GUESTS)))

print("\n--- Unfortunate news: ---")
print("The new dinner table will not arrive on time :(")
print("There are too many guests on the invitation list.")

SIZE_TABLE = 2
TOT_GUESTS_INVITED = len(DINNER_GUESTS)
GUESTS_UNINVITED = TOT_GUESTS_INVITED - SIZE_TABLE
print(str(GUESTS_UNINVITED) + " guests will need to be uninvited.\n")

UNINVITED_GUEST = DINNER_GUESTS.pop(0)
GUESTS_UNINVITED = len(DINNER_GUESTS) - SIZE_TABLE
print(UNINVITED_GUEST.title() + UNINVITE_MSG)
print(str(GUESTS_UNINVITED) + " more guests will need to be uninvited.\n")

UNINVITED_GUEST = DINNER_GUESTS.pop(1)
GUESTS_UNINVITED = len(DINNER_GUESTS) - SIZE_TABLE
print(UNINVITED_GUEST.title() + UNINVITE_MSG)
print(str(GUESTS_UNINVITED) + " more guests will need to be uninvited.\n")

UNINVITED_GUEST = DINNER_GUESTS.pop(2)
GUESTS_UNINVITED = len(DINNER_GUESTS) - SIZE_TABLE
print(UNINVITED_GUEST.title() + UNINVITE_MSG)
print(str(GUESTS_UNINVITED) + " more guests will need to be uninvited.\n")

UNINVITED_GUEST = DINNER_GUESTS.pop(2)
GUESTS_UNINVITED = len(DINNER_GUESTS) - SIZE_TABLE
print(UNINVITED_GUEST.title() + UNINVITE_MSG)
print(str(GUESTS_UNINVITED) + " more guests will need to be uninvited.\n")

print("\n --- Final update: ---")
print(DINNER_GUESTS[0].title() + FINAL_INVITE_MSG)
print(DINNER_GUESTS[1].title() + FINAL_INVITE_MSG)
print("\nTotal invited guests: " + str(len(DINNER_GUESTS)))

print("\n --- Updated invitation list: ---")
del DINNER_GUESTS[0]
del DINNER_GUESTS[0]
print("Guests left on the list:", DINNER_GUESTS)
print("Guests left to invite: " + str(len(DINNER_GUESTS)))
