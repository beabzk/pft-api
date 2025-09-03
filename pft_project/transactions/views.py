from rest_framework import viewsets, permissions
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer
from .permissions import IsOwner

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a user's categories to be viewed or edited.
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        This view should return a list of all the categories
        for the currently authenticated user.
        """
        return self.request.user.categories.all()

    def perform_create(self, serializer):
        """
        Assign the current user as the owner of the new category.
        """
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows a user's transactions to be viewed or edited.
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        This view should return a list of all the transactions
        for the currently authenticated user.
        """
        queryset = self.request.user.transactions.all()
        
        # Optional filtering by category
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category__id=category)
            
        return queryset.order_by('-date')

    def get_serializer_context(self):
        """
        Pass the default DRF context (request, format, view) to the serializer.
        """
        return super().get_serializer_context()

    def perform_create(self, serializer):
        """
        Assign the current user as the owner of the new transaction.
        """
        serializer.save(user=self.request.user)
