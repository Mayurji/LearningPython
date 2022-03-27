"""Function taking positional and keyword args"""

def profile(*personal, **professional):
    print(f'Personal Detail: {[p for p in personal]}')
    print(f'Professional Detail: {professional}')
    
profile('mayur', 'male', '30', work='MLE', org="python", pay='1M')