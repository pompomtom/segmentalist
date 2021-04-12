from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, SelectField, StringField, SelectMultipleField, PasswordField, BooleanField
from app.structures import *
from wtforms.validators import DataRequired

class newCampaignForm(FlaskForm):
    campaignName = StringField("Campaign Name", validators=[DataRequired()])
    campaignType = RadioField('Type', choices=campaignTypes(), validators=[DataRequired()])
    comCatPreference = SelectMultipleField(choices=comCatPreferences())
    submit = SubmitField('Submit')

""" 
 Lots of work to do on this form and structure definition. 
 Dictionary of restrictions, to enable 'more than $50 to emergencies' etc,
 so how to express that in the form?   
 (perhaps have sub-element for restriction, and allow type, value, field selection there?)
"""

""" TODO: make fieldAvailable reflect the fields available in dbo.Segmentable """
def fieldsAvailable():
    return [(1,"Emergency Cash in Last Six Months"),(2,"Is Active Regular Giver")]


def conditionsAvailable():
    return [(1,"LESS THAN"),(2,"GREATER THAN")]


class newSegmentForm(FlaskForm):
    segmentName = StringField("Segment Name", validators=[DataRequired()])
    segmentChannel = RadioField('Type', choices=channels(), validators=[DataRequired()])
    allowPool = SelectMultipleField(choices=supporterPools())
    denyPool = SelectMultipleField(choices=supporterPools())
    submit = SubmitField('Submit')


class newConditionForm(FlaskForm):
    conditionName = StringField("Condition Name (optional)")
    conditionField = SelectMultipleField(choices=fieldsAvailable())
    submit = SubmitField('Submit')