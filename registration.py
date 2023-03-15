from filters.alowed_users import registration_allowed_users_filter
from handlers.admin_command.command_add_allowed_user import register_command_add_allowed_user
from handlers.danial_msg import register_danial_msg

from filters.admin_filter import registration_admin_filter

from handlers.admin_command import register_command_add_admin
from handlers.command_start import register_command_start
from handlers.command_help import register_command_help
from handlers.command_debug import register_command_debug
from handlers.response_generator import register_response_generator
from handlers.command_img import register_command_img
from handlers.command_unknown import register_command_unknown
from handlers.balance_check import register_balance_check
from handlers.command_balance import register_command_balance
from handlers.admin_command.command_change_token import register_command_change_token
from handlers.admin_command.command_remove_allowed_user import register_command_remove_allowed_user


def handlers_registrations(dispatcher):
    #  check user access
    register_danial_msg(dispatcher)

    # Admins commands
    # register_command_add_admin(dispatcher)
    register_command_add_allowed_user(dispatcher)
    register_command_remove_allowed_user(dispatcher)
    register_command_change_token(dispatcher)

    # Check balance handler
    register_balance_check(dispatcher)

    # Users commands
    register_command_start(dispatcher)
    register_command_help(dispatcher)
    register_command_debug(dispatcher)
    register_command_balance(dispatcher)
    register_command_img(dispatcher)

    # if not of the commands didn't fit
    register_command_unknown(dispatcher)

    # Send every message in gpt if msg it's not command
    register_response_generator(dispatcher)


def filters_registrations(dispatcher):
    registration_admin_filter(dispatcher)
    registration_allowed_users_filter(dispatcher)


def all_registrations(dispatcher):
    handlers_registrations(dispatcher)
    filters_registrations(dispatcher)
