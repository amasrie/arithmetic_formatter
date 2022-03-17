def add_time(start, duration, day=""):
  new_time = ""
  list_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  upper_list = list(map(str.upper,list_week))
  start_time, start_format = start.split(" ")
  opposite_format = "AM" if start_format == "PM" else "PM"
  start_hours, start_minutes = start_time.split(":")
  duration_hours, duration_minutes = duration.split(":")
  total_hours = int(duration_hours)
  total_minutes = int(start_minutes) + int(duration_minutes)
  if total_minutes > 59:
    total_minutes = total_minutes % 60
    total_hours += 1
  total_hours += int(start_hours)
  total_days = total_hours//24 if start_format == "AM" else (total_hours + 12)//24
  difference_hours = total_hours//12
  total_format = start_format if difference_hours%2 == 0 else opposite_format
  total_hours = total_hours%12
  new_time = f'{"12" if total_hours == 0 else total_hours}:{"0" if total_minutes < 10 else ""}{total_minutes} {total_format}'
  if len(day) > 0:
    week_day = (upper_list.index(day.upper()) + total_days) % 7
    new_time += f', {list_week[week_day]}'
  if total_days == 1:
    new_time += f' (next day)'
  elif total_days > 1:
    new_time += f' ({total_days} days later)'
  return new_time
