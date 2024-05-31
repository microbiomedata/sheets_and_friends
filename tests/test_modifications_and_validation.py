import pytest
from glom import glom

from sheets_and_friends.modifications_and_validation import add_attribute_handler, \
    add_example_handler, overwrite_example_handler, replace_annotation_handler, \
    replace_attribute_handler, remove_attribute_handler


@pytest.fixture
def schema_dict():
    return {
        "name": "schema",
        "id": "schema",
        "slots": {
            "slot1": {
                "name": "slot1",
            },
            "slot2": {
                "name": "slot2",
            }
        },
        "classes": {
            "class1": {
                "name": "class1",
                "id": "class1",
                "slots": [
                    "slot1",
                    "slot2",
                ],
                "slot_usage": {
                    "slot1": {
                        "name": "slot1",
                        "range": "string",
                        "todos": [
                            "todo #1"
                        ],
                        "examples": [
                            {"value": "example #1"}
                        ],
                        "annotations": {
                            "annotation_name_1": {
                                "tag": "annotation_name_1",
                                "value": "annotation #1"
                            }
                        }
                    },
                    "slot2": {
                        "name": "slot2",
                    },
                }
            }
        }
    }


def test_add_attribute_handler_add_to_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    add_attribute_handler(schema_dict, base_path, "todos", "todo #2")
    assert glom(schema_dict, base_path + ".todos") == ["todo #1", "todo #2"]


def test_add_attribute_handler_add_multiple_to_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    add_attribute_handler(schema_dict, base_path, "todos", "todo #2|todo #3")
    assert glom(schema_dict, base_path + ".todos") == ["todo #1", "todo #2", "todo #3"]


def test_add_attribute_handler_create_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    add_attribute_handler(schema_dict, base_path, "notes", "note #1")
    assert glom(schema_dict, base_path + ".notes") == ["note #1"]


def test_add_attribute_handler_no_target(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    add_attribute_handler(schema_dict, base_path, "", "")
    add_attribute_handler(schema_dict, base_path, None, "")


def test_add_example_handler_add_to_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    add_example_handler(schema_dict, base_path, "examples", "example #2")
    assert glom(schema_dict, base_path + ".examples") == [
        {"value": "example #1"},
        {"value": "example #2"}
    ]


def test_add_example_handler_add_multiple_to_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    add_example_handler(schema_dict, base_path, "examples", "example #2|example #3")
    assert glom(schema_dict, base_path + ".examples") == [
        {"value": "example #1"},
        {"value": "example #2"},
        {"value": "example #3"}
    ]


def test_add_example_handler_add_no_existing(schema_dict):
    base_path = "classes.class1.slot_usage.slot2"
    add_example_handler(schema_dict, base_path, "examples", "example #4")
    assert glom(schema_dict, base_path + ".examples") == [
        {"value": "example #4"}
    ]


def test_overwrite_example_handler_single(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    overwrite_example_handler(schema_dict, base_path, "examples", "example #2")
    assert glom(schema_dict, base_path + ".examples") == [
        {"value": "example #2"}
    ]


def test_overwrite_example_handler_multiple(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    overwrite_example_handler(schema_dict, base_path, "examples", "example #2|example #3")
    assert glom(schema_dict, base_path + ".examples") == [
        {"value": "example #2"},
        {"value": "example #3"}
    ]


def test_replace_annotation_handler_replace(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_annotation_handler(schema_dict, base_path, "annotation_name_1", "annotation #1 updated")
    assert glom(schema_dict, base_path + ".annotations.annotation_name_1.value") == "annotation #1 updated"


def test_replace_annotation_handler_add(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_annotation_handler(schema_dict, base_path, "annotation_name_2", "annotation #2")
    assert glom(schema_dict, base_path + ".annotations.annotation_name_2.value") == "annotation #2"


def test_replace_annotation_handler_add_no_existing(schema_dict):
    base_path = "classes.class1.slot_usage.slot2"
    replace_annotation_handler(schema_dict, base_path, "annotation_name_3", "annotation #3")
    assert glom(schema_dict, base_path + ".annotations.annotation_name_3.value") == "annotation #3"


def test_replace_attribute_handler_add_required(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_attribute_handler(schema_dict, base_path, "required", "true")
    assert glom(schema_dict, base_path + ".required") is True


def test_replace_attribute_handler_replace_range(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_attribute_handler(schema_dict, base_path, "range", "integer")
    assert glom(schema_dict, base_path + ".range") == "integer"


def test_replace_attribute_handler_dotted_target_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_attribute_handler(schema_dict, base_path, "any_of.0.range", "string")
    assert glom(schema_dict, base_path + ".any_of.0.range") == "string"


def test_replace_attribute_handler_dotted_target_padded_list(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_attribute_handler(schema_dict, base_path, "any_of.3.range", "string")
    assert glom(schema_dict, base_path + ".any_of.0") == {}
    assert glom(schema_dict, base_path + ".any_of.1") == {}
    assert glom(schema_dict, base_path + ".any_of.2") == {}
    assert glom(schema_dict, base_path + ".any_of.3") == {"range": "string"}


def test_replace_attribute_handler_dotted_target_dict(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    replace_attribute_handler(schema_dict, base_path, "structured_pattern.syntax", "{number} {unit}")
    replace_attribute_handler(schema_dict, base_path, "structured_pattern.partial_match", "false")
    assert glom(schema_dict, base_path + ".structured_pattern") == {
        "syntax": "{number} {unit}",
        "partial_match": False
    }


def test_remove_attribute_handler(schema_dict):
    base_path = "classes.class1.slot_usage.slot1"
    remove_attribute_handler(schema_dict, base_path, "examples", "")
    assert "examples" not in glom(schema_dict, base_path)
