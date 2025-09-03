
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce
from transactions.models import Transaction
import datetime

class MonthlySummaryView(APIView):
	"""
	API view to get a summary of income and expenses for the current month.
	"""
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		# Allow ?year=YYYY&month=MM (1-12 or 01-12)
		year = request.query_params.get('year')
		month = request.query_params.get('month')
		today = datetime.date.today()
		try:
			year = int(year) if year else today.year
			month = int(month) if month else today.month
			# Validate month
			if not (1 <= month <= 12):
				raise ValueError
			start_of_month = datetime.date(year, month, 1)
		except Exception:
			return Response({'detail': 'Invalid year or month.'}, status=status.HTTP_400_BAD_REQUEST)

		# Calculate the first day of the next month for filtering
		if month == 12:
			next_month = datetime.date(year + 1, 1, 1)
		else:
			next_month = datetime.date(year, month + 1, 1)

		# Get all transactions for the current user in the selected month
		transactions = Transaction.objects.filter(
			user=request.user,
			date__gte=start_of_month,
			date__lt=next_month
		)

		# Calculate total income
		total_income = transactions.filter(transaction_type='income').aggregate(
			total=Coalesce(Sum('amount'), 0, output_field=DecimalField())
		)['total']

		# Calculate total expenses
		total_expenses = transactions.filter(transaction_type='expense').aggregate(
			total=Coalesce(Sum('amount'), 0, output_field=DecimalField())
		)['total']

		net_savings = total_income - total_expenses

		summary_data = {
			'year': year,
			'month': start_of_month.strftime('%B'),
			'total_income': total_income,
			'total_expenses': total_expenses,
			'net_savings': net_savings,
		}
		return Response(summary_data, status=status.HTTP_200_OK)
