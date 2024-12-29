from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # E-posta Gönderimi
            try:
                send_mail(
                    subject=f"Yeni İletişim Mesajı: {name}",
                    message=f"Gönderen: {name} ({email})\n\nMesaj:\n{message}",
                    from_email='your-email@gmail.com',  # Gönderen e-posta
                    recipient_list=['admin@kepa.com'],  # Alıcı e-posta
                    fail_silently=False,
                )
                success = True
            except Exception as e:
                print(f"E-posta gönderim hatası: {e}")

            # Formu sıfırla
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form, 'success': success})