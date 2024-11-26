# Crear un nuevo documento de Word
doc = Document()

# Configuración de estilos
style = doc.styles['Normal']
font = style.font
font.name = 'Arial'
font.size = Pt(11)

# Añadir el nombre y la información de contacto
doc.add_heading('RODDY ALEXI BONILLA DUQUE', level=1)

contact_info = doc.add_paragraph()
contact_info.add_run('Mexico City, Mexico\n').bold = True
contact_info.add_run('Phone: +52 56 3578 2227\n')
contact_info.add_run('Email: roddybonilla@gmail.com | roddy151@gmail.com')

# Añadir Professional Summary
doc.add_heading('PROFESSIONAL SUMMARY', level=1)
summary = (
    "Experienced IT Project Manager with a rich background in managing complex projects in the technology sector, "
    "employing Agile and Kanban principles to drive progress and deliver value. Renowned for exceptional leadership in "
    "coordinating cross-functional teams, negotiating contracts, and optimizing product lifecycles. Expertise in forging "
    "strong client relationships, streamlining processes, and implementing innovative solutions to achieve strategic goals. "
    "Brings a pragmatic approach to problem-solving and a commitment to operational excellence within fast-paced environments."
)
doc.add_paragraph(summary)

# Añadir Professional Experience
doc.add_heading('PROFESSIONAL EXPERIENCE', level=1)

# Job 1
doc.add_heading('Project Manager | EmQu Technologies S.A.', level=2)
job1 = doc.add_paragraph()
job1.add_run('Mexico City, Mexico | January 2022 - Present\n').italic = True
job1.add_run(
    "- Spearheaded IT project management using Agile methodologies, including Scrum and Kanban.\n"
    "- Fostered collaboration with technical teams and stakeholders to devise innovative and impactful solutions."
)

# Job 2
doc.add_heading('Sales and Contract Manager | Faraday SAICyF', level=2)
job2 = doc.add_paragraph()
job2.add_run('Buenos Aires, Argentina | September 2019 - December 2021\n').italic = True
job2.add_run(
    "- Managed technical bids, coordinated requests and documentation involved in bidding processes, and estimated associated costs.\n"
    "- Ensured successful execution of projects for key clients through planning, execution, monitoring, and control.\n"
    "- Acted as a bridge between clients and the technical team to ensure clear and effective communication throughout all project phases."
)

# Job 3
doc.add_heading('Sales Engineer | Schoss S.A.', level=2)
job3 = doc.add_paragraph()
job3.add_run('Buenos Aires, Argentina | November 2018 - August 2019\n').italic = True
job3.add_run(
    "- Provided technical and commercial support to clients, building strong and trustworthy relationships to develop new business opportunities.\n"
    "- Created technical-commercial offers for products, solutions, and services, managing and closing sales by tracking commercial opportunities."
)

# Job 4
doc.add_heading('After Sales Engineer | Ponis S.A.', level=2)
job4 = doc.add_paragraph()
job4.add_run('Buenos Aires, Argentina | December 2017 - November 2018\n').italic = True
job4.add_run(
    "- Commissioned products and provided technical advice to customers on the operation and use of products.\n"
    "- Analyzed situations to make technical and commercial decisions to solve problems effectively."
)

# Job 5
doc.add_heading('CEO | Grupo Carboni C.A.', level=2)
job5 = doc.add_paragraph()
job5.add_run('Táchira, Venezuela | May 2013 - December 2017\n').italic = True
job5.add_run(
    "- Developed plans and strategies to achieve sales goals and objectives, designed management indicators to measure performance, and ensured the sales team was properly trained and motivated.\n"
    "- Controlled available inventory to optimize performance, successfully expanded into new regional markets, and ensured rapid acceptance in these markets."
)

# Job 6
doc.add_heading('Technical Sales Advisor in the Andes Region | Industria Filtros y Laboratorios C.A.', level=2)
job6 = doc.add_paragraph()
job6.add_run('Venezuela | June 2010 - April 2013\n').italic = True
job6.add_run(
    "- Planned, projected, and budgeted sales by department, supervised, advised, and trained the sales force of different distributors.\n"
    "- Implemented a comprehensive action plan to resolve widespread customer dissatisfaction due to technical failures, regained customer trust, and significantly increased sales."
)

# Job 7
doc.add_heading('Electronic Engineer | SIDETUR (Siderúrgica del Túrbio S.A.)', level=2)
job7 = doc.add_paragraph()
job7.add_run('Barquisimeto, Venezuela | February 2008 - May 2010\n').italic = True
job7.add_run(
    "- Performed preventive and corrective maintenance in the control area, troubleshooted technical issues, and provided technical support to staff.\n"
    "- Conducted research to improve maintenance procedures, developed projects, programmed PLCs using STEP 7 (PLC Simatic-7), and created HMI applications using Simatic HMI."
)

# Añadir Education
doc.add_heading('EDUCATION', level=1)
education = (
    "Electronic Engineer\n"
    "Universidad Nacional Experimental del Táchira (UNET), Táchira, Venezuela | 2002-2008\n"
    "Postgraduate in Project Management\n"
    "Universidad Tecnológica Nacional (UTN), Buenos Aires, Argentina | January-May 2019\n"
    "Master in Industrial Automation and Robotics\n"
    "Esneca Business School, Madrid, Spain | July 2019 - July 2020\n"
    "Diploma in Business Management and Administration\n"
    "School of Economics and Business - Universidad Nacional de San Martín (Ministerio de Desarrollo Productivo de Argentina) | June-November 2021"
)
doc.add_paragraph(education)

# Añadir Skills
doc.add_heading('SKILLS', level=1)
skills = (
    "- Project Management\n"
    "- Agile Methodologies (Scrum, Kanban)\n"
    "- Client Relationship Management (CRM)\n"
    "- B2B and B2C Sales\n"
    "- Technical Support and Maintenance\n"
    "- Leadership and Team Coordination\n"
    "- Data Analysis and Database Management\n"
    "- Communication and Public Speaking"
)
doc.add_paragraph(skills)

# Añadir Training and Certifications
doc.add_heading('TRAINING AND CERTIFICATIONS', level=1)
training = (
    "- Platzi: Cloud Computing Introduction (December 2023), Agile Team Management Course (July 2023), Logical Thinking: Algorithms and Flowcharts (July 2023), Scrum Master Course (July 2023), Software Engineering Fundamentals (December 2022)\n"
    "- Fortinet: NSE 2 Network Security Associate (September 2022 - 2024)\n"
    "- CertiProf: Scrum Foundation Professional Certificate - SFPC™ (October 2022)\n"
    "- Instituto Tecnológico de Monterey / Coursera: Risk Management and Project Change Management, Project Scheduling and Budgeting, Project Initiation & Planning\n"
    "- University of California, Irvine UCI / Coursera: Finance for Non-Financial Professionals\n"
    "- LinkedIn Learning: Power BI for Beginners, Learn SCRUM (July 2020)\n"
    "- Schneider Electric: Active Energy Efficiency using Speed Control, Efficient Engine Control with Power Transmission and Control Systems (March - April 2020)\n"
    "- AIERA: Specialization in Foreign Trade Management (March 2020)\n"
    "- Kuka Argentina: Robotics RP1 (June 2019)"
)
doc.add_paragraph(training)

# Añadir Languages
doc.add_heading('LANGUAGES', level=1)
languages = (
    "- Spanish: Native\n"
    "- English: Basic"
)
doc.add_paragraph(languages)

# Guardar el documento
file_path = "/mnt/data/Roddy_Bonilla_CV_2024_English_Final.docx"
doc.save(file_path)

file_path
