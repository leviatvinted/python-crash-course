'''
The following exercises are a bit more complex than those in Chapter 2, but
they give you an opportunity to use lists in all of the ways described.

3-4. Guest List: 
If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you'd like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.

3-5. Changing Guest List: 
You just heard that one of your guests can't make the
dinner, so you need to send out a new set of invitations. You'll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can't make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.

3-6. More Guests: 
You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

3-7. Shrinking Guest List: 
You just found out that your new dinner table won't
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you're sorry you can't invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they're still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
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

CANCELED_GUEST = DINNER_GUESTS.pop(1)
print("\n--- Change in dinner plans: ---")
print(CANCELED_GUEST.title() + CANCEL_MSG)

DINNER_GUESTS.append('epictetus')
print("\n--- Sending out new dinner invitations: ---")
print(DINNER_GUESTS[0].title() + NEW_INVITE_MSG)
print(DINNER_GUESTS[1].title() + NEW_INVITE_MSG)
print(DINNER_GUESTS[2].title() + NEW_INVITE_MSG)

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

print("\n--- Unfortunate news: ---")
print("The new dinner table will not arrive on time :(\n")

UNINVITED_GUEST = DINNER_GUESTS.pop(0)
print(UNINVITED_GUEST.title() + UNINVITE_MSG)

UNINVITED_GUEST = DINNER_GUESTS.pop(1)
print(UNINVITED_GUEST.title() + UNINVITE_MSG)

UNINVITED_GUEST = DINNER_GUESTS.pop(2)
print(UNINVITED_GUEST.title() + UNINVITE_MSG)

UNINVITED_GUEST = DINNER_GUESTS.pop(2)
print(UNINVITED_GUEST.title() + UNINVITE_MSG)

print("\n --- Final update: ---")
print(DINNER_GUESTS[0].title() + FINAL_INVITE_MSG)
print(DINNER_GUESTS[1].title() + FINAL_INVITE_MSG)

del DINNER_GUESTS[0]
del DINNER_GUESTS[0]
print("\nGuests left on the list:", DINNER_GUESTS)
