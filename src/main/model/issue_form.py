from .form import Form


class IssueForm(Form):
    def __init__(self, date, time, plot, note, issue_type, description):
        super().__init__(date, time, plot, note)
        self.type = issue_type
        self.description = description
