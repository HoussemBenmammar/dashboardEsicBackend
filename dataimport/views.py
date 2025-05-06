import pandas as pd
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import ImportedData

@api_view(['POST'])
@parser_classes([MultiPartParser])
def upload_file(request):
    file = request.FILES.get('file')

    if not file:
        return Response({'error': 'Aucun fichier fourni.'}, status=400)

    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return Response({'error': 'Format non supporté'}, status=400)

        # Nettoyage de base
        df = df.dropna(how='all')
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
        preview = df.head(10).to_dict(orient='records')

        # Sauvegarde en base (optionnel)
        ImportedData.objects.create(data=preview)

        return Response({
            'message': 'Fichier importé avec succès.',
            'columns': list(df.columns),
            'preview': preview
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)
