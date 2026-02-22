from agents.agent import ModelSettings
from dotenv import load_dotenv
from agents import Agent, Runner, function_tool

load_dotenv()


@function_tool
def calculate_mortgage(principal_amount: float, annualized_rate: float, number_of_years: int) -> str:
    """
    This function calculates the mortage payment.
    Args:
        principal_amount: The mortgage amount.
        annualized_rate: The annualized interest rate in percentage form.
        number_of_years: The number of years to pay off the mortgage.

    Returns:
        A string containing the monthly mortgage payment.

    """
    monthly_rate = (annualized_rate / 100) / 12
    number_of_payments = number_of_years * 12
    monthly_payment = (principal_amount * monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments - 1)
    return f"The monthly mortgage payment is {monthly_payment:.2f}"


mortage_agent = Agent(name="MortgageAdvisor", 
    instructions="You are a mortage assistant.", 
    tools=[calculate_mortgage],
    tool_use_behavior="stop_on_first_tool",
    model_settings=ModelSettings(tool_choice="required"),
    )

result = Runner.run_sync(mortage_agent, "What is my monthly payments if I borrow $800,000 at 6% interest rate for 30 years?")
print(result.final_output)