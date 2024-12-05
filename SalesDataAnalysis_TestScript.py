import csv
import unittest

# Class to analyze best-selling products
class BestSelling:
    def best_selling_analysis(self):
        # Open the CSV file for reading
        with open('supermarket_sales2.csv', 'r') as file:
            reader = csv.reader(file)
            sales_data = list(reader)

        product_sales = {}

        for row in sales_data[1:]:
            product_id = row[2]  # Product ID
            sales_amount = float(row[7])  # Sales amount
            # Accumulate sales amount for each product
            if product_id in product_sales:
                product_sales[product_id] += sales_amount
            else:
                product_sales[product_id] = sales_amount

        # Sort products by total sales amount in descending order
        sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
        # Get the top 5 best-selling products
        top_products = [product[0] for product in sorted_products[:5]]
        return top_products

# Class to analyze product performance based on quantity sold
class ProductPerformance:
    def product_performance_analysis(self):
        # Open the CSV file for reading
        with open('supermarket_sales2.csv', 'r') as file:
            reader = csv.reader(file)
            sales_data = list(reader)

        product_qty = {}

        for row in sales_data[1:]:
            product_id = row[2]  # Product ID
            quantity = float(row[4])  # Quantity sold
            # Accumulate quantity sold for each product
            if product_id in product_qty:
                product_qty[product_id] += quantity
            else:
                product_qty[product_id] = quantity

        # Sort products by quantity sold in descending order
        sorted_products = sorted(product_qty.items(), key=lambda x: x[1], reverse=True)
        # Print sorted product quantities
        for product in sorted_products:
            print(product)

# Class to analyze customer behavior based on total amount spent and quantity purchased
class CustomerBehaviour:
    def customer_behavior_analysis(self):
        # Open the CSV file for reading
        with open('supermarket_sales2.csv', 'r') as file:
            reader = csv.reader(file)
            sales_data = list(reader)

        customer_sales_amount = {}
        customer_sales_qty = {}

        for row in sales_data[1:]:
            customer_id = row[1]  # Customer ID
            total_amount = float(row[7])  # Total amount spent
            quantity = float(row[4])  # Quantity purchased

            # Accumulate total amount and quantity for each customer
            if customer_id in customer_sales_amount:
                customer_sales_amount[customer_id] += total_amount
                customer_sales_qty[customer_id] += quantity
            else:
                customer_sales_amount[customer_id] = total_amount
                customer_sales_qty[customer_id] = quantity

        # Print customer data based on total amount spent
        print("\n======= Based on Total Amount Spent =============")
        print(list(customer_sales_amount.items()))
        # Print customer data based on total quantity purchased
        print("\n======= Based on Total Quantity =============")
        print(list(customer_sales_qty.items()))

# Class to analyze regional sales data
class RegionalSalesAnalysis:
    def __init__(self):
        self.sales_data = []

    # Load sales data from CSV file
    def load_sales_data(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            self.sales_data = list(reader)

    # Calculate sales by region
    def sales_by_region(self):
        region_sales = {}

        for row in self.sales_data[1:]:
            region = row[-1]  # Region
            total_price = float(row[-2])  # Total price
            # Accumulate total sales for each region
            if region in region_sales:
                region_sales[region] += total_price
            else:
                region_sales[region] = total_price
        return region_sales

    # Perform regional sales analysis
    def regional_sales_analysis(self):
        self.load_sales_data('supermarket_sales2.csv')
        region_sales = self.sales_by_region()

        # Print regional sales analysis results
        print("======= Regional Sales Analysis ===========")
        for region, sales in region_sales.items():
            print(f"Region: {region}, Total Sales: {sales}")
        print("===========================================")

# Facade class to provide a unified interface to all analysis classes
class Facade:
    def __init__(self):
        self.best_selling = BestSelling()
        self.customer_behaviour = CustomerBehaviour()
        self.product_performance = ProductPerformance()
        self.regional_sales = RegionalSalesAnalysis()

    # Execute best-selling product analysis
    def execute_best_selling_analysis(self):
        return self.best_selling.best_selling_analysis()

    # Execute customer behavior analysis
    def execute_customer_behavior_analysis(self):
        self.customer_behaviour.customer_behavior_analysis()

    # Execute product performance analysis
    def execute_product_performance_analysis(self):
        self.product_performance.product_performance_analysis()

    # Execute regional sales analysis
    def execute_regional_sales_analysis(self):
        self.regional_sales.regional_sales_analysis()

class Test(unittest.TestCase):
    def test_best_selling_analysis(self):
        facade = Facade()
        expected_top_products = ['106', '104', '103', '108', '109']  # Replace with actual expected values
        result = facade.execute_best_selling_analysis()
        self.assertEqual(result, expected_top_products)

# Main function to provide a menu-driven interface for analysis
def main():
    facade = Facade()

    while True:
        print("\n=============== Main menu ===============\n")
        print("1. Best-selling Product Analysis")
        print("2. Customer Behavior Analysis")
        print("3. Product Performance Analysis")
        print("4. Regional Sales Analysis")
        print("5. Exit\n")
        option = int(input("Enter your option: \n"))

        # Execute analysis based on user option
        if option == 1:
            facade.execute_best_selling_analysis()
        elif option == 2:
            facade.execute_customer_behavior_analysis()
        elif option == 3:
            facade.execute_product_performance_analysis()
        elif option == 4:
            facade.execute_regional_sales_analysis()
        elif option == 5:
            break
        else:
            print("Invalid option, please try again.")

# Entry point of the script
if __name__ == "__main__":
    # Run the unit tests instead of the main menu
    unittest.main()
