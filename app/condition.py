from app import app
from flask import render_template, request, abort, redirect
from app.forms import newSegmentForm, fieldsAvailable, conditionsAvailable, newConditionForm
import json


@app.route("/condition", methods=["GET", "POST"])
def condition():
    form = newConditionForm()
    return render_template("condition.html", form=form)


"""
    with open("segmentalist.json") as json_file:
        try:
            campaigndetail = json.load(json_file)
        except:
            abort(404, description="Resource not found")
    if request.method == "GET":
        form = newSegmentForm()
        return render_template("segment.html", form=form)
    else:
        # receiving post:
        newseg = [("segmentName", request.form.get("segmentName")),
                  ("segmentChannel", request.form.get("segmentChannel")),
                  ("allowPool", request.form.get("allowPool")),
                  ("denyPool", request.form.get("denyPool"))
                  ("restrictions",[])]
        campaigndetail["segments"].append(newseg)
        with open("segmentalist.json", "w") as json_file:
            json_file.write(json.dumps(campaigndetail))
        return redirect("/viewSegments")segment.py
"""