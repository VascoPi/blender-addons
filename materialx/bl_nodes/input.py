# SPDX-License-Identifier: GPL-2.0-or-later
# Copyright 2022, AMD
import bpy.types

from .node_parser import NodeParser
from .. import utils

class ShaderNodeValue(NodeParser):
    """ Returns float value """

    def export(self):
        return self.get_output_default()


class ShaderNodeRGB(NodeParser):
    """ Returns color value """

    def export(self):
        return self.get_output_default()


class ShaderNodeMxShaderNodeGroup(bpy.types.ShaderNodeCustomGroup):
    bl_idname = 'ShaderNodeMxShaderNodeGroup'
    bl_label = "MaterialX"

    bl_width_default = 200

    def nested_tree_filter(self, context):
        for path_tree in bpy.context.space_data.path:
            if path_tree.node_tree.name == context.name:
                return False
        return True

    def update_group_tree(self, context):
        if self.node_tree != self.node_tree:
            self.node_tree = self.node_tree

    from ..node_tree import MxNodeTree
    node_tree: bpy.props.PointerProperty(type=MxNodeTree, poll=nested_tree_filter,
                                                   update=update_group_tree)

    bytecode: bpy.props.StringProperty()
    bytecode_hash: bpy.props.StringProperty()

    oso_path: bpy.props.StringProperty(
        name="File Path",
        description="File path used for importing MaterialX node tree from .mtlx file",
        maxlen=1024, subtype="FILE_PATH")

    def init(self, context):
        self.node_tree=bpy.data.node_groups.new(self.bl_label, utils.with_prefix("MxNodeTree"))
        if hasattr(self.node_tree, 'is_hidden'):
            self.node_tree.is_hidden=True
        # group_input = self.node_tree.nodes.new('NodeGroupInput')
        group_output = self.node_tree.nodes.new('NodeGroupOutput')
        # group_input.location = [-300, 70]
        group_output.location = [300, 70]

    def draw_label(self):
        # if self.node_tree:
        #     return self.node_tree.name

        return 'MaterialX'

    def draw_buttons(self, context, layout):

        col = layout.column(align=True)

        row = col.row(align=True)
        row.prop(self, 'oso_path')
        if self.oso_path:
            row.operator(utils.with_prefix('nodes_update_osl'), text="", icon="FILE_REFRESH").oso_path = self.oso_path


        row = col.row(align=True)


        row.template_ID(self, "node_tree")
        if self.node_tree:
            row.operator(utils.with_prefix('nodes_edit_group'), text="", icon="NODETREE").node_tree = self.node_tree.name


        #row.operator('bbn.create_group', text='', icon='ADD').node = self.name

