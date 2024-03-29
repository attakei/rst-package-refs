"""NPM registry refecence module."""
from typing import List, Optional

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner


def reference_role(
    role: str,
    rawtext: str,
    text: str,
    lineno: int,
    inliner: Inliner,
    options: Optional[dict] = None,
    content: Optional[List[str]] = None,
):
    """Parser."""
    options = roles.normalized_role_options(options)
    messages = []
    url = f"https://www.npmjs.com/package/{text}"
    return [nodes.reference(rawtext, text, refuri=url, **options)], messages


def setup():  # noqa: D103
    roles.register_canonical_role("npm", reference_role)
