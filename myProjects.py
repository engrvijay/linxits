from projects.models import Project

first_project = Project(
     title="CybeSecurity, System Security",
     description="Work include but not limited to Network Access control, Endpoint Compliance, Mobile Control, Instrusion Prevention",
     technology="Linux, Java, Python, Snyk,PostgreSQL, switches, firewall, NetScout, salesforce, Artifactory",
 )
first_project.save()

second_project = Project(
     title="Cloud Transformation, Automation",
     description="Resolve application platform issue, acheve high-availability, scalibility, moduliraty",
     technology="Linux, AWS, Docker, Kubernetes, RDBMS, NGINX, AMQP, TCP/IP JAVA, C, Gitlab, Junkins",
 )
second_project.save()

third_project = Project(
     title="SRE, Data Privacy",
     description="Resolution, Metigation, RCA to improve operational effeciency, Reliability, resolve customer issues",
     technology="Linux, AWS, SQL, Oracle, MySQL, Splunk, Elastic Serch, Gitlab, Junkins, JAVA, CPNI",
 )
third_project.save()

fourth_project = Project(
     title="This Web Project",
     description="Web Development",
     technology="Linux, Python, Django, SqlLite",
 )
fourth_project.save()
cert_project = Project(
     title="Certifications",
     description="Python3, CyberSecurity, AWS, Harvard Managementor (HBR) ®-Leadership Development, Kubernetes (CKA, CKAD)",
     technology="Leadership, Management, Security, Cloud Computing, Processes",
 )
cert_project.save()
