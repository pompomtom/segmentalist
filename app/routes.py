from app import app, segment, condition
from flask import render_template, request, session, abort, redirect
from app.forms import newCampaignForm, newSegmentForm
from app.structures import campaign as cmp
import json
from datetime import date


@app.route("/", methods=["GET"])
def root():
    items = ('test', 'test')
    progress = 55
    progresslabel = "Progress label"
    return render_template("base.html", len=len(items), content=items,  progress=progress, progresslabel=progresslabel)

@app.route("/campaign", methods=["GET","POST"])
def campaign():

    if request.method == "GET":
        form = newCampaignForm()
        return render_template("campaign.html",form=form)

    if request.method == "POST":
        """ if submitted campaign """
        dt = date.today()
        campaignName=request.form.get("campaignName")
        campaignType=request.form.get("campaignType")
        comCatPreference = request.form.getlist("comCatPreference")
        camp = cmp(campaignname = campaignName,
                       campaigntype = campaignType,
                       comcatpreference = comCatPreference,
                       createdon = dt.__str__()
                    )

        """ Store object properties as json in session: """
        out=json.dumps(camp.__dict__)
        with open("segmentalist.json","w") as f:
            f.write(out)
        # Load segment page
        return redirect("/segment")