from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from member.serializers import MemberSerializer
from member.models import Member

# Create your views here.
class MemberView(APIView):

    def post(self, request):
        # get body request from client
        data_request = JSONParser().parse(request)


        #insert into database
        member = MemberSerializer(data=data_request)
        if member.is_valid(raise_exception=True):
            member.save()

    

            return JsonResponse(member.data, status=200)

        return JsonResponse(status=400, messages="Failed", safe=False)

    def get(self, request):

        member = Member.objects.all() # select * from member

        data_member = MemberSerializer(member, many=True)

        return JsonResponse(data_member.data, status=200, safe=False)
    
    # def put(self, requesr, id=None):





        # def get(self, request):
         
    #     data = {
    #         "name": "Pandu",
    #         "gender": "male"
    #     }
        # success : 200
        # insert : 200
        # success : 200