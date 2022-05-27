from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


# WTForm
# Create a post form
class CreatePostForm(FlaskForm):
    title = StringField("Título de la Publicación", validators=[DataRequired()])
    subtitle = StringField("Subtitulo", validators=[DataRequired()])
    img_url = StringField("URL de la Imagen Principal", validators=[DataRequired(), URL()])
    body = CKEditorField("Contenido de la Publicación", validators=[DataRequired()])
    submit = SubmitField("Crear Publicación")


# Create a user form
class RegisterForm(FlaskForm):
    email = StringField("Correo Electrónico", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    name = StringField("Nombre", validators=[DataRequired()])
    submit = SubmitField("Registrarme!")


# Create a login form
class LoginForm(FlaskForm):
    email = StringField("Correo Electrónico", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Ingresar!")


# Create a Comment form
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comentario", validators=[DataRequired()])
    submit = SubmitField("Enviar Comentario")
