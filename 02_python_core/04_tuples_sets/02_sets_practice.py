# Task 2: Set Operations & Analytics

day1_registrations = ["aman@test.com", "priya@test.com", "rahul@test.com", "aman@test.com", "sneha@test.com"]
day2_registrations = ["rahul@test.com", "amit@test.com", "priya@test.com", "vikram@test.com"]

# 1. Convert both lists into sets to clean up duplicate registrations.
day1_set = set(day1_registrations)
day2_set = set(day2_registrations)

# 2. Perform set operations and print results:
print("Total unique attendees across both days (Union):", day1_set | day2_set)
print("Attendees who came on both days (Intersection):", day1_set & day2_set)
print("Attendees who registered only on Day 1 (Difference):", day1_set - day2_set)
print("Attendees who registered for only one of the days (Symmetric Difference):", day1_set ^ day2_set)

# 3. Add a new email "kabir@test.com" to the Day 2 set and print the updated set.
day2_set.add("kabir@test.com")

# 4. Remove "vikram@test.com" from the Day 2 set safely
# Note: discard() is safer than remove() as it doesn't raise a KeyError if the element doesn't exist.
day2_set.discard("vikram@test.com")
print("Day 2 set after adding a new email and removing one:", day2_set)
