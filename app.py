from sharkjump import summarize_show
from flask import Flask, render_template, redirect, url_for, jsonify, request
from config import Config
from forms import ShowSearchForm

application = Flask(__name__, template_folder='views')
application.config.from_object(Config)

@application.route('/', methods = ['GET', 'POST'])
@application.route('/index', methods = ['GET', 'POST'])
def index():
  form = ShowSearchForm()
  if form.validate_on_submit():
    try:
      show_summary = summarize_show(form.show_name.data)
      eras = show_summary["eras"]
      poster_url = show_summary["poster"]
      return render_template('show_search.html', form=form, eras=eras, poster_url=poster_url)
    except:
      return render_template('search_error.html', form=form, show_name=form.show_name.data)
  else:
    return render_template('show_search.html', form=form, eras=None)

if __name__ == '__main__':
  application.run(host = '0.0.0.0')
