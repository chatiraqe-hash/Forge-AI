from typing import Callable, Any


PluginHook = Callable[[dict[str, Any]], dict[str, Any]]

_PLUGINS: dict[str, list[PluginHook]] = {
    "before_generate": [],
    "after_generate": [],
    "before_export": [],
    "after_export": [],
}


def register_plugin(hook: str, plugin: PluginHook) -> None:
    if hook not in _PLUGINS:
        raise ValueError(f"Unknown plugin hook: {hook}")

    _PLUGINS[hook].append(plugin)


def run_plugins(hook: str, context: dict[str, Any]) -> dict[str, Any]:
    if hook not in _PLUGINS:
        raise ValueError(f"Unknown plugin hook: {hook}")

    for plugin in _PLUGINS[hook]:
        context = plugin(context)

    return context