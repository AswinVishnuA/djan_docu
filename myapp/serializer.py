from rest_framework import serializers
from .models import couplemodel

class couplemodelSerializer(serializers.ModelSerializer):
    class meta:
        model= couplemodel
        fields=('id','Bfname','Gfname','ProbofMarr')
            

