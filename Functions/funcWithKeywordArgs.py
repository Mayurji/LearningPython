"""Function with arbitrary no. of keyword arguments"""

def profile(name, gender, **attrs):
    common = {"name": name, "gender": gender}
    common.update(attrs)
    return common
print(profile('mayur', 'male', books=10, work='mle'))