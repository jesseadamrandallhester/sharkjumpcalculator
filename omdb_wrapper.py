import omdb
omdb.set_default('apikey', '20b75a93')
from episode import make_episode

def get_show_poster(title):
  return omdb.get(title=title)["poster"]

def get_all_episodes(title):
  show_info = omdb.get(title=title)
  num_seasons = int(show_info["total_seasons"])
  episodes = []
  season = 1
  while season <= num_seasons:
    episodes.extend(get_episodes_in_season(title, season))
    season += 1
  return episodes

def get_all_rated_episodes(title):
  all_episodes = get_all_episodes(title)
  return [ep for ep in all_episodes if ep.rating]

def get_episodes_in_season(title, season):
  episodes_json = omdb.get(title=title, season=season)["episodes"]
  episodes = []
  for ej in episodes_json:
    episodes.append(make_episode(ej["title"], ej["released"], season, ej["episode"], ej["imdb_rating"]))
  return episodes
