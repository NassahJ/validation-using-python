def greeting_app(name):
 approved_names = ["James","Daniel","Peter"]
 if name in approved_names:
  print("Welcome", name, "to level 3")
 else:
  print("User unauthorized")
greeting_app("James")