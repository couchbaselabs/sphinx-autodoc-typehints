# coding=utf-8
import pytest
from sphinx.util import logging


@pytest.mark.sphinx("html", testroot="annotation", freshenv=True)
def test_annotation_html(app, status, warning):
    app.config.sphinx_autodoc_alias = {("A", "B"), ("C", "D")}
    app.verbosity = 2
    logging.setup(app, status, warning)
    app.builder.doctreedir.rmtree()
    app.builder.outdir.rmtree()
    app.builder.build_all()
    assert not warning.getvalue()
    messages = [i for i in status.getvalue().split("\n") if "[autodoc-typehints][process-docstring] " in i]
    assert len(messages) == 5


@pytest.mark.sphinx("text", testroot="annotation", freshenv=True)
def test_annotation_text(app):
    app.builder.doctreedir.rmtree()
    app.builder.outdir.rmtree()
    app.builder.build_all()
    with open(app.builder.outdir / "index.txt") as out_file:
        content = out_file.read()
    assert (
        content
        == """typehints
*********

Test type hints.

test_code_annotation.test_param_init_return_str(param)

   Test one init param and return value is str.

   Parameters:
      **param** ("int") -- parameter to increase

   Return type:
      "str"

   Returns:
      increase value with one

test_code_annotation.test_param_init_return_tuple_str_ellipsis(param, i)

   Test one init param and return value is str.

   Parameters:
      * **param** ("Tuple"["str"]) -- parameter to increase

      * **i** ("int") -- integer

   Return type:
      "Tuple"["str"]

   Returns:
      increase value with one

test_code_annotation.test_param_init_return_tuple_str_int(param, i)

   Test one init param and return value is str.

   Parameters:
      * **param** ("Tuple"["str", "int"]) -- parameter to increase

      * **i** ("int") -- integer

   Return type:
      "Tuple"["str", "int"]

   Returns:
      increase value with one

test_code_annotation.test_param_init_return_union_str_int(param, i)

   Test one init param and return value is str.

   Parameters:
      * **param** ("Union"["str", "int"]) -- parameter to increase

      * **i** ("int") -- integer

   Return type:
      "Union"["str", "int"]

   Returns:
      increase value with one

test_code_annotation.test_type_var(bound_arg, either_arg)

   Test type var arguments.

   Parameters:
      * **bound_arg** ("TypeVar"("BoundArg", bound= "int")) -- bond
        parameter

      * **either_arg** ("TypeVar"("EitherOfArg", "str", "int")) --
        either of parameter

   Return type:
      "Tuple"["TypeVar"("BoundArg", bound= "int"),
      "TypeVar"("EitherOfArg", "str", "int")]

   Returns:
      tuple response
"""
    )


@pytest.mark.sphinx("text", testroot="comments", freshenv=True)
def test_comments_text(app):
    app.builder.doctreedir.rmtree()
    app.builder.outdir.rmtree()
    app.builder.build_all()
    with open(app.builder.outdir / "index.txt") as out_file:
        content = out_file.read()
    print(content)
    assert (
        content
        == """typehints
*********

Test type hints.

test_code_comments.test_param_init_return_str(param)

   Test one init param and return value is str.

   Parameters:
      **param** -- parameter to increase

   Returns:
      increase value with one

test_code_comments.test_param_init_return_tuple_str_ellipsis(param, i)

   Test one init param and return value is str.

   Parameters:
      * **param** ("Tuple"["str"]) -- parameter to increase

      * **i** ("int") -- integer

   Return type:
      "Tuple"["str"]

   Returns:
      increase value with one

test_code_comments.test_param_init_return_tuple_str_int(param, i)

   Test one init param and return value is str.

   Parameters:
      * **param** ("Tuple"["str", "int"]) -- parameter to increase

      * **i** ("int") -- integer

   Return type:
      "Tuple"["str", "int"]

   Returns:
      increase value with one

test_code_comments.test_param_init_return_union_str_int(param, i)

   Test one init param and return value is str.

   Parameters:
      * **param** ("Union"["str", "int"]) -- parameter to increase

      * **i** ("int") -- integer

   Return type:
      "Union"["str", "int"]

   Returns:
      increase value with one
"""
    )
