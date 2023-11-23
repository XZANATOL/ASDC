from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import QueryDict
from . import forms
from . import models

import pandas as pd

@csrf_exempt
def upload(request):
	if request.method == "POST":
		res = []
		data = request.FILES
		for filename, file in request.FILES.items():
			data = file
			break
		data = pd.read_excel(data)
		data.dropna(inplace=True)

		for index, row in data.iterrows():
			data_parsed = {
				"name": row.get(" Name"),
				"description": row.get(" Description "),
				"location":  row.get("Location "),
				"price":  row.get("Price"),
				"color":  row.get("Color")
			}

			form = forms.RecordForm(data_parsed)
			if form.is_valid():
				form = form.save()
				data_parsed["id"] = form.pk
				res.append(data_parsed)

		return JsonResponse(res, safe=False)
	else:
		return JsonResponse({"error": "Invalid Method"}, safe=False, status=405)


@csrf_exempt
def read(request, key):
	if request.method == "GET":
		try:
			record = models.Record.objects.get(pk=key)
			record = {
				"name": record.name,
				"description": record.description,
				"location":  record.location,
				"price": record.price,
				"color": record.color
			}
			return JsonResponse(record, safe=False)
		except models.Record.DoesNotExist:
			return JsonResponse({"error": "Not Found"}, safe=False, status=404)
	else:
		return JsonResponse({"error": "Invalid Method"}, safe=False, status=405)


@csrf_exempt
def update(request, key):
	if request.method == "PUT":
		try:
			record = models.Record.objects.get(pk=key)
			data = QueryDict(request.body).dict()
			data["description"] = record.description
			data["location"] = record.location
			data["price"] = record.price
			data["color"] = record.color
			record = forms.RecordForm(data, instance=record)

			if record.is_valid():
				record.save()
				return JsonResponse(data, safe=False)
			else:
				return JsonResponse({"error": "Invalid request"}, safe=False, status=400)
		except models.Record.DoesNotExist:
			return JsonResponse({"error": "Not Found"}, safe=False, status=404)
	else:
		return JsonResponse({"error": "Invalid Method"}, safe=False, status=405)


@csrf_exempt
def delete(request, key):
	if request.method == "DELETE":
		try:
			record = models.Record.objects.get(pk=key)
			data = {
				"name": record.name,
				"description": record.description,
				"location":  record.location,
				"price": record.price,
				"color": record.color
			}
			record.delete()
			return JsonResponse(data, safe=False)
		except models.Record.DoesNotExist:
			return JsonResponse({"error": "Not Found"}, safe=False, status=404)
	else:
		return JsonResponse({"error": "Invalid Method"}, safe=False, status=405)