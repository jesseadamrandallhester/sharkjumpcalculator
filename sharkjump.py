from scipy import mean, std
from scipy.stats import ttest_ind
from omdb_wrapper import get_show_poster, get_all_rated_episodes

SIGNIFICANCE = 0.05
MIN_MEAN_DIFFERENCE_IN_SD = 0.5 
MIN_ERA_LENGTH = 8

def get_average_rating(rated_episodes):
	return round(mean([ep.rating for ep in rated_episodes]), 1)
	
def get_eras(episodes, significance = SIGNIFICANCE, min_mean_difference_in_sd = MIN_MEAN_DIFFERENCE_IN_SD, min_era_length = MIN_ERA_LENGTH):
  stddev, n, eras = (std([e.rating for e in episodes]), len(episodes), [])
  i = min_era_length
  current_era = episodes[0:i]
  while i < n:
    possible_next_era = episodes[i:(i + min_era_length)]
    if len(possible_next_era) < min_era_length: 
      current_era.extend(possible_next_era)
      break # because we must have reached the end of the show
    before = [ep.rating for ep in current_era]
    after = [ep.rating for ep in possible_next_era]
    p = ttest_ind(before, after).pvalue	
    if p < SIGNIFICANCE and abs(mean(before) - mean(after)) / stddev >= min_mean_difference_in_sd:
      eras.append(current_era)
      current_era = possible_next_era	
    else:
      current_era.extend(possible_next_era)
    i += min_era_length
  eras.append(current_era)
  return eras

def summarize_eras(episodes):
	eras = get_eras(episodes)
	return [era_summary(era) for era in eras]

def era_summary(era):
  return {'first episode' : era[0], 'last episode' : era[len(era) - 1],
		'episodes' : len(era), 'average rating' : get_average_rating(era)}	

def summarize_show(show_name):
  summary = {}
  summary['poster'] = get_show_poster(show_name)
  rated_episodes = get_all_rated_episodes(show_name)
  summary['eras'] = summarize_eras(rated_episodes)
  return summary	
