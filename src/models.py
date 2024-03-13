from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    
    def __repr__(self):
        return f'<Favorites {self.id}>'

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id
        }

class People (db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    height = db.Column(db.Integer(), nullable=False)
    hair_color = db.Column(db.String(255), nullable=False)
    skin_color = db.Column(db.String(255), nullable=False)
    eye_color = db.Column(db.String(255), nullable=False)
    birth_year = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    homeworld = db.Column(db.Integer(), db.ForeignKey('planets.id'), nullable=True)
    favorites = db.relationship('Favorites', backref='people', lazy=True)
    
    def __repr__(self):
        return '<People %r>' % self.name
    
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "height" : self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld,
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    diameter = db.Column(db.Integer(), nullable=False)
    rotation_period = db.Column(db.Integer(), nullable=False)
    orbital_period = db.Column(db.Integer(), nullable=False)
    gravity = db.Column(db.Integer(), nullable=False)
    population = db.Column(db.Integer(), nullable=False)
    climate = db.Column(db.String(255), nullable=False)
    terrain = db.Column(db.String(255), nullable=False)
    surface_water = db.Column(db.Integer(), nullable=False)
    favorites = db.relationship('Favorites', backref='planets', lazy=True)
    
    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
        }