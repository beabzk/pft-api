from rest_framework import serializers
from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = ['id', 'name', 'user']
        read_only_fields = ['user'] # User is set automatically from the request

class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    """
    # Use PrimaryKeyRelatedField to only allow categories owned by the current user
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False, allow_null=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the category queryset to only show categories owned by the logged-in user.
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            self.fields['category'].queryset = Category.objects.filter(user=request.user)

    class Meta:
        model = Transaction
        fields = [
            'id', 'category', 'amount', 'transaction_type', 'date', 
            'description', 'user', 'created_at'
        ]
        read_only_fields = ['user']
