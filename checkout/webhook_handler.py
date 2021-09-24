from django.http import HttpResponse


class stripeWH_handler:
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        return HttpResponse(
            content = f'webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content = f'webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content = f'webhook received: {event["type"]}',
            status=200)
