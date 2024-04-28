# it is very easy to place/replace variable in strings by(string formatin)
letter = "Hi {} how  are you, you are from {}"
name = "yash"
place = "karnataka"
# --- now we add (name and place in {})
print(letter.format(name, place))
# or same thing can be done more easily so that for perticular item we can change
print(f"Hi {name} how  are you, you are from {place}")
# -same output-----


print("\n")
# ----2f----
#here it convent decimal point to 2 decimal point

txt = "Rs {prize:.2f} Rupee!"
print(txt.format(prize = 49.0999988))