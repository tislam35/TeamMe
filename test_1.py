import system
import users
from pprint import pprint

print("1.  " + str(system.system.OU_list))
print("2. " + str(system.system.OU_count))
user1 = users.OU("JohnCruz1", "pass123", "John", "Cruz", "John.123@gmail.com", "718-234-2341", "vollyball, chess")
user1.score = 20
system.system.OU_list.append(user1)
system.system.OU_count += 1
print("3. " + str(system.system.OU_list))
print("4. " + str(system.system.OU_count))
print("5. ")
pprint(vars(user1))

print("6." + str(system.system.FSU))
system.system.FSU = users.SU("FSU", "pass123", "Group", "S", "FSU@gmail.com", "718-123-567", "coding, teamwork")
system.system.FSU.score = 100
system.system.FSU.referenceInfo = ("kim.456@gmail.com", 20)
print("7." )
pprint(vars(system.system.FSU))

# get info  from GUI
entered_first_name = "Kim"
entered_last_name = "Zhang"
entered_email = "kim.456@gmail.com"
entered_phone_number = "718-234-6543"
entered_interests = "chess, basketball"
entered_reference_username = "FSU"



isSuccessRegister = system.system.register(entered_first_name, entered_last_name,
                                   entered_email, entered_phone_number,
                                   entered_interests, entered_reference_username)
print("7.8. " + str(system.system.registered_visitor_list))
print("7.9. " + str(system.system.OU_list))
print("8. " + str(isSuccessRegister))
# system.system.add_visitor_to_OU(entered_email)
system.system.approve("kim.456@gmail.com")
print("8.1. " + str(system.system.registered_visitor_list))
print("8.2. " + str(system.system.OU_list))
pprint(vars(system.system.OU_list[0]))


isSuccessLogin = system.system.login("KimZhang1", "KimZhang")
print("9: " + str(isSuccessLogin))

print("10.1 : " + str(system.system.find_user_by_username("KimZhang1").score))
print(system.system.OU_count)
print(system.system.VIP_count)
system.system.update_user_score("KimZhang1", 20)
print(system.system.OU_count)
print(system.system.VIP_count)
print("10.11: " + str(system.system.VIP_list))
print("10.2 : " + str(system.system.find_user_by_username("KimZhang1").score))

# print("11.0: " + str(system.system.OU_count))
# print("11.1: " + str(system.system.VIP_count))
# print("11.11: " + str(system.system.blacklist_count))
# system.system.blacklist_user("KimZhang1")
# print("11.2: " + str(system.system.OU_count))
# print("11.21: " + str(system.system.VIP_count))
# print("11.22: " + str(system.system.blacklist_count))

# print("11.0: " + str(system.system.OU_count))
# print("11.1: " + str(system.system.VIP_count))
# print("11.11: " + str(system.system.blacklist_count))
# system.system.kick("KimZhang1")
# print("11.2: " + str(system.system.OU_count))
# print("11.21: " + str(system.system.VIP_count))
# print("11.22: " + str(system.system.blacklist_count))

# print(len(system.system.complaints))
# # system.system.complain_user("KimZhang1", "I seem this person steal.")
# # print(system.system.complaints[0][0])
# # print(system.system.complaints[0][1])

# print(len(system.system.complaints))
# system.system.compliment("KimZhang1", "Very Nice")
# print(system.system.complaints[0][0])
# print(system.system.complaints[0][1])

# system.system.top_3()
# print(system.system.top_3())

