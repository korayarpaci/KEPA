import os
import json
from django.shortcuts import render

def gold_chart(request):
    # Zaman dilimini al (varsayılan olarak 1 günlük veri)
    time_frame = request.GET.get('time_frame', '1day')

    # JSON dosya dizini
    json_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

    # Zaman dilimi ile JSON dosyası eşleştirmesi
    file_map = {
        '1day': '1daysgold.json',
        '1week': '1weekgold.json',
        '1month': '1monthgold.json',
        '1year': '1yeargold.json',
        '5year': '5yearsgold.json',
        '1day_forecast': 'altin_1_gun_tahmin.json',
        '1week_forecast': 'altin_1_hafta_tahmin.json',
        '1month_forecast': 'altin_1_ay_tahmin.json',

    }

    # Dosya adı ve yolu
    file_name = file_map.get(time_frame, '1daygold.json')
    file_path = os.path.join(json_dir, file_name)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Null veya undefined değerleri filtrele
        chart_data = [
            {"time": item["tarih"], "value": item["fiyat"]}
            for item in data.get("gold_fiyatlari", [])
            if item.get("fiyat") is not None
        ]

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Hata:", e)
        chart_data = []

    # Konsolda kontrol
    print("Frontend'e gönderilen chart_data:", chart_data)

    return render(request, 'gold/gold.html', {
        'chart_data': json.dumps(chart_data),
        'time_frame': time_frame,
    })