from collections import namedtuple
from datetime import datetime

Episode = namedtuple('Episode', ['title', 'date', 'season', 'number', 'rating'])

def make_episode(title, date_str, season, number, rating):
  # The OMDB API uses the date format 'YYYY-mm-dd'
  try:
    # ...but sometimes the date is 'N/A'
    date = datetime.strptime(date_str, "%Y-%m-%d")
  except:
    date = None
  season = int(season)
  number = int(number)
  try:
    # an unrated episode will have a rating of 'N/A'
    rating = float(rating)
  except:
    rating = None
  return Episode(title, date, season, number, rating)
