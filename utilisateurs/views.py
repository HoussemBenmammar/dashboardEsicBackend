from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import generics

# 🎟 Login - retourne access + refresh + role
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# 👤 Register
@api_view(['POST'])
def register_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'username': user.username}, status=201)
    return Response(serializer.errors, status=400)


# 🔐 Admin only route
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_only(request):
    if request.user.role != 'admin':
        return Response({"error": "Accès refusé"}, status=403)
    return Response({"message": f"Bienvenue admin {request.user.username}"})


# 🔄 Récupérer tous les utilisateurs (admin seulement)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    if request.user.role != 'admin':
        return Response({"error": "Accès refusé"}, status=403)
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# ✏️ Modifier un utilisateur (admin uniquement)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    if request.user.role != 'admin':
        return Response({"error": "Accès refusé"}, status=403)
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "Utilisateur non trouvé"}, status=404)

    serializer = UserRegisterSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


# 🗑 Supprimer un utilisateur (admin uniquement)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    if request.user.role != 'admin':
        return Response({"error": "Accès refusé"}, status=403)
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"message": "Utilisateur supprimé"}, status=204)
    except User.DoesNotExist:
        return Response({"error": "Utilisateur non trouvé"}, status=404)
