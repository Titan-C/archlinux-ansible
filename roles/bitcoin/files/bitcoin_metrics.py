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

graph_info["blocks_n_headers"] = {
    "title": _("Blocks and Headers"),
    "metrics": [
        ("blocks", "area"),
        ("headers", "line"),
    ],
}
