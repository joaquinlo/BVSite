from application import app
from flask import request, render_template, redirect, url_for
from application.models.reports_model import Report
from application.controllers import reports_controller

@app.route('/index')
def index():
    reports = Report.query.all()
    return render_template('reports/index.html', title_tag = 'Noticias', reports = reports)

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        reports_controller.new_report()
    return render_template('reports/new.html', title_tag = 'Nuevo reporte')

@app.route('/delete/<id>')
def delete(id):
    report = Report.query.get(id)
    reports_controller.delete_report(report)
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    report = Report.query.get(id)
    if request.method == 'POST':
        reports_controller.update_report(report)
    return render_template('reports/update.html', title_tag = 'Editar reporte', report = report)