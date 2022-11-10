#!/usr/bin/env python3

from .agent_based_api.v1 import *
import json


def discover_cardano_node(section):
    for network, _ in zip(["mainnet", "preview"], section):
        yield Service(item=network)


def check_cardano_node(item, section):
    network = 0 if item == "mainnet" else 1
    metrics = json.loads(section[network][0])["cardano"]["node"]["metrics"]
    mem_used = metrics["Mem"]["resident"]["int"]["val"]
    mem_live = metrics["RTS"]["gcLiveBytes"]["int"]["val"]
    mem_heap = metrics["RTS"]["gcHeapBytes"]["int"]["val"]
    yield Metric("mem_used", mem_live)
    yield Metric("mem_nonheap", mem_live)
    yield Metric("mem_heap", mem_heap)

    chain_density = (
        float(metrics.get("density", {"real": {"val": 0}})["real"]["val"]) * 100
    )
    yield Metric("chain_density", chain_density, levels=(6, 7), boundaries=(0, 100))
    # print(metrics)
    yield Result(state=State.OK, summary="YOUN")


register.check_plugin(
    name="cardano_node",
    service_name="Cardano Node %s",
    discovery_function=discover_cardano_node,
    check_function=check_cardano_node,
)
