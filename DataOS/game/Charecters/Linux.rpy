define l = Character("Linux")
image linuxi = "linux[lin_gen if gender is None else gender]"
#gendered values are to be 3 letter between each _
default lin_gen = random.randint(0,1)