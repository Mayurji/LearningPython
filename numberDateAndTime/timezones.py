from datetime import datetime
from threading import local
from pytz import timezone

# Chicago TZ to Bengaluru TZ
d = datetime(2021, 12, 31, 2, 45, 0)
central = timezone('US/Central')
local_d = central.localize(d)
print(f"US localized Time {local_d}")

#Convert to Bengaluru Time
beng_z = local_d.astimezone(timezone('Asia/Kolkata'))
print(f'Bengaluru TZ: {beng_z}')