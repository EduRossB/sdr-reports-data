# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property

from sdr_reports_data.database import Column, PkModel, db, reference_col, relationship
from sdr_reports_data.extensions import bcrypt



class Lista1(PkModel):
    """Modelo para la primera lista CSV."""

    __tablename__ = "lista1"

    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String(80), nullable=False)
    last_name = Column(db.String(80), nullable=False)
    url = Column(db.String(255), nullable=False)
    email_address = Column(db.String(80), nullable=False)
    company = Column(db.String(100), nullable=False)
    position = Column(db.String(100), nullable=False)
    connected_on = Column(db.Date, nullable=True)
    
    def __repr__(self):
        """Representa la instancia como una cadena única."""
        return f"<Lista1({self.first_name} {self.last_name})>"

class Lista2(PkModel):
    """Modelo para la segunda lista CSV."""

    __tablename__ = "lista2"

    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String(80), nullable=False)
    last_name = Column(db.String(80), nullable=False)
    linkedin_url = Column(db.String(255), nullable=False)
    email = Column(db.String(80), nullable=False)
    company = Column(db.String(100), nullable=False)
    title = Column(db.String(100), nullable=False)
    seniority = Column(db.String(100), nullable=True)
    last_contacted = Column(db.Date, nullable=True)
    website = Column(db.String(255), nullable=True)
    industry = Column(db.String(100), nullable=True)
    city = Column(db.String(100), nullable=True)
    state = Column(db.String(100), nullable=True)
    country = Column(db.String(100), nullable=True)
    
    def __repr__(self):
        """Representa la instancia como una cadena única."""
        return f"<Lista2({self.first_name} {self.last_name})>"












class Role(PkModel):
    """A role for a user."""

    __tablename__ = "roles"
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Role({self.name})>"


class User(UserMixin, PkModel):
    """A user of the app."""

    __tablename__ = "users"
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    _password = Column("password", db.LargeBinary(128), nullable=True)
    created_at = Column(
        db.DateTime, nullable=False, default=dt.datetime.now(dt.timezone.utc)
    )
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    @hybrid_property
    def password(self):
        """Hashed password."""
        return self._password

    @password.setter
    def password(self, value):
        """Set password."""
        self._password = bcrypt.generate_password_hash(value)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self._password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"
