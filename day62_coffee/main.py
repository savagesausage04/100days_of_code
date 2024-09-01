from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps (URL)', validators=[URL()])
    opening_time = StringField('Opening Time (eg. 8AM)')
    closing_time = StringField('Closing Time (eg. 5:30PM)')
    coffee_rating = SelectField('Coffee Rating', choices=[('☕️'), ('☕☕'), ('☕☕☕'), ('☕☕☕☕'), ('☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Strength Rating', choices=[('📱'), ('📱📱'), ('📱📱📱'), ('📱📱📱📱'), ('📱📱📱📱📱')])
    outlet_rating = SelectField('Power Outlet Rating', choices=[('🔌'), ('🔌🔌'), ('🔌🔌🔌'), ('🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌')])

    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        f = open("cafe-data.csv", "a")
        f.write(f"\n{form.cafe.data},{form.cafe_location.data},{form.opening_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.outlet_rating.data}")
        f.close()
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
