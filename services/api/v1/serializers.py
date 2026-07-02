from rest_framework import serializers
from ...models import Services, Category




class ServicesSerializers(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    speacials = serializers.SerializerMethodField()

    def get_category(self, obj):
        return [cat.name for cat in obj.category.all()]

    def get_tags(self, obj):
        return [tg.title for tg in obj.tags.all()]

    def get_speacials(self, obj):
        return [sp.text for sp in obj.speacials.all()]
    
    class Meta:
        model = Services
        fields = ["name", "photo", "title", "category", "tags", "speacials"]



class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"