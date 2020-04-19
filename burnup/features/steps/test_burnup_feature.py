from behave import *
from burnup.utils import *
from hamcrest import *
from behave import register_type
import parse

use_step_matcher("parse")




# -- REGISTER: User-defined type converter (parse_type).
register_type(NumberList=parse_list_of_number)




@given('i have a "{list:NumberList}"  of numbers')
def step_impl(context, list):
    context.data = list


@then('the lowest average is "{result:g}"')
def step_impl(context, result):
    assert_that(lowest_average_over_last_six_values(context.data), equal_to(result))


@step("i have more than 6 numbers")
def step_impl(context):
    assert_that(len(context.data), greater_than_or_equal_to(6))


@then('the highest average is "{result:g}"')
def step_impl(context, result):
    assert_that(highest_average_over_last_six_values(context.data), equal_to(result))


@step('the average is "{result:g}"')
def step_impl(context, result):
    assert_that(average_over_last_six_values(context.data), equal_to(result))


@given("i have a list of past sprint velocity")
def step_impl(context):
    context.data = [3, 34, 21, 7, 42, 9, 13, 21]


@then("i can give a best case forecast for the next 6 iterations based on the best 3 iterations over the last 6 iterations")
def step_impl(context):
    assert_that(get_best_forecast(context.data), equal_to([178, 206, 234, 262, 290,318]))


@then("i can give a worst case forecast for the next 6 iterations based on the worst 3 iterations over the last 6 iterations")
def step_impl(context):
    assert_that(get_worst_forecast(context.data), equal_to([159.67, 169.34, 179.01, 188.68, 198.35, 208.02]))


@then("i can give an average case forecast for the next 6 iterations based on at most the last 6 iterations")
def step_impl(context):
    assert_that(get_average_forecast(context.data), equal_to([168.83, 187.66, 206.49, 225.32, 244.15, 262.98]))


@then("i must get the real progress by incrementing each week with the sum of previous weeks")
def step_impl(context):
    assert_that(get_real_progress(context.data), equal_to([3, 37, 58, 65, 107, 116, 129, 150]))


@then(
    "i can give a best case forecast for the next 6 iterations based on the standard deviation on the last 6 iterations")
def step_impl(context):
    assert_that(get_best_forecast(context.data, CalculusType.STANDARDDEV), equal_to([181.61, 213.22, 244.83, 276.44, 308.05, 339.66]))

@then(
    "i can give a worst case forecast for the next 6 iterations based on the the standard deviation on  the last 6 iterations")
def step_impl(context):
    assert_that(get_worst_forecast(context.data, CalculusType.STANDARDDEV), equal_to([156.05, 162.1, 168.15, 174.2, 180.25, 186.3]))