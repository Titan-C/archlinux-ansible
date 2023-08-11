#!/usr/bin/env python3

from .agent_based_api.v1 import *
import json


def discover_lnd(section):
    yield Service(item="Testnet")


def check_lnd(item, section):
    result = json.loads(section[0][0])
    if result.get("code") == 2:
        yield Result(state=State.CRIT, summary=result.get("message", "Something wrong"))
        return

    for metric in ["num_active_channels", "num_peers"]:
        yield Metric(metric, result[metric])

    yield Result(
        state=State.OK if result["synced_to_chain"] else State.CRIT,
        summary="Synced to chain",
    )
    yield Result(
        state=State.OK if result["synced_to_graph"] else State.CRIT,
        summary="Synced to Graph",
    )


register.check_plugin(
    name="lnd",
    service_name="LND %s",
    discovery_function=discover_lnd,
    check_function=check_lnd,
)
