from django.http import HttpResponse


class stripeWH_handler:
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        return HttpResponse(
            content = f'webhook received: {event["type"]}',
            status=200)
