from cmk.graphing.v1 import Title
from cmk.graphing.v1.graphs import Graph
from cmk.graphing.v1.metrics import Color, DecimalNotation, Metric, Unit

metric_info_verificationprogress = Metric(
    name="verificationprogress",
    title=Title("Verification Progress"),
    unit=Unit(DecimalNotation("%")),
    color=Color.GREEN,
)

metric_info_blocks = Metric(
    name="blocks",
    title=Title("Blocks"),
    unit=Unit(DecimalNotation("")),
    color=Color.BLUE,
)

metric_info_headers = Metric(
    name="headers",
    title=Title("Headers"),
    unit=Unit(DecimalNotation("")),
    color=Color.LIGHT_GREEN,
)

metric_info_pruneheight = Metric(
    name="pruneheight",
    title=Title("Prune Height"),
    unit=Unit(DecimalNotation("")),
    color=Color.LIGHT_PURPLE,
)

graph_blocks_n_headers = Graph(
    name="blocks_n_headers",
    title=Title("Blocks and Headers"),
    simple_lines=["blocks", "header"],
    compound_lines=["pruneheight"],
    optional=["pruneheight"],
)

metric_info_num_active_channels = Metric(
    name="num_active_channels",
    title=Title("Active Channels"),
    unit=Unit(DecimalNotation("")),
    color=Color.DARK_YELLOW,
)

metric_info_num_peers = Metric(
    name="num_peers",
    title=Title("Peers"),
    unit=Unit(DecimalNotation("")),
    color=Color.BROWN,
)

graph_channels_n_peers = Graph(
    name="channels_n_peers",
    title=Title("Active Channels and Peers"),
    simple_lines=["num_active_channels", "num_peers"],
)
