from app import app, segment
from flask import render_template, request, session, abort
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
        if request.form.get("campaignName"):
            dt = date.today()
            campaignName=request.form.get("campaignName")
            campaignType=request.form.get("campaignType")
            comCatPreference = request.form.getlist("comCatPreference")
            camp = cmp(campaignname = campaignName,
                       campaigntype = campaignType,
                       comcatpreference = comCatPreference,
                       createdon = dt.__str__() )

            """ Store object properties as json in session: """
            out=json.dumps(camp.__dict__)
            session["Campaign"]=out
            """ Store object properties as json in file """
            with open("segmentalist.json","w") as f:
                f.write(out)
            """ Initialise segment file """
            with open("segmentalist_segs.json","w") as f:
                f.write("\n")

            form=newSegmentForm()
            return                 render_template("segment.html",
                                   form=form,
                                   campaignname=campaignName,
                                   campaigndata=session["Campaign"])
        else:
            """ if submitted segment. """
            """ Load campaign data """
            with open("segmentalist.json") as json_file:
                try:
                    campaigndetail = json.load(json_file)
                except:
                    abort(404, description="Resource not found")

            """ check for other segments """
   #         try:
            with open("segmentalist_segs.json") as json_file:
                segmentdetail = json.load(json_file)
                """
                    newseg=[("segmentName",request.form.get("segmentName")),
                            ("segmentChannel",request.form.get("segmentChannel")),
                            ("allowPool",request.form.get("allowPool")),
                            ("denyPool",request.form.get("denyPool"))]
                    segmentdetail.append(json.loads(newseg))
                """
"""
            except:
                    #not a json file yet. make one.
                if request.form.get("segmentName"):
                    newseg=[("segmentName",request.form.get("segmentName")),
                            ("segmentChannel",request.form.get("segmentChannel")),
                            ("allowPool",request.form.get("allowPool")),
                            ("denyPool",request.form.get("denyPool"))]
                    with open("segmentalist_segs.json","w") as json_file:
                        json_file.write(json.dumps(newseg))
                    segmentdetail=newseg
"""
"""
            if segmentdetail:
                segmentCount=len(segmentdetail)
            else:
                segmentCount=0

            campaignname=campaigndetail["cname"]
            form = newSegmentForm()
            return render_template("segment.html",
                                form=form,
                                segmentcount=segmentCount,
                                campaignname=campaignname,
                                campaigndata=session["Campaign"])

"""