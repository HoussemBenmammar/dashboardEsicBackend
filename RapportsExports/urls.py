from .views import generate_pdf, export_csv, export_excel, export_plot

urlpatterns += [
    path('export/pdf/', generate_pdf),
    path('export/csv/', export_csv),
    path('export/excel/', export_excel),
    path('export/plot/', export_plot),
]
