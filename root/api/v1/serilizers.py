from rest_framework import serializers





class ServicesSerializer(serializers.Serializer):
    name = serializers.CharField()
    photo = serializers.ImageField()
    title = serializers.CharField()
    short_content = serializers.CharField()
    long_content = serializers.CharField()
    catalog_link = serializers.URLField(required=False, allow_null=True)
    status = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    speacials = serializers.SerializerMethodField()

    def get_category(self, obj):
        return [cat.name for cat in obj.category.all()]

    def get_tags(self, obj):
        return [tg.title for tg in obj.tags.all()]

    def get_speacials(self, obj):
        return [sp.text for sp in obj.speacials.all()]
    

class CategorySerializers(serializers.Serializer):
    name = serializers.CharField()