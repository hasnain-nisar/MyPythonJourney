# Can we have a set with 18(int) and 18 as (str)?

s = set()
s.add(18)
s.add("18")

print(s)

# output: {'18', 18}