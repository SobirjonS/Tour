from main import models
from rest_framework.response import Response

def get_fields(request):
    user = request.user
    data = request.data

    allowed_fields = ['first_name', 'last_name', 'email', 'phone_number', 'is_admin', 'is_partner', 'avatar']
    updated_fields = {}
    
    for field in allowed_fields:
        if field in data:
            if field == 'email' and models.CustomUser.objects.filter(email=data[field]).exclude(pk=user.pk).exists():
                return Response({'error': 'Email already exists'}, status=400)
            updated_fields[field] = data[field]

    for field, value in updated_fields.items():
        setattr(user, field, value)
    
    user.save()

    return Response({'success': 'Data user updated successfully'})