import uuid
import datetime

from src.data import db
from src.data.model.issue import Issue
from src.data.model.density import Density 



def save_new_issue(data):
    new_user = Issue(
        name="Cocaina",
        date=datetime.date.today(),
        plot_id=1,
        issue_type="Droga",
        description="Tiza"
    )
    save_changes(new_user)
    response_object = {
        'status': 'success',
        'message': 'Successfully registered.'
    }
    return response_object, 201


def get_all_issues():
    return Issue.query.all()


def get_a_issue(public_id):
    return Issue.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
