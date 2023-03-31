
![](./pictures/databand1.png)

# IBM Databand hands-on Workshop

Welcome to our hands-on workshop where you will learn to deploy [databand](https://databand.ai/) on an [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) cluster. Additionally, we will explore the integration capabilities with [Apache Airflow](https://airflow.apache.org/), [PostgreSQL](https://www.postgresql.org/), [python](https://www.python.org/) and [IBM Datastage](https://www.ibm.com/products/datastage).

Note that there is a full documented set of instructions for [deploying databand](https://docs.databand.ai/docs/installing-databand-in-kubernetes-cluster) on a Kubernetes / OpenShift production environment. For educational purposes, some shortcuts have been made during this workshop.

## Contents

### Video Playlist (in German)

I recorded a quick guide of each chapter in this [YouTube playlist](https://youtube.com/playlist?list=PLa8RtivAledWdZsEzl34UUY_Eephzj7pZ)

### Part 1: Deployment and Setup

| Chapter   | Content                                                   | Video (in German)                           |
| :--------:|-----------------------------------------------------------|---------------------------------------------|
| 0         | [Prerequisites](./jupyter/0_prerequisites.ipynb)          |[Abschnitt 0](https://youtu.be/qXYpGCiDJnQ)  |
| 1         | [Hardware provisioning](./jupyter/1_provisioning.ipynb)   |[Abschnitt 1](https://youtu.be/pyn_ZG-_NW8)  |
| 2         | [Databand deployment](./jupyter/2_databand_deploy.ipynb)  |[Abschnitt 2](https://youtu.be/I7wjO_Ucqx0)  |
| 3         | [Airflow deployment](./jupyter/3_airflow_deploy.ipynb)    |[Abschnitt 3](https://youtu.be/4n49O8ZCrno)  |
| 4         | [Airflow integration](./jupyter/4_airflow_int.ipynb)      |[Abschnitt 4](https://youtu.be/RSnTgBpFd24)  |
| 5         | [DataStage integration](./jupyter/5_datastage_int.ipynb)  |[Abschnitt 5](https://youtu.be/8OZt0w2OGTY)  |
| 6         | [Postgres deployment](./jupyter/6_postgres_deploy.ipynb)  |[Abschnitt 6](https://youtu.be/4Ki8IQpGR8U)  |

### Part 2: Development and Observability

### Video Playlist (in German)

I recorded a quick guide of each chapter in this [YouTube playlist](https://www.youtube.com/playlist?list=PLa8RtivAledVTxwkLOk_W2XTt0CDaQfrm)

| Chapter   | Content                                                            | Video (in German)                            |
| :--------:|--------------------------------------------------------------------|----------------------------------------------|
| 7         | [Preparation](./jupyter/7_dags_dev.ipynb)                          |[Abschnitt 7](https://youtu.be/AGPCNkdLiys)   |
| 8         | [SQL Airflow pipelines](./jupyter/8_SQL_dag_dev.ipynb)             |[Abschnitt 8](https://youtu.be/Y7EJnEo_v_A)   |
| 9         | [Python pipelines](./jupyter/9_python_dag_dev.ipynb)               |[Abschnitt 9](https://youtu.be/TEOkEjKSOtU)   |
| 10        | [Python on Airflow pipelines](./jupyter/10_py_air_dag_dev.ipynb)   |[Abschnitt 10](https://youtu.be/1XIoYTvCRPM)  |
| 11        | [DataStage pipelines](./jupyter/11_datastage_dev.ipynb)            |[Abschnitt 11](https://youtu.be/zqsWfLfJ9xI)  |
| 12        | [Alerts and exceptions](./jupyter/12_alerts_dev.ipynb)             |[Abschnitt 12](https://youtu.be/1zCYC_69qXs)  |
| 13        | [Customized user metrics](./jupyter/13_quantum_dev.ipynb) <br/> example: **Quantum Computing**    |[Abschnitt 13](https://youtu.be/Lhq7VajnlRI)  |

### How and why was this workshop developed?

All contents were developed and tested on a MacBook using Microsoft Visual Studio Code with popular extensions for Markdown, Jupyter, Python and bash. Future enhancements will include Windows and Linux to adapt the commands when necessary.

The intention of this workshop was to provide IBMers and its business parterns with a single set of intructions for self-education that can be updated and enhanced by other collaborators using the functions of git repositories. A secondary goal was to minimize or even reduce to zero the ammount of keystrokes necessary to deliver this workshop to a wider audience, either remotely or face to face.

It would be appreciated if the typos, suggestions, improvements, etc. would be reported by opening issues on the git repository. Alternatively, you can send your feedback directly to angelito@de.ibm.com.

### Disclaimer

The contents of this workshop have been fully tested and verified but the normal evolution of the many software pieces (most of them open source) will cause disruptions at some point in time. Please apologyze for the inconveniences if that ocurrs. Just open an issue in this repository to let us know. Anyway, we are looking forward to receive your feedback and perhaps your willingness to collaborate and improve this effort.

### Acknowledgements

Thanks to Matt Koscak, Adrian Houselander and Elena Lowery for having written the documentation I adapted and used as the starting point to compile this workshop.

### Repository mirrors

If you notice formatting failures while displaying the webpages, it may be caused by the differences in the rendering engines hosting the git repositories. Just clone the repository on your local machine and display it with Jupyter. Alternatively, you may try one of these mirrors:

- GitLab: https://gitlab.com/angel-ibm/deployment-databand
- GitHub: https://github.com/angel-ibm/deployment-databand
- Enterprise github (IBM internal): https://github.ibm.com/angelito/databand-workshop

If you need a written documentation, all the contents are also available in PDF and Word format:
- [Documentation](https://gitlab.com/angel-ibm/deployment-databand/-/tree/main/docs) in gitlab
- [Documentation](https://github.com/angel-ibm/deployment-databand/tree/main/docs) in github
