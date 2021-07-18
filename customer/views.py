import requests

from django.http import JsonResponse
from rest_framework.views import APIView

from customer.serializers import AddressSerializer, CustomerSerializer

# Create your views here.
class CustomerView(APIView):

    def post(self, request):

        # get data from another service
        _url = "http://b92f40ed78c0.ngrok.io"
        data_api = requests.get(_url).json()    

        for da in data_api:
            customer = {
                'name' : da['name'],
                'is_company' : da['is_company'],
                'related_company' : da['related_company'],
                'salary': da['penghasilan'],
                'phone' : da['phone'],
                'mobile' : da['mobile']
            }

            address_data = {
                'type' : da['address_type'],
                'street' : da['street'],
                'zip' : da['zip'],
                'city' : da['city'],
                'state' : da['state'],
                'country' : da['country'],
            }

            cstm = CustomerSerializer(data=customer_data)
            if cstm.is_valid(raise_exception=True):
                cstm.save()

                id_customer = cstm.data['id']

                address_data['customer'] = id_customer

                addr = AddressSerializer(data=address_data)
                if addr.is_valid(raise_exception=True):
                    addr.save()
                
                continue
            else:
                return JsonResponse(Status=400, data={"message":"Failed"}, safe=False)

        return JsonResponse(status=200, data={"message":"Success"}, safe=False)    

