import django
import os
import sys
import time
import json
import requests
from inventory.api.inventory_rest.models import Automobile



sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()


from sales_rest.models import AutomobileVO
# Import models from sales_rest, here.
# from sales_rest.models import Something

def get_automobiles():
    response = requests.get('http://inventory-api:8000/api/automobiles/')
    content = json.loads(response.content)
    for car in content["automobiles"]:
        try:
            AutomobileVO.objects.update_or_create(
                import_href= Automobile['href']
                defaults={
                    "vin": automobile["vin"],
                }
            )
        except Exception as e:
            print(e, file=sys.stderr)


def poll():
    while True:
        print('Sales poller polling for data')
        try:
            # Write your polling logic, here
            pass
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
