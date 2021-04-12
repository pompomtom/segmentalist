import json

class campaign:
    def __init__(self,campaignname,campaigntype,comcatpreference,createdon):
        self.cname = campaignname
        self.ctype = campaigntype
        self.comCat = comcatpreference
        self.createdOn = createdon
        self.segments = []
        #self.savedata = json.loads(dict([('campaignname',campaignname),('campaigntype',campaigntype)]))
                                            #,('comcatpreference',comcatpreference)]))


""" 
    To implement with runq (or just find a guid library...)
    self.guid = runq("SELECT NEWID()")
"""

def supporterPools():
    return [(1, 'Advocacy'), (2, 'Bequest'), (3, 'Community Fundraising'), (4, 'Corporate Partner'),
            (5, 'Donor'), (6, 'Key Supporter'), (7, 'Major Donor'), (8, 'Member'), (9, 'Retail'),
            (10, 'Trust / Foundation'), (11, 'Volunteering'), (12, 'Workplace Giving')]

def d_supporterPools():
    return {(1, 'Advocacy'), (2, 'Bequest'), (3, 'Community Fundraising'), (4, 'Corporate Partner'),
            (5, 'Donor'), (6, 'Key Supporter'), (7, 'Major Donor'), (8, 'Member'), (9, 'Retail'),
            (10, 'Trust / Foundation'), (11, 'Volunteering'), (12, 'Workplace Giving')}

def campaignTypes():
    return [(1, 'Appeal'), (2, 'Marketing'), (3, 'Update')]

def channels():
    return [(1, 'Direct Mail'), (2, 'Email'), (3, 'Phone'), (4, 'SMS')]


def d_channels():
    return {(1, 'Direct Mail'), (2, 'Email'), (3, 'Phone'), (4, 'SMS')}



def comCatPreferences():
    return [
        (1, "Advocacy Comms"),
        (2, "All Other Appeals"),
        (3, "Annual Report"),
        (4, "Autumn Appeal"),
        (5, "Bequest Information"),
        (6, "CEO Update"),
        (7, "Christmas Appeal"),
        (8, "Emergency Appeals"),
        (9, "EOY Calendar"),
        (10, "EOY Thank You Card"),
        (11, "Events"),
        (12, "Membership eNewsletter"),
        (13, "Merchandise Catalogue"),
        (14, "Premium Pack"),
        (15, "Quarterly Update"),
        (16, "Regular Giving Tax Receipt"),
        (17, "Reminder Appeal"),
        (18, "RG Tax Receipt"),
        (19, "Soft Asks"),
        (20, "Spring Appeal"),
        (21, "Stories from the Field"),
        (22, "Surveys"),
        (23, "Tax Appeal"),
        (24, "World's Children")]


def supporterProfileCodes():
    return \
        [(1, "3rd Party Fundraiser"),
         (2, "3rd Party Fundraising Donor"),
         (3, "Advocacy Supporter"),
         (4, "Art Union Ticket Purchaser"),
         (5, "Bequest"),
         (6, "Born to Knit Supporter"),
         (7, "CEO VIP"),
         (8, "Charity Challenge"),
         (9, "Charity Challenge Prospect"),
         (10, "Community Referrals"),
         (11, "Corporate"),
         (12, "Cubbies Supporter"),
         (13, "eCommerce"),
         (14, "Endowment Fund"),
         (15, "Estate"),
         (16, "Event Invitees"),
         (17, "EX-SCA Board Member"),
         (18, "Friends of Eglantyne Jebb Society"),
         (19, "Hands on Learning"),
         (20, "Impact Investment"),
         (21, "Impact Investment Fund - Investment Committee Member"),
         (22, "Impact Investment Fund Board"),
         (23, "Key Supporter"),
         (24, "Library for All"),
         (25, "Major Donor"),
         (26, "Major Donor Prospect"),
         (27, "Member"),
         (28, "Middle Donors"),
         (29, "Retail"),
         (30, "SCA Board Member"),
         (31, "Staff Member"),
         (32, "Supporter Opinions Panel"),
         (33, "Top Supporter"),
         (34, "Trust / Foundation"),
         (35, "VIP"),
         (36, "Volunteer"),
         (37, "Workplace Giving Donor"),
         (38, "Workplace Giving Employer")
         ]

