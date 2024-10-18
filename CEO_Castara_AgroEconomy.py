import streamlit as st

# Defining the expanded lists
roles = {
    "Management": [
        "Marketing & Sales Manager",
        "Customer Relations Manager",
        "Distribution Manager",
        "Product & Services Manager",
        "Facilities & Resources Manager",
        "Project Manager",
        "Supply Chain & Partner Manager",
        "Cost & Expense Accounting Manager",
        "Revenue Streams Manager",
        "Franchisee Manager",
    ],
    "Franchisee": [
        "Regional Franchisee",
        "Local Franchisee",
        "Operational Manager",
        "Store Manager",
        "Sales Manager",
        "Finance Manager",
        "Inventory Manager",
        "Customer Service Manager",
        "Marketing Specialist",
        "Support Specialist",
    ],
    "Investor": [
        "Equity Investor",
        "Angel Investor",
        "Venture Capitalist",
        "Private Equity Investor",
        "Crowdfunding Investor",
        "Institutional Investor",
        "Limited Partner",
        "General Partner",
        "Board Member",
        "Strategic Advisor",
    ],
    "Supplier": [
        "Primary Supplier",
        "Logistics Partner",
        "Service Provider",
        "Raw Material Supplier",
        "Tech Provider",
        "Secondary Supplier",
        "Sustainability Consultant",
        "Supply Chain Manager",
        "Vendor Manager",
        "Quality Control Specialist",
    ],
    "Customer": [
        "B2B Customer",
        "B2C Customer",
        "Wholesale Buyer",
        "Retail Buyer",
        "Frequent Buyer",
        "Seasonal Buyer",
        "Corporate Buyer",
        "Distributor",
        "End Consumer",
        "Local Consumer",
    ]
}

actions = {
    "Operations": [
        "Process Orders",
        "Track Shipments",
        "Inventory Management",
        "Facility Management",
        "Supplier Coordination",
        "Contract Management",
        "Resource Allocation",
        "Operational Audit",
        "Logistics Optimization",
        "Franchise Management",
    ],
    "Finance": [
        "Budget Allocation",
        "Cash Flow Monitoring",
        "Expense Management",
        "Revenue Forecasting",
        "Investment Planning",
        "Financial Reporting",
        "Capital Allocation",
        "Cost Control",
        "Payroll Management",
        "Tax Compliance",
    ],
    "Marketing": [
        "Market Research",
        "Campaign Planning",
        "Brand Management",
        "Customer Segmentation",
        "Ad Budgeting",
        "Social Media Strategy",
        "Partnership Development",
        "Lead Generation",
        "PR Management",
        "Customer Feedback Analysis",
    ],
    "Sales": [
        "Sales Forecasting",
        "Price Optimization",
        "Customer Acquisition",
        "Client Relationship Management",
        "Order Processing",
        "Performance Analysis",
        "Lead Conversion",
        "Cross-Selling Strategies",
        "Sales Training",
        "Partnership Sales",
    ],
    "HR": [
        "Employee Recruitment",
        "Training Programs",
        "Payroll Management",
        "Performance Appraisal",
        "Employee Retention",
        "Conflict Resolution",
        "Workforce Planning",
        "Policy Implementation",
        "Employee Benefits Management",
        "Career Development",
    ]
}

# Streamlit app setup
st.title("Castara AgroEconomy Venture Navigation System")
st.write("Select the User role, Sub-role, Action, and Activity to begin your journey.")

# Step 1: User Role selection
selected_role = st.selectbox("Select User Role", list(roles.keys()))

# Step 2: Sub-role selection
if selected_role:
    selected_sub_role = st.selectbox("Select Sub-role", roles[selected_role])

# Step 3: Action selection
selected_action_category = st.selectbox("Select Action", list(actions.keys()))

# Step 4: Activity selection
if selected_action_category:
    selected_activity = st.selectbox("Select Activity", actions[selected_action_category])

# Button to validate combination and show outcome
if st.button("Submit"):
    if selected_role and selected_sub_role and selected_action_category and selected_activity:
        # Here we could add rules or checks for valid combinations
        st.success(f"Navigating to {selected_role} > {selected_sub_role} > {selected_action_category} > {selected_activity}")
        # This is where the navigation would occur or the appropriate page load would be triggered
    else:
        st.error("Please complete all selections to proceed.")
