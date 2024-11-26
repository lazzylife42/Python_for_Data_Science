import time
from datetime import datetime

epoch_time = float(time.time())
current_date = datetime.fromtimestamp(epoch_time).strftime('%b %d %Y')

# résultat 
print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2E} in scientific notation")
print(current_date)
