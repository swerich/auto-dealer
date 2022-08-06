import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_project.settings")
django.setup()

from service_rest.models import AutomobileVO
# Import models from service_rest, here.
# from service_rest.models import Something
def get_automobiles():
    response = requests.get("http://inventory-api:8000/api/automobiles/")
    content = json.loads(response.content)
    for automobile in content["automobiles"]:
        try:
            AutomobileVO.objects.update_or_create(
                import_href=automobile["href"],
                defaults={
                    "color": automobile["color"],
                    "year": automobile["year"],
                    "vin": automobile["vin"],
                }
            )
        except Exception as e:
            print("Error", e, file=sys.stderr)
        print("SUCCESS", automobile)

def poll():
    while True:
        print('Service poller polling for data')
        try:
            get_automobiles()
            # Write your polling logic, here
            
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(15)


if __name__ == "__main__":
    poll()
