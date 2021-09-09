import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL2')
app.config['SECRET_KEY'] = os.environ.get('SECRET')
db = SQLAlchemy(app)


class Personal_Details(db.Model):
    __tablename__ = 'personal_details'
    p_d_id = db.Column(db.Integer, primary_key=True)
    p_d_type = db.Column(db.String(30))
    p_d_value = db.Column(db.String(100))

    def __init__(self, p_d_type, p_d_value):
        self.p_d_value = p_d_value
        self.p_d_type = p_d_type


class About_Me(db.Model):
    __tablename__ = 'about_me'
    a_m_id = db.Column(db.Integer, primary_key=True)
    a_m_content = db.Column(db.Text)

    def __init__(self, a_m_content):
        self.a_m_content = a_m_content


class Work_Experience(db.Model):
    __tablename__ = 'work_experience'
    w_e_id = db.Column(db.Integer, primary_key=True)
    w_e_title = db.Column(db.String(50))
    w_e_company = db.Column(db.String(50))
    w_e_start = db.Column(db.String(10))
    w_e_end = db.Column(db.String(10))
    w_e_current = db.Column(db.String(10))
    w_e_description = db.Column(db.Text)

    def __init__(self, w_e_title, w_e_company, w_e_start, w_e_end, w_e_current, w_e_description):
        self.w_e_title = w_e_title
        self.w_e_company = w_e_company
        self.w_e_start = w_e_start
        self.w_e_end = w_e_end
        self.w_e_current = w_e_current
        self.w_e_description = w_e_description


class Skill(db.Model):
    __tablename__ = 'skill'
    s_id = db.Column(db.Integer, primary_key=True)
    s_name = db.Column(db.String(50))

    def __init__(self, s_name):
        self.s_name = s_name


class Personal_Project(db.Model):
    __tablename__ = 'personal_project'
    p_p_id = db.Column(db.Integer, primary_key=True)
    p_p_name = db.Column(db.String(50))
    p_p_description = db.Column(db.Text)
    p_p_link = db.Column(db.Text)

    def __init__(self, p_p_name, p_p_description, p_p_link):
        self.p_p_name = p_p_name
        self.p_p_description = p_p_description
        self.p_p_link = p_p_link


@app.route('/get_personal_information')
def get_personal_information():
    get_personal_information = Personal_Details.query.all()
    personal_info = []
    for info in get_personal_information:
        personal_info.append({'id': info.p_d_id, 'type': info.p_d_type, 'value': info.p_d_value})
    return jsonify({'personal_info': personal_info})


@app.route('/get_about_me')
def get_about_me():
    get_about_me = About_Me.query.all()
    about_me = []
    for me in get_about_me:
        about_me.append({'id': me.a_m_id, 'description': me.a_m_content})
    return jsonify({'about_me': about_me})


@app.route('/get_work_experience')
def get_work_experience():
    get_work_experience = Work_Experience.query.all()
    work_experience = []
    for work in get_work_experience:
        work_experience.append({'id': work.w_e_id, 'title': work.w_e_title, 'company': work.w_e_company,
                                'start': work.w_e_start, 'end': work.w_e_end, 'current': work.w_e_current,
                                'description': work.w_e_description})

    return jsonify({'work_experience': work_experience})


@app.route('/get_skill')
def get_skill():
    get_skill = Skill.query.all()
    skill = []
    for s in get_skill:
        skill.append({'id': s.s_id, 'name': s.s_name})

    return jsonify({'skill': skill})


@app.route('/get_personal_project')
def get_personal_project():
    get_personal_project = Personal_Project.query.all()
    personal_project = []
    for project in get_personal_project:
        personal_project.append({'id': project.p_p_id, 'name': project.p_p_name, 'description': project.p_p_description,
                                 'url': project.p_p_link})

    return jsonify({'personal_project': personal_project})


if __name__ == '__main__':
    app.run()
