# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright 2022, AMD

import bpy
from nodeitems_utils import (
    NodeCategory,
    NodeItem,
)

from .. import logging
log = logging.Log("bl_nodes")


from . import (
    color,
    converter,
    input,
    output,
    shader,
    texture,
    vector,
)
node_parser_classes = (
    output.ShaderNodeOutputMaterial,

    color.ShaderNodeInvert,
    color.ShaderNodeMixRGB,

    converter.ShaderNodeMath,

    input.ShaderNodeValue,
    input.ShaderNodeRGB,

    shader.ShaderNodeAddShader,
    shader.ShaderNodeMixShader,
    shader.ShaderNodeEmission,
    shader.ShaderNodeBsdfGlass,
    shader.ShaderNodeBsdfDiffuse,
    shader.ShaderNodeBsdfPrincipled,

    texture.ShaderNodeTexImage,

    vector.ShaderNodeNormalMap,
)

node_categories = [
    NodeCategory('ShaderNodeMX_SHADER_INPUT', "MaterialX", items=[NodeItem('ShaderNodeMxShaderNodeGroup'),])]
