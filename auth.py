from flask import abort
from models.user import User
from flask_jwt_extended import get_jwt_identity
from setup import db


def authorize(user_id=None):
    """Checks whether is_admin is True or passed identity matches required
    identity, otherwise aborts request.

    Returns:
        function: Abort function to raise error if not authorized
    """
    jwt_user_id = get_jwt_identity()
    stmt = db.select(User).where(User.id == jwt_user_id)
    user = db.session.scalar(stmt)
    
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        return abort(401)