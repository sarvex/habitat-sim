#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from os import path as osp

import pytest
import quaternion  # noqa: F401

import habitat_sim
import habitat_sim.errors
from habitat_sim.utils.settings import make_cfg

_test_scenes = [
    osp.abspath(
        osp.join(
            osp.dirname(__file__),
            "../data/scene_datasets/mp3d_example/17DRP5sb8fy/17DRP5sb8fy.glb",
        )
    ),
    osp.abspath(
        osp.join(
            osp.dirname(__file__),
            "../data/scene_datasets/mp3d/ur6pFq6Qu1A/ur6pFq6Qu1A.glb",
        )
    ),
]


@pytest.mark.parametrize("scene", _test_scenes)
def test_semantic_scene(scene, make_cfg_settings):
    # [sangarg] This test is broken, Mosra and Alex have more context
    # disabling the test for now
    pytest.skip("Disabled")
    return
