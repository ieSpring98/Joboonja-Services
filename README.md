## Joboonja Service

This project is the web service for Internet Engineering course for spring 2019 for University of Tehran.

To run the project creation job in crontab, open the crontab:
```
crontab -e
```
And add the command:
```
*/5 * * * * cd ROOT_PROJECT; source venv/bin/activate; python manage.py add_project > data/add_project.out 2>&1
```
In which the variable ``ROOT_PROJECT`` is your the project root address.