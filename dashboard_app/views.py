from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json 
from .models import Book
# from .model.evaluate import Evaluator
from .journalGPT import master 
import csv 


class Evaluator:
    
    def __init__(self):
        pass 
    
    def gather_results(self, sentence, words):
        return sentence
        pass 


# Evaluates the results from the model 
def handle_model_results(request):
    if request.method == 'POST':
        # Get the sentence and words from the request body
        print(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        sentence = body['sentence']
        words = body['words']

        # Perform the calculation using the model
        evaluator = Evaluator()
        try:
            result = evaluator.gather_results(sentence, words)
            print("Get result successful", result)
            print(result)
        except Exception as e: 
            return JsonResponse({'error': f"Invalid data received: {e}"}, status=400)

        # Return the result as a JSON response
        return JsonResponse({'result': result}, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# Evaluates the result of uploading a file 
def upload_file(request):
    if request.method == 'POST':
        print(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        filepath = body['filepath']
        # Handle the uploaded file
        # Save the file to the server
        # Return a JSON response with information about the uploaded file
        try:
            result = master.main(filepath, 'test.pptx')
            return JsonResponse({'result': filepath}, status=200)
        except Exception as e:
             return JsonResponse({'error': f"Invalid data received: {e}"}, status=400)
        # return JsonResponse({'result': filepath}, status=200)
    return JsonResponse({'error': "Invalid request method"}, status=400)


        
# Index request html 
def index(request):
    books = Book.objects.all()
    return render(request, 'dashboard_app/index.html')
