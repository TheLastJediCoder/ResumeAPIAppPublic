# ResumeAPIAppPublic
Application with landing page and admin panel for restaurant to advertise and manage menu and deals.


# Description
Application which respond my resume details in JSON format. 
Python Flask framework was used to build api and PostgreSQL was used to store data.

# API's

- https://harshparecha.herokuapp.com/get_personal_information

- https://harshparecha.herokuapp.com/get_about_me

- https://harshparecha.herokuapp.com/get_skill

- https://harshparecha.herokuapp.com/get_personal_project


# Database Design
- personal_detail Table
  | Field         | Type          | Key           |
  | ------------- | ------------- | ------------- |
  | p_d_id       | Int           | PK            |
  | p_d_type     | Varchar       |               |
  | p_d_value | Varchar       |               |
  
- about_me Table
  | Field              | Type          | Key           |
  | ------------------ | ------------- | ------------- |
  | a_m_id        | Int           | PK            |
  | a_m_content | Text           |      |
  
- work_experience Table
  | Field                | Type          | Key           |
  | -------------------- | ------------- | ------------- |
  | w_e_id           | Int           | PK            |
  | w_e_title         | Varchar           |        |
  | w_e_company   | Varchar           |        |
  | w_e_start       | Varchar       |               |
  | w_e_end       | Varchar       |               |
  | w_e_current       | Varchar       |               |
  | w_e_description       | Text       |               |
  
- skill Table
  | Field              | Type          | Key           |
  | ------------------ | ------------- | ------------- |
  | s_id        | Int           | PK            |
  | s_name | Varchar           |      |

- personal_project Table
  | Field                | Type          | Key           |
  | -------------------- | ------------- | ------------- |
  | p_p_id           | Int           | PK            |
  | p_p_name            | Varchar           |       |
  | p_p_description       | Text       |               |
  | p_p_link            | Text       |               |


# Requirements
- click==8.0.1
- colorama==0.4.4
- Flask==2.0.1
- Flask-SQLAlchemy==2.5.1
- greenlet==1.1.1
- gunicorn==20.1.0
- itsdangerous==2.0.1
- Jinja2==3.0.1
- MarkupSafe==2.0.1
- psycopg2==2.9.1
- SQLAlchemy==1.4.23
- Werkzeug==2.0.1
