# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_external_pipeline_data 1'] = '''{
  "__class__": "ExternalPipelineData",
  "active_presets": [],
  "is_job": true,
  "name": "foo_job",
  "parent_pipeline_snapshot": null,
  "pipeline_snapshot": {
    "__class__": "PipelineSnapshot",
    "config_schema_snapshot": {
      "__class__": "ConfigSchemaSnapshot",
      "all_config_snaps_by_key": {
        "Any": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": null,
          "given_name": "Any",
          "key": "Any",
          "kind": {
            "__enum__": "ConfigTypeKind.ANY"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
          "__class__": "ConfigTypeSnap",
          "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
          "kind": {
            "__enum__": "ConfigTypeKind.ARRAY"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
          ]
        },
        "Array.String": {
          "__class__": "ConfigTypeSnap",
          "description": "List of Array.String",
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "Array.String",
          "kind": {
            "__enum__": "ConfigTypeKind.ARRAY"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "String"
          ]
        },
        "Bool": {
          "__class__": "ConfigTypeSnap",
          "description": "",
          "enum_values": null,
          "fields": null,
          "given_name": "Bool",
          "key": "Bool",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR"
          },
          "scalar_kind": {
            "__enum__": "ConfigScalarKind.BOOL"
          },
          "type_param_keys": null
        },
        "Float": {
          "__class__": "ConfigTypeSnap",
          "description": "",
          "enum_values": null,
          "fields": null,
          "given_name": "Float",
          "key": "Float",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR"
          },
          "scalar_kind": {
            "__enum__": "ConfigScalarKind.FLOAT"
          },
          "type_param_keys": null
        },
        "Int": {
          "__class__": "ConfigTypeSnap",
          "description": "",
          "enum_values": null,
          "fields": null,
          "given_name": "Int",
          "key": "Int",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR"
          },
          "scalar_kind": {
            "__enum__": "ConfigScalarKind.INT"
          },
          "type_param_keys": null
        },
        "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR_UNION"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "Bool",
            "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
          ]
        },
        "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR_UNION"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "Float",
            "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
          ]
        },
        "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR_UNION"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "Int",
            "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
          ]
        },
        "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR_UNION"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "String",
            "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
          ]
        },
        "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": null,
          "given_name": null,
          "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR_UNION"
          },
          "scalar_kind": null,
          "type_param_keys": [
            "String",
            "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
          ]
        },
        "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
              "description": "Execute all steps in a single process.",
              "is_required": false,
              "name": "in_process",
              "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
              "description": "Execute each step in an individual process.",
              "is_required": false,
              "name": "multiprocess",
              "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
            }
          ],
          "given_name": null,
          "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": null,
              "is_required": false,
              "name": "disabled",
              "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": null,
              "is_required": false,
              "name": "enabled",
              "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
            }
          ],
          "given_name": null,
          "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
              "is_required": false,
              "name": "forkserver",
              "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
              "is_required": false,
              "name": "spawn",
              "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
            }
          ],
          "given_name": null,
          "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "json",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "pickle",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "value",
              "type_key": "Int"
            }
          ],
          "given_name": null,
          "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "json",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "pickle",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "value",
              "type_key": "Bool"
            }
          ],
          "given_name": null,
          "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "json",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "pickle",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "value",
              "type_key": "Float"
            }
          ],
          "given_name": null,
          "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "json",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "pickle",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "value",
              "type_key": "String"
            }
          ],
          "given_name": null,
          "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "json",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "pickle",
              "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "value",
              "type_key": "Any"
            }
          ],
          "given_name": null,
          "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
          "kind": {
            "__enum__": "ConfigTypeKind.SELECTOR"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.07cb4c25af1ee77ffdc2d3d5b312fd61d8dc3989": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "field_aliases": {
            "ops": "solids"
          },
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
              "description": "Configure how steps are executed within a run.",
              "is_required": false,
              "name": "execution",
              "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": "Configure how loggers emit messages within a run.",
              "is_required": false,
              "name": "loggers",
              "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"foo_op\\": {}}",
              "description": "Configure runtime parameters for ops or assets.",
              "is_required": false,
              "name": "ops",
              "type_key": "Shape.15ab078f25ca130d0e38ab95bfced4126bcbf277"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"io_manager\\": {}}",
              "description": "Configure how shared resources are implemented within a run.",
              "is_required": false,
              "name": "resources",
              "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
            }
          ],
          "given_name": null,
          "key": "Shape.07cb4c25af1ee77ffdc2d3d5b312fd61d8dc3989",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "\\"INFO\\"",
              "description": "The logger\'s threshold.",
              "is_required": false,
              "name": "log_level",
              "type_key": "String"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "\\"dagster\\"",
              "description": "The name of your logger.",
              "is_required": false,
              "name": "name",
              "type_key": "String"
            }
          ],
          "given_name": null,
          "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "key",
              "type_key": "String"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "limit",
              "type_key": "Int"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": false,
              "name": "value",
              "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
            }
          ],
          "given_name": null,
          "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
              "description": "The default colored console logger.",
              "is_required": false,
              "name": "config",
              "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
            }
          ],
          "given_name": null,
          "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
              "is_required": false,
              "name": "io_manager",
              "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
            }
          ],
          "given_name": null,
          "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.15ab078f25ca130d0e38ab95bfced4126bcbf277": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "field_aliases": {
            "ops": "solids"
          },
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{}",
              "description": null,
              "is_required": false,
              "name": "foo_op",
              "type_key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f"
            }
          ],
          "given_name": null,
          "key": "Shape.15ab078f25ca130d0e38ab95bfced4126bcbf277",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "applyLimitPerUniqueValue",
              "type_key": "Bool"
            }
          ],
          "given_name": null,
          "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "field_aliases": {
            "ops": "solids"
          },
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": false,
              "name": "config",
              "type_key": "Any"
            }
          ],
          "given_name": null,
          "key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": "[DEPRECATED]",
              "is_required": false,
              "name": "marker_to_close",
              "type_key": "String"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"enabled\\": {}}",
              "description": "Whether retries are enabled or not. By default, retries are enabled.",
              "is_required": false,
              "name": "retries",
              "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
            }
          ],
          "given_name": null,
          "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": true,
              "name": "path",
              "type_key": "String"
            }
          ],
          "given_name": null,
          "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
              "is_required": false,
              "name": "preload_modules",
              "type_key": "Array.String"
            }
          ],
          "given_name": null,
          "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "0",
              "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
              "is_required": false,
              "name": "max_concurrent",
              "type_key": "Int"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"enabled\\": {}}",
              "description": "Whether retries are enabled or not. By default, retries are enabled.",
              "is_required": false,
              "name": "retries",
              "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
              "is_required": false,
              "name": "start_method",
              "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
            },
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
              "is_required": false,
              "name": "tag_concurrency_limits",
              "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
            }
          ],
          "given_name": null,
          "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": false,
              "name": "config",
              "type_key": "Any"
            }
          ],
          "given_name": null,
          "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [],
          "given_name": null,
          "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": false,
              "name": "console",
              "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
            }
          ],
          "given_name": null,
          "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
          "__class__": "ConfigTypeSnap",
          "description": null,
          "enum_values": null,
          "fields": [
            {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"multiprocess\\": {}}",
              "description": null,
              "is_required": false,
              "name": "config",
              "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
            }
          ],
          "given_name": null,
          "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
          "kind": {
            "__enum__": "ConfigTypeKind.STRICT_SHAPE"
          },
          "scalar_kind": null,
          "type_param_keys": null
        },
        "String": {
          "__class__": "ConfigTypeSnap",
          "description": "",
          "enum_values": null,
          "fields": null,
          "given_name": "String",
          "key": "String",
          "kind": {
            "__enum__": "ConfigTypeKind.SCALAR"
          },
          "scalar_kind": {
            "__enum__": "ConfigScalarKind.STRING"
          },
          "type_param_keys": null
        }
      }
    },
    "dagster_type_namespace_snapshot": {
      "__class__": "DagsterTypeNamespaceSnapshot",
      "all_dagster_type_snaps_by_key": {
        "Any": {
          "__class__": "DagsterTypeSnap",
          "description": null,
          "display_name": "Any",
          "is_builtin": true,
          "key": "Any",
          "kind": {
            "__enum__": "DagsterTypeKind.ANY"
          },
          "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
          "materializer_schema_key": null,
          "name": "Any",
          "type_param_keys": []
        },
        "Bool": {
          "__class__": "DagsterTypeSnap",
          "description": null,
          "display_name": "Bool",
          "is_builtin": true,
          "key": "Bool",
          "kind": {
            "__enum__": "DagsterTypeKind.SCALAR"
          },
          "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
          "materializer_schema_key": null,
          "name": "Bool",
          "type_param_keys": []
        },
        "Float": {
          "__class__": "DagsterTypeSnap",
          "description": null,
          "display_name": "Float",
          "is_builtin": true,
          "key": "Float",
          "kind": {
            "__enum__": "DagsterTypeKind.SCALAR"
          },
          "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
          "materializer_schema_key": null,
          "name": "Float",
          "type_param_keys": []
        },
        "Int": {
          "__class__": "DagsterTypeSnap",
          "description": null,
          "display_name": "Int",
          "is_builtin": true,
          "key": "Int",
          "kind": {
            "__enum__": "DagsterTypeKind.SCALAR"
          },
          "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
          "materializer_schema_key": null,
          "name": "Int",
          "type_param_keys": []
        },
        "Nothing": {
          "__class__": "DagsterTypeSnap",
          "description": null,
          "display_name": "Nothing",
          "is_builtin": true,
          "key": "Nothing",
          "kind": {
            "__enum__": "DagsterTypeKind.NOTHING"
          },
          "loader_schema_key": null,
          "materializer_schema_key": null,
          "name": "Nothing",
          "type_param_keys": []
        },
        "String": {
          "__class__": "DagsterTypeSnap",
          "description": null,
          "display_name": "String",
          "is_builtin": true,
          "key": "String",
          "kind": {
            "__enum__": "DagsterTypeKind.SCALAR"
          },
          "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
          "materializer_schema_key": null,
          "name": "String",
          "type_param_keys": []
        }
      }
    },
    "dep_structure_snapshot": {
      "__class__": "DependencyStructureSnapshot",
      "solid_invocation_snaps": [
        {
          "__class__": "SolidInvocationSnap",
          "input_dep_snaps": [],
          "is_dynamic_mapped": false,
          "solid_def_name": "foo_op",
          "solid_name": "foo_op",
          "tags": {}
        }
      ]
    },
    "description": null,
    "graph_def_name": "foo_job",
    "lineage_snapshot": null,
    "mode_def_snaps": [
      {
        "__class__": "ModeDefSnap",
        "description": null,
        "logger_def_snaps": [
          {
            "__class__": "LoggerDefSnap",
            "config_field_snap": {
              "__class__": "ConfigFieldSnap",
              "default_provided": true,
              "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
              "description": "The default colored console logger.",
              "is_required": false,
              "name": "config",
              "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
            },
            "description": "The default colored console logger.",
            "name": "console"
          }
        ],
        "name": "default",
        "resource_def_snaps": [
          {
            "__class__": "ResourceDefSnap",
            "config_field_snap": {
              "__class__": "ConfigFieldSnap",
              "default_provided": false,
              "default_value_as_json_str": null,
              "description": null,
              "is_required": false,
              "name": "config",
              "type_key": "Any"
            },
            "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
            "name": "io_manager"
          }
        ],
        "root_config_key": "Shape.07cb4c25af1ee77ffdc2d3d5b312fd61d8dc3989"
      }
    ],
    "name": "foo_job",
    "solid_definitions_snapshot": {
      "__class__": "SolidDefinitionsSnapshot",
      "composite_solid_def_snaps": [],
      "solid_def_snaps": [
        {
          "__class__": "SolidDefSnap",
          "config_field_snap": {
            "__class__": "ConfigFieldSnap",
            "default_provided": false,
            "default_value_as_json_str": null,
            "description": null,
            "is_required": false,
            "name": "config",
            "type_key": "Any"
          },
          "description": null,
          "input_def_snaps": [],
          "name": "foo_op",
          "output_def_snaps": [
            {
              "__class__": "OutputDefSnap",
              "dagster_type_key": "Any",
              "description": null,
              "is_dynamic": false,
              "is_required": true,
              "name": "result"
            }
          ],
          "required_resource_keys": [],
          "tags": {}
        }
      ]
    },
    "tags": {}
  }
}'''

snapshots['test_external_repository_data 1'] = '''{
  "__class__": "ExternalRepositoryData",
  "external_asset_graph_data": [],
  "external_job_refs": null,
  "external_partition_set_datas": [
    {
      "__class__": "ExternalPartitionSetData",
      "external_partitions_data": {
        "__class__": "ExternalTimeWindowPartitionsDefinitionData",
        "cron_schedule": "15 0 * * *",
        "day_offset": null,
        "end_offset": 0,
        "fmt": "%Y-%m-%d",
        "hour_offset": null,
        "minute_offset": null,
        "schedule_type": null,
        "start": 1577836800.0,
        "timezone": "UTC"
      },
      "mode": "default",
      "name": "foo_job_partition_set",
      "pipeline_name": "foo_job",
      "solid_selection": null
    }
  ],
  "external_pipeline_datas": [
    {
      "__class__": "ExternalPipelineData",
      "active_presets": [],
      "is_job": true,
      "name": "foo_job",
      "parent_pipeline_snapshot": null,
      "pipeline_snapshot": {
        "__class__": "PipelineSnapshot",
        "config_schema_snapshot": {
          "__class__": "ConfigSchemaSnapshot",
          "all_config_snaps_by_key": {
            "Any": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": null,
              "given_name": "Any",
              "key": "Any",
              "kind": {
                "__enum__": "ConfigTypeKind.ANY"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
              "__class__": "ConfigTypeSnap",
              "description": "List of Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
              "kind": {
                "__enum__": "ConfigTypeKind.ARRAY"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
              ]
            },
            "Array.String": {
              "__class__": "ConfigTypeSnap",
              "description": "List of Array.String",
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "Array.String",
              "kind": {
                "__enum__": "ConfigTypeKind.ARRAY"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "String"
              ]
            },
            "Bool": {
              "__class__": "ConfigTypeSnap",
              "description": "",
              "enum_values": null,
              "fields": null,
              "given_name": "Bool",
              "key": "Bool",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR"
              },
              "scalar_kind": {
                "__enum__": "ConfigScalarKind.BOOL"
              },
              "type_param_keys": null
            },
            "Float": {
              "__class__": "ConfigTypeSnap",
              "description": "",
              "enum_values": null,
              "fields": null,
              "given_name": "Float",
              "key": "Float",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR"
              },
              "scalar_kind": {
                "__enum__": "ConfigScalarKind.FLOAT"
              },
              "type_param_keys": null
            },
            "Int": {
              "__class__": "ConfigTypeSnap",
              "description": "",
              "enum_values": null,
              "fields": null,
              "given_name": "Int",
              "key": "Int",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR"
              },
              "scalar_kind": {
                "__enum__": "ConfigScalarKind.INT"
              },
              "type_param_keys": null
            },
            "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR_UNION"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "Bool",
                "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59"
              ]
            },
            "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR_UNION"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "Float",
                "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3"
              ]
            },
            "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR_UNION"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "Int",
                "Selector.a9799b971d12ace70a2d8803c883c863417d0725"
              ]
            },
            "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR_UNION"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "String",
                "Selector.e04723c9d9937e3ab21206435b22247cfbe58269"
              ]
            },
            "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": null,
              "given_name": null,
              "key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR_UNION"
              },
              "scalar_kind": null,
              "type_param_keys": [
                "String",
                "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
              ]
            },
            "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"retries\\": {\\"enabled\\": {}}}",
                  "description": "Execute all steps in a single process.",
                  "is_required": false,
                  "name": "in_process",
                  "type_key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}",
                  "description": "Execute each step in an individual process.",
                  "is_required": false,
                  "name": "multiprocess",
                  "type_key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1"
                }
              ],
              "given_name": null,
              "key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": null,
                  "is_required": false,
                  "name": "disabled",
                  "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": null,
                  "is_required": false,
                  "name": "enabled",
                  "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
                }
              ],
              "given_name": null,
              "key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": "Configure the multiprocess executor to start subprocesses using `forkserver`.",
                  "is_required": false,
                  "name": "forkserver",
                  "type_key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": "Configure the multiprocess executor to start subprocesses using `spawn`.",
                  "is_required": false,
                  "name": "spawn",
                  "type_key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709"
                }
              ],
              "given_name": null,
              "key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.a9799b971d12ace70a2d8803c883c863417d0725": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "json",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "pickle",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "value",
                  "type_key": "Int"
                }
              ],
              "given_name": null,
              "key": "Selector.a9799b971d12ace70a2d8803c883c863417d0725",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "json",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "pickle",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "value",
                  "type_key": "Bool"
                }
              ],
              "given_name": null,
              "key": "Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "json",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "pickle",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "value",
                  "type_key": "Float"
                }
              ],
              "given_name": null,
              "key": "Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.e04723c9d9937e3ab21206435b22247cfbe58269": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "json",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "pickle",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "value",
                  "type_key": "String"
                }
              ],
              "given_name": null,
              "key": "Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "json",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "pickle",
                  "type_key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "value",
                  "type_key": "Any"
                }
              ],
              "given_name": null,
              "key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
              "kind": {
                "__enum__": "ConfigTypeKind.SELECTOR"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.07cb4c25af1ee77ffdc2d3d5b312fd61d8dc3989": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "field_aliases": {
                "ops": "solids"
              },
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"config\\": {\\"multiprocess\\": {\\"max_concurrent\\": 0, \\"retries\\": {\\"enabled\\": {}}}}}",
                  "description": "Configure how steps are executed within a run.",
                  "is_required": false,
                  "name": "execution",
                  "type_key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": "Configure how loggers emit messages within a run.",
                  "is_required": false,
                  "name": "loggers",
                  "type_key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"foo_op\\": {}}",
                  "description": "Configure runtime parameters for ops or assets.",
                  "is_required": false,
                  "name": "ops",
                  "type_key": "Shape.15ab078f25ca130d0e38ab95bfced4126bcbf277"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"io_manager\\": {}}",
                  "description": "Configure how shared resources are implemented within a run.",
                  "is_required": false,
                  "name": "resources",
                  "type_key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778"
                }
              ],
              "given_name": null,
              "key": "Shape.07cb4c25af1ee77ffdc2d3d5b312fd61d8dc3989",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.081354663b9d4b8fbfd1cb8e358763912953913f": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "\\"INFO\\"",
                  "description": "The logger\'s threshold.",
                  "is_required": false,
                  "name": "log_level",
                  "type_key": "String"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "\\"dagster\\"",
                  "description": "The name of your logger.",
                  "is_required": false,
                  "name": "name",
                  "type_key": "String"
                }
              ],
              "given_name": null,
              "key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "key",
                  "type_key": "String"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "limit",
                  "type_key": "Int"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": false,
                  "name": "value",
                  "type_key": "ScalarUnion.String-Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85"
                }
              ],
              "given_name": null,
              "key": "Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
                  "description": "The default colored console logger.",
                  "is_required": false,
                  "name": "config",
                  "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
                }
              ],
              "given_name": null,
              "key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
                  "is_required": false,
                  "name": "io_manager",
                  "type_key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7"
                }
              ],
              "given_name": null,
              "key": "Shape.1578133c1c71e8e3c9cf3ad46c216eb51b48c778",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.15ab078f25ca130d0e38ab95bfced4126bcbf277": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "field_aliases": {
                "ops": "solids"
              },
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{}",
                  "description": null,
                  "is_required": false,
                  "name": "foo_op",
                  "type_key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f"
                }
              ],
              "given_name": null,
              "key": "Shape.15ab078f25ca130d0e38ab95bfced4126bcbf277",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "applyLimitPerUniqueValue",
                  "type_key": "Bool"
                }
              ],
              "given_name": null,
              "key": "Shape.24ddf8da2b4484ca9c900e229e17286c1e1f6e85",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "field_aliases": {
                "ops": "solids"
              },
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": false,
                  "name": "config",
                  "type_key": "Any"
                }
              ],
              "given_name": null,
              "key": "Shape.36f967aeb3f6dab9d3a24674eef563a75d431b7f",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": "[DEPRECATED]",
                  "is_required": false,
                  "name": "marker_to_close",
                  "type_key": "String"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"enabled\\": {}}",
                  "description": "Whether retries are enabled or not. By default, retries are enabled.",
                  "is_required": false,
                  "name": "retries",
                  "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
                }
              ],
              "given_name": null,
              "key": "Shape.44f24ac55059da1634e84af6c1bf7e0ed332251c",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": true,
                  "name": "path",
                  "type_key": "String"
                }
              ],
              "given_name": null,
              "key": "Shape.4b53b73df342381d0d05c5f36183dc99cb9676e2",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": "Explicitly specify the modules to preload in the forkserver. Otherwise, there are two cases for default values if modules are not specified. If the Dagster job was loaded from a module, the same module will be preloaded. If not, the `dagster` module is preloaded.",
                  "is_required": false,
                  "name": "preload_modules",
                  "type_key": "Array.String"
                }
              ],
              "given_name": null,
              "key": "Shape.4b5c35afb20df31266eeee7e8c1060f1b490d054",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.60acefe08e1243b47034a632522b12985eb4acd1": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "0",
                  "description": "The number of processes that may run concurrently. By default, this is set to be the return value of `multiprocessing.cpu_count()`.",
                  "is_required": false,
                  "name": "max_concurrent",
                  "type_key": "Int"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"enabled\\": {}}",
                  "description": "Whether retries are enabled or not. By default, retries are enabled.",
                  "is_required": false,
                  "name": "retries",
                  "type_key": "Selector.1bfb167aea90780aa679597800c71bd8c65ed0b2"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": "Select how subprocesses are created. By default, `spawn` is selected. See https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods.",
                  "is_required": false,
                  "name": "start_method",
                  "type_key": "Selector.8318f5aff6cd0698a5c7fedfb9bdc75fd8006db8"
                },
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": "A set of limits that are applied to steps with particular tags. If a value is set, the limit is applied to only that key-value pair. If no value is set, the limit is applied across all values of that key. If the value is set to a dict with `applyLimitPerUniqueValue: true`, the limit will apply to the number of unique values for that key. Note that these limits are per run, not global.",
                  "is_required": false,
                  "name": "tag_concurrency_limits",
                  "type_key": "Array.Shape.0c1ec89f38a496d79fd06df0e76cb61d9c5b7a8d"
                }
              ],
              "given_name": null,
              "key": "Shape.60acefe08e1243b47034a632522b12985eb4acd1",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.743e47901855cb245064dd633e217bfcb49a11a7": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": false,
                  "name": "config",
                  "type_key": "Any"
                }
              ],
              "given_name": null,
              "key": "Shape.743e47901855cb245064dd633e217bfcb49a11a7",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [],
              "given_name": null,
              "key": "Shape.da39a3ee5e6b4b0d3255bfef95601890afd80709",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": false,
                  "name": "console",
                  "type_key": "Shape.0fe8353d6b542accfad9becbdbaeb92f649ebb9a"
                }
              ],
              "given_name": null,
              "key": "Shape.e895d95ee6d0eff1b884c76f44a2ab7089f0c49b",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b": {
              "__class__": "ConfigTypeSnap",
              "description": null,
              "enum_values": null,
              "fields": [
                {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"multiprocess\\": {}}",
                  "description": null,
                  "is_required": false,
                  "name": "config",
                  "type_key": "Selector.00371ab72ca40393148a9c985b86e3fba193b4e2"
                }
              ],
              "given_name": null,
              "key": "Shape.f74882eed6db21825b8461f675d1a11e200f2f1b",
              "kind": {
                "__enum__": "ConfigTypeKind.STRICT_SHAPE"
              },
              "scalar_kind": null,
              "type_param_keys": null
            },
            "String": {
              "__class__": "ConfigTypeSnap",
              "description": "",
              "enum_values": null,
              "fields": null,
              "given_name": "String",
              "key": "String",
              "kind": {
                "__enum__": "ConfigTypeKind.SCALAR"
              },
              "scalar_kind": {
                "__enum__": "ConfigScalarKind.STRING"
              },
              "type_param_keys": null
            }
          }
        },
        "dagster_type_namespace_snapshot": {
          "__class__": "DagsterTypeNamespaceSnapshot",
          "all_dagster_type_snaps_by_key": {
            "Any": {
              "__class__": "DagsterTypeSnap",
              "description": null,
              "display_name": "Any",
              "is_builtin": true,
              "key": "Any",
              "kind": {
                "__enum__": "DagsterTypeKind.ANY"
              },
              "loader_schema_key": "Selector.f2fe6dfdc60a1947a8f8e7cd377a012b47065bc4",
              "materializer_schema_key": null,
              "name": "Any",
              "type_param_keys": []
            },
            "Bool": {
              "__class__": "DagsterTypeSnap",
              "description": null,
              "display_name": "Bool",
              "is_builtin": true,
              "key": "Bool",
              "kind": {
                "__enum__": "DagsterTypeKind.SCALAR"
              },
              "loader_schema_key": "ScalarUnion.Bool-Selector.be5d518b39e86a43c5f2eecaf538c1f6c7711b59",
              "materializer_schema_key": null,
              "name": "Bool",
              "type_param_keys": []
            },
            "Float": {
              "__class__": "DagsterTypeSnap",
              "description": null,
              "display_name": "Float",
              "is_builtin": true,
              "key": "Float",
              "kind": {
                "__enum__": "DagsterTypeKind.SCALAR"
              },
              "loader_schema_key": "ScalarUnion.Float-Selector.d00a37e3807d37c9f69cc62997c4a5f4a176e5c3",
              "materializer_schema_key": null,
              "name": "Float",
              "type_param_keys": []
            },
            "Int": {
              "__class__": "DagsterTypeSnap",
              "description": null,
              "display_name": "Int",
              "is_builtin": true,
              "key": "Int",
              "kind": {
                "__enum__": "DagsterTypeKind.SCALAR"
              },
              "loader_schema_key": "ScalarUnion.Int-Selector.a9799b971d12ace70a2d8803c883c863417d0725",
              "materializer_schema_key": null,
              "name": "Int",
              "type_param_keys": []
            },
            "Nothing": {
              "__class__": "DagsterTypeSnap",
              "description": null,
              "display_name": "Nothing",
              "is_builtin": true,
              "key": "Nothing",
              "kind": {
                "__enum__": "DagsterTypeKind.NOTHING"
              },
              "loader_schema_key": null,
              "materializer_schema_key": null,
              "name": "Nothing",
              "type_param_keys": []
            },
            "String": {
              "__class__": "DagsterTypeSnap",
              "description": null,
              "display_name": "String",
              "is_builtin": true,
              "key": "String",
              "kind": {
                "__enum__": "DagsterTypeKind.SCALAR"
              },
              "loader_schema_key": "ScalarUnion.String-Selector.e04723c9d9937e3ab21206435b22247cfbe58269",
              "materializer_schema_key": null,
              "name": "String",
              "type_param_keys": []
            }
          }
        },
        "dep_structure_snapshot": {
          "__class__": "DependencyStructureSnapshot",
          "solid_invocation_snaps": [
            {
              "__class__": "SolidInvocationSnap",
              "input_dep_snaps": [],
              "is_dynamic_mapped": false,
              "solid_def_name": "foo_op",
              "solid_name": "foo_op",
              "tags": {}
            }
          ]
        },
        "description": null,
        "graph_def_name": "foo_job",
        "lineage_snapshot": null,
        "mode_def_snaps": [
          {
            "__class__": "ModeDefSnap",
            "description": null,
            "logger_def_snaps": [
              {
                "__class__": "LoggerDefSnap",
                "config_field_snap": {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": true,
                  "default_value_as_json_str": "{\\"log_level\\": \\"INFO\\", \\"name\\": \\"dagster\\"}",
                  "description": "The default colored console logger.",
                  "is_required": false,
                  "name": "config",
                  "type_key": "Shape.081354663b9d4b8fbfd1cb8e358763912953913f"
                },
                "description": "The default colored console logger.",
                "name": "console"
              }
            ],
            "name": "default",
            "resource_def_snaps": [
              {
                "__class__": "ResourceDefSnap",
                "config_field_snap": {
                  "__class__": "ConfigFieldSnap",
                  "default_provided": false,
                  "default_value_as_json_str": null,
                  "description": null,
                  "is_required": false,
                  "name": "config",
                  "type_key": "Any"
                },
                "description": "Built-in filesystem IO manager that stores and retrieves values using pickling.",
                "name": "io_manager"
              }
            ],
            "root_config_key": "Shape.07cb4c25af1ee77ffdc2d3d5b312fd61d8dc3989"
          }
        ],
        "name": "foo_job",
        "solid_definitions_snapshot": {
          "__class__": "SolidDefinitionsSnapshot",
          "composite_solid_def_snaps": [],
          "solid_def_snaps": [
            {
              "__class__": "SolidDefSnap",
              "config_field_snap": {
                "__class__": "ConfigFieldSnap",
                "default_provided": false,
                "default_value_as_json_str": null,
                "description": null,
                "is_required": false,
                "name": "config",
                "type_key": "Any"
              },
              "description": null,
              "input_def_snaps": [],
              "name": "foo_op",
              "output_def_snaps": [
                {
                  "__class__": "OutputDefSnap",
                  "dagster_type_key": "Any",
                  "description": null,
                  "is_dynamic": false,
                  "is_required": true,
                  "name": "result"
                }
              ],
              "required_resource_keys": [],
              "tags": {}
            }
          ]
        },
        "tags": {}
      }
    }
  ],
  "external_resource_data": [],
  "external_schedule_datas": [
    {
      "__class__": "ExternalScheduleData",
      "cron_schedule": "@daily",
      "description": null,
      "environment_vars": {},
      "execution_timezone": "US/Central",
      "mode": "default",
      "name": "foo_schedule",
      "partition_set_name": null,
      "pipeline_name": "foo_job",
      "solid_selection": null
    }
  ],
  "external_sensor_datas": [],
  "name": "repo",
  "utilized_env_vars": {}
}'''
