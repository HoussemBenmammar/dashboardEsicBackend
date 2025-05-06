from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ImportedData
import pandas as pd
from django.db.models import Max

@api_view(['GET'])
def get_visual_data(request):
    # Dernier fichier importé
    latest_data = ImportedData.objects.order_by('-uploaded_at').first()

    if not latest_data:
        return Response({'error': 'Aucune donnée disponible'}, status=404)

    df = pd.DataFrame(latest_data.data)

    # Exemple de filtre temporel
    start = request.GET.get('start')
    end = request.GET.get('end')

    if 'date' in df.columns and start and end:
        df['date'] = pd.to_datetime(df['date'])
        df = df[(df['date'] >= start) & (df['date'] <= end)]

    # Exemple de filtre catégoriel
    category = request.GET.get('category')
    if category and 'category' in df.columns:
        df = df[df['category'] == category]

    # Résumé par colonne
    summary = df.describe(include='all').to_dict()

    return Response({
        'columns': list(df.columns),
        'rows': df.to_dict(orient='records'),
        'summary': summary,
    })
