from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional
from FlaskBlogApp.models import User
from flask_login import current_user
"""Version 2"""


def maxImageSize(max_size=2):
    max_bytes = max_size * 1024 * 1024

    def _check_file_size(form, field):
        if len(field.data.read()) > max_bytes:
            raise ValidationErr(
                f'Το μέγεθος της εικόνας δεν μπορεί να υπερβαίνει τα {max_bytes} ΜΒ')

    return _check_file_size


class SignupForm(FlaskForm):
    username = StringField(label="Username",
                           validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                       Length(min=3, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες")])

    email = StringField(label="email",
                        validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                    Email(message="Παρακαλώ εισάγετε ένα σωστό email")])

    password = StringField(label="password",
                           validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                       Length(min=3, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες")])

    password2 = StringField(label="Επιβεβαίωση password",
                            validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                        Length(
                                min=3, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες"),
                                EqualTo('password', message='Τα δύο πεδία password πρέπει να είναι τα ίδια')])

    submit = SubmitField('Εγγραφή')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Αυτό το username υπάρχει ήδη')


class LoginForm(FlaskForm):

    email = StringField(label="email",
                        validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                    Email(message="Παρακαλώ εισάγετε ένα σωστό email")])

    password = StringField(label="password",
                           validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό.")])

    remember_me = BooleanField(label="Remember me")
    submit = SubmitField('Entrance')


class NewArticleForm(FlaskForm):
    article_title = StringField(label="Τίτλος Άρθρου",
                                validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                            Length(min=3, max=50, message="Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες")])

    article_body = TextAreaField(label="Κείμενο Άρθρου",
                                 validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                             Length(min=5, message="Το κείμενο του άρθρου πρέπει να έχει τουλάχιστον 5 χαρακτήρες")])

    submit = SubmitField('Αποστολή')


class AccountUpdateForm(FlaskForm):
    username = StringField(label="Username",
                           validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                       Length(min=3, max=15, message="Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες")])

    email = StringField(label="email",
                        validators=[DataRequired(message="Αυτό το πεδίο δε μπορεί να είναι κενό."),
                                    Email(message="Παρακαλώ εισάγετε ένα σωστό email")])

    profile_image = FileField('Εικόνα Προφίλ', validator=[Optional(strip_whitespace=True),
                                                          FileAllowed(
                                                              ['jpg', 'jpeg', 'png'], 'Επιτρέπονται συγκεκριμένα formats'),
                                                          maxImageSize(max_size=3)])

    submit = SubmitField('Αποστολή')

    def validate_username(self, username):

        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Αυτό το username υπάρχει ήδη')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Αυτό το email υπάρχει ήδη')
