from app import app
# from cache import cache
from flask import request, render_template, redirect
from app.model.CoursesModel import Courses


@app.route("/courses", methods=["GET"])
# @cache.cached(timeout=50)
def getCourses():
    courses = Courses.getAll()
    return render_template("courses.html", data=enumerate(courses, 1))


@app.route("/courses", methods=["POST"])
# @cache.cached(timeout=50)
def createCourses():
    name = request.form["name"]
    sks = int(request.form["sks"])
    semester = int(request.form["semester"])
    courses = Courses(name=name, sks=sks, semester=semester)
    courses.save()
    return redirect("/courses")


@app.route("/courses/<int:id>/edit", methods=["GET"])
# @cache.cached(timeout=50)
def updateCoursesForm(id):
    courses = Courses.getById(id)
    return render_template("courses_update.html", data=courses)


@app.route("/courses/<int:id>/edit", methods={"POST"})
# @cache.cached(timeout=50)
def updateCourses(id):
    courses = Courses.findById(id)

    name = request.form["name"]
    sks = int(request.form["sks"])
    semester = int(request.form["semester"])

    courses.name = name
    courses.sks = sks
    courses.semester = semester
    courses.save()
    return redirect("/courses")


@app.route("/courses/<int:id>/delete", methods=["GET"])
# @cache.cached(timeout=50)
def deleteCourse(id):
    courses = Courses.findById(id)
    courses.delete()
    return redirect("/courses")
