from cmk.gui.i18n import _

from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
)

metric_info["verificationprogress"] = {
    "title": _("Verification Progress"),
    "unit": "",
    "color": "16/a",
}

metric_info["blocks"] = {
    "title": _("Blocks"),
    "unit": "count",
    "color": "26/a",
}

metric_info["headers"] = {
    "title": _("Headers"),
    "unit": "count",
    "color": "14/a",
}

metric_info["pruneheight"] = {
    "title": _("Prune Height"),
    "unit": "count",
    "color": "24/a",
}

graph_info["blocks_n_headers"] = {
    "title": _("Blocks and Headers"),
    "metrics": [
        ("blocks", "area"),
        ("headers", "line"),
        ("pruneheight", "line"),
    ],
}

## LND
metric_info["num_active_channels"] = {
    "title": _("Active Channels"),
    "unit": "count",
    "color": "16/a",
}

metric_info["num_peers"] = {
    "title": _("Peers"),
    "unit": "count",
    "color": "26/a",
}

graph_info["channels_n_peers"] = {
    "title": _("Active Channels and Peers"),
    "metrics": [
        ("num_active_channels", "line"),
        ("num_peers", "line"),
    ],
}
