from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from exts import db
from shortuuid import uuid
from werkzeug.security import generate_password_hash, check_password_hash

class PermissionEnum(Enum):
    BOARD = '板块'
    POST = '帖子'
    COMMENT = '评论'
    FRONT_USER = '前台用户'
    CMS_USER = '后台用户'


class PermissionModel(db.Model):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(db.Enum(PermissionEnum), nullable=False, unique=True)
    role_permission_table = db.Table(
        'role_permission_table',
        Column('role_id', Integer, ForeignKey('role.id')),
        Column('permission_id', Integer, ForeignKey('permission.id'))
    )


class RoleModel(db.Model):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    desc = Column(String(200), nullable=True)
    create_time = Column(DateTime, default=datetime.now)
    permissions = db.relationship('PermissionModel', secondary=PermissionModel.role_permission_table, backref='roles')


class UserModel(db.Model):
    __tablename__ = 'user'
    id = Column(String(100), primary_key=True, default=uuid)
    username = Column(String(50), nullable=False, unique=True)
    _password = Column(String(200), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    avatar = Column(String(100))
    signature = Column(String(100))
    join_time = Column(DateTime, default=datetime.now)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    role_id = Column(Integer, ForeignKey('role.id'))
    role = db.relationship('RoleModel', backref='users')

    def __init__(self, *args, **kwargs):
        if 'password' in kwargs:
            self.password = kwargs.get('password')
            kwargs.pop('password')

        super(UserModel, self).__init__(*args, **kwargs)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    def has_permission(self, permission):
        return permission in [permission.name for permission in self.role.permission]
