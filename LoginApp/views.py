import dlib
import numpy as np
import face_recognition as fr
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import get_user_model, login

User = get_user_model()

# Create your views here.

def home_view(request):
    context = {
        'title': 'Home',
    }

    return render(request, 'LoginApp/home.html', context=context)


@csrf_exempt
def register_face(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        username = request.POST['username']

        img = fr.load_image_file(image_file)
        encodings = fr.face_encodings(img)

        if len(encodings) == 0:
            return JsonResponse({'error':'No face found'})
        
        encoding = encodings[0]
        user = User.objects.get(username=username)
        user.face_encoding = encoding.tobytes()
        user.save()

        return JsonResponse({'status':'status'})
    

@csrf_exempt
def login_face(request):
    if request.method == 'POST':
        image_file = request.FILES['image']

        img = fr.load_image_file(image_file)
        encodings = fr.face_encodings(img)

        if len(encodings) == 0:
            return JsonResponse({'error': 'No face detected.'})

        uploaded_encoding = encodings[0]

        for user in User.objects.exclude(face_encoding__isnull=True):
            known_encoding = np.frombuffer(user.face_encoding, dtype=np.float64)
            matches = fr.compare_faces([known_encoding], uploaded_encoding, tolerance=0.5)
            if matches[0]:
                login(request, user)
                return JsonResponse({'status': 'success', 'username': user.username})

        return JsonResponse({'status': 'failed'})