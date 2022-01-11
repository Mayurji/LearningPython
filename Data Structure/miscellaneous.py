from operator import attrgetter

"""
Sort objects of same class, which doesn't natively support comparison operation.
"""

class User:
    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def __repr__(self) -> str:
        return 'User({})'.format(self.user_id)

users = [User(4), User(56), User(23)]
print(f'Sorted By User Id: {sorted(users, key=lambda k: k.user_id)}')

# Using Attribute Getter
print(f"Sorted By User Id: {sorted(users, key=attrgetter('user_id'))}")