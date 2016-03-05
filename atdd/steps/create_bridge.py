# -*- coding: utf-8 -*-

from behave import when, given, then
from nose import tools

from vswitch.bridge import add_br


"""Create bridges feature steps file
Feature: add-br
"""

BRIDGE_NAME = 'test'


@given('a name for the bridge')
def step_given_add_bridge(context):
    context.bridge_name = BRIDGE_NAME
    tools.assert_equal(context.bridge_name, BRIDGE_NAME)


@when('a bridge is created')
def step_when_add_bridge(context):
    context.bridge_result = add_br(name=BRIDGE_NAME)
    tools.assert_is_not_none(context.bridge_result)


@then('the bridge is created and its port and interface')
def step_then_add_bridge(context):
    tools.assert_is_not_none(context.bridge_result['port'])
    tools.assert_is_not_none(context.bridge_result['interface'])
    tools.assert_equal(context.bridge_result['port']['name'], BRIDGE_NAME)
    tools.assert_equal(context.bridge_result['interface']['name'], BRIDGE_NAME)
