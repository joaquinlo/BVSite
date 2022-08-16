from flask import redirect, request, url_for, flash
from application.models.reports_model import Report
from application import db

def new_report():
    title = request.form['title']
    subtitle = request.form['subtitle']
    body = request.form['body']

    new_report = Report(title, subtitle, body)
    db.session.add(new_report)
    db.session.commit()
    flash('Noticia creada satisfactoriamente')
    return redirect(url_for('index'))

def delete_report(report):
    db.session.delete(report)
    db.session.commit()
    flash('Noticia eliminada satisfactoriamente')

def update_report(report):
    new_title = request.form['title']
    new_subtitle = request.form['subtitle']
    new_body = request.form['body']

    report.title = new_title
    report.subtitle = new_subtitle
    report.body = new_body

    db.session.commit()
    return redirect(url_for('index'))