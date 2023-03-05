from handlers.admin_command import register_command_add_admin
from handlers.command_start import register_command_start
from handlers.command_help import register_command_help
from handlers.txt2txt import register_txt2txt
from handlers.command_debug import register_command_debug
from handlers.command_unknown import register_command_unknown


def handlers_registrations(dispatcher):
    # Admins commands
    register_command_add_admin(dispatcher)

    # Users commands
    register_command_start(dispatcher)
    register_command_help(dispatcher)
    register_command_debug(dispatcher)

    # Secret command

    register_command_unknown(dispatcher)
    register_txt2txt(dispatcher)


def all_registrations(dispatcher):
    handlers_registrations(dispatcher)
