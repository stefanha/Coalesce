from rest_framework import serializers
from .models import Opportunity

class OpportunitySerializer(serializers.ModelSerializer):
    skills_required = serializers.ListField()

    class Meta:
        model = Opportunity
        fields = ('id',
                  'datetime',
                  'title',
                  'description',
                  # TODO 'organizer',
                  'location',
                  'personnel_needed',
                  'skills_required',
                  'commitment_type',
                  'background_check_requirements',
                  # TODO 'image',
                  'clothing_requirements',
                  'post_privacy',
                  # TODO 'training_requirements'
                  )
