from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import pandas as pd
from .models import ImportedData

def generate_pdf(request):
    latest = ImportedData.objects.last()
    if not latest:
        return Response({"error": "Pas de données"}, status=404)

    df = pd.DataFrame(latest.data)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    p.drawString(100, height - 50, "Rapport d'analyse de données")

    stats = df.describe().round(2)

    y = height - 100
    for col in stats.columns:
        p.drawString(50, y, f"{col}: Moyenne = {stats[col]['mean']}, Médiane = {df[col].median()}, Écart-type = {stats[col]['std']}")
        y -= 20

    p.showPage()
    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="rapport.pdf")

from django.http import HttpResponse

def export_csv(request):
    latest = ImportedData.objects.last()
    if not latest:
        return Response({"error": "Pas de données"}, status=404)

    df = pd.DataFrame(latest.data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'
    df.to_csv(path_or_buf=response, index=False)
    return response


from django.http import HttpResponse

def export_csv(request):
    latest = ImportedData.objects.last()
    if not latest:
        return Response({"error": "Pas de données"}, status=404)

    df = pd.DataFrame(latest.data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data.csv'
    df.to_csv(path_or_buf=response, index=False)
    return response
