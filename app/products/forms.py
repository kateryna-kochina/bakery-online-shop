###################################### EXAMPLE ######################################

# from flask_wtf import FlaskForm
# from wtforms import IntegerField, SubmitField
# from wtforms.validators import DataRequired
# import requests


# class RateMovieForm(FlaskForm):
#     rating = IntegerField("Your Rating Out of 10 e.g. 7.5")
#     review = IntegerField("Your Review")
#     submit = SubmitField("Done")


# class FindMovieForm(FlaskForm):
#     title = StringField("Movie Title", validators=[DataRequired()])
#     submit = SubmitField("Add Movie")

# @app.route("/edit", methods=["GET", "POST"])
# def rate_movie():
#     form = RateMovieForm()
#     movie_id = request.args.get("id")
#     movie = db.get_or_404(Movie, movie_id)
#     if form.validate_on_submit():
#         movie.rating = float(form.rating.data)
#         movie.review = form.review.data
#         db.session.commit()
#         return redirect(url_for('home'))
#     return render_template("edit.html", movie=movie, form=form)

# @app.route("/add", methods=["GET", "POST"])
# def add_movie():
#     form = FindMovieForm()
#     if form.validate_on_submit():
#         movie_title = form.title.data
#         response = requests.get(MOVIE_DB_SEARCH_URL, params={
#                                 "api_key": MOVIE_DB_API_KEY, "query": movie_title})
#         data = response.json()["results"]
#         return render_template("select.html", options=data)
#     return render_template("add.html", form=form)

###################################### EXAMPLE ######################################