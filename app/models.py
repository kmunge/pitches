from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch(db.Model):
    '''
    Pitch class to define the Pitch Objects
    '''
    __tablename__='pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_category = db.Column(db.String)
    pitch = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()
    
    @classmethod
    def get_pitches(cls,pitch_category):
        pitches = Pitch.query.filter_by(pitch_category = pitch_category).all()
        return pitches

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(id=id).first()

        return pitch    


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))


    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()
        
        return comments

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
        

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

class Comment(db.Model):
    
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comments= db.Column(db.String)
    pitch_id = db.Column(db.Integer)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    


    def save_comment(self):
        '''
        Function that saves each pitches comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments