from rest_framework import serializers
from django.db import models

from .models import Sex, Pet
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

from groups.models import Group
from traits.models import Trait

from ipdb import set_trace as st


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(default=Sex.DEFAULT, choices=Sex.choices)
    group = GroupSerializer()
    traits_count = serializers.SerializerMethodField()
    traits = TraitSerializer(many=True)

    def get_traits_count(self, instance: Pet) -> int:
        return instance.traits.count()

    def create(self, validated_data: dict) -> Pet:
        group_dict = validated_data.pop("group")
        trait_dict = validated_data.pop("traits")

        group, _ = Group.objects.get_or_create(**group_dict)
        pet = Pet.objects.create(**validated_data, group=group)

        for trait in trait_dict:
            new_trait, _ = Trait.objects.get_or_create(**trait)
            pet.traits.add(new_trait)

        return pet

    def update(self, instance: Pet, validated_data: dict) -> Pet:
        group_dict: dict = validated_data.pop("group", None)
        traits_dict: list[dict] = validated_data.pop("traits", None)

        if group_dict:
            group, _ = Group.objects.get_or_create(**group_dict)
            for key, value in group_dict.items():
                setattr(group, key, value)
            group.save()

        if traits_dict:
            instance.traits.clear()
            for trait in traits_dict:
                new_trait, _ = Trait.objects.get_or_create(**trait)
                instance.traits.add(new_trait)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.group = group
        instance.save()

        return instance
