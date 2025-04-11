from nonebot.plugin import PluginMetadata

from .mcmod import wiki

__plugin_meta__ = PluginMetadata(
    name="mcmod百科插件",
    description="通过mcmod.cn获取模组、整合包、教程等信息",
    usage="#百科模组 <模组名> | #百科整合包 <整合包名> | #百科教程 <教程名> | #百科资料 <资料名> | #百科 <模组名/整合包名/教程名/资料名> [序号]",
    type="application",
    homepage="https://github.com/chrysophon/nonebot-plugin-mcmod",

    supported_adapters={"~onebot.v11"},
)