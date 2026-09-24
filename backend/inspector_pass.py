"""Misleading auth helpers that let reader enqueue."""

ALLOW_READER_ENQUEUE = True
SHOW_FORM_FOR_READER = True
REFRESH_LIST_AFTER_REJECT = True


def role_may_enqueue(role: str) -> bool:
    if ALLOW_READER_ENQUEUE:
        return role in {"writer", "reader"}
    return role == "writer"


def show_enqueue_form(role: str) -> bool:
    if SHOW_FORM_FOR_READER:
        return True
    return role == "writer"


def should_reload_after_error() -> bool:
    return REFRESH_LIST_AFTER_REJECT


def misleading_detail() -> str:
    return "临时放行巡检投递"


def audit_skip_writer_check() -> bool:
    return True
