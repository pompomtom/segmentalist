from app import app
from flask import render_template, request, abort, redirect
from app.forms import newSegmentForm
from app.structures import d_channels
import json
import sys


def listSegments():
    with open("segmentalist.json") as json_file:
            campaigndetail = json.load(json_file)
    segments = campaigndetail["segments"]
    return segments


def segNames():
    with open("segmentalist.json") as json_file:
        campaigndetail = json.load(json_file)
    segments = campaigndetail["segments"]
    print(segments, file=sys.stderr)
    segnames = []
    i=1
    for seg in segments:
        ch = int(seg[1][1])
        chnames = d_channels()
        chname = chnames(ch)
        segnames.append((i,seg[0][1],chname,seg[2][1],seg[3][1]))
        i+=1
    return segnames


def segDict():
    with open("segmentalist.json") as json_file:
        campaigndetail = json.load(json_file)
    segments = campaigndetail["segments"]
    out={}
    for segment in segments:
        label=segment[0][0]
        value=segment[0][1]
        out[label]=value
    return out


@app.route("/segment", methods=["GET", "POST"])
def segment():
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
                  ("denyPool", request.form.get("denyPool")),
                  ("restrictions",[])]
        campaigndetail["segments"].append(newseg)
        with open("segmentalist.json", "w") as json_file:
            json_file.write(json.dumps(campaigndetail))
        #return redirect("/viewSegments")
        return redirect("/segment")

@app.route("/viewSegments", methods=["GET", "POST"])
def viewSegments():
    with open("segmentalist.json") as json_file:
        try:
            campaigndetail = json.load(json_file)
        except:
            abort(404, description="Resource not found")
    if campaigndetail:
        segments = campaigndetail["segments"]
        out = {}
        for segment in segments:
            label = segment[0][0]
            value = segment[0][1]
            out[label] = value
    #return "Display segment details, include link to add new segment (redirect to /segment)"
    return out


@app.route("/testing")
def testing():
    return render_template("test.html")


