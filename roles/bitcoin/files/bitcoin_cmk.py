#!/usr/bin/env python3

from .agent_based_api.v1 import *
import json

# BITCOIND
## <<<bitcoind:sep(0):cached(1693046953,60)>>>
## {"chain":"main","blocks":804919,"headers":804919,"bestblockhash":"000000000000000000028be7a06ffd3b61e818620a13eb4f4ce909eb762b1f6b","difficulty":55621444139429.57,"time":1693044800,"mediantime":1693043488,"verificationprogress":0.9999910682858709,"initialblockdownload":false,"chainwork":"000000000000000000000000000000000000000053638ae08fce64b828e3e330","size_on_disk":1418041428,"pruned":true,"pruneheight":804167,"automatic_pruning":true,"prune_target_size":1572864000,"warnings":""}
##


def parse_bitcoind(string_table):
    return [json.loads(line[0]) for line in string_table]


register.agent_section(name="bitcoind", parse_function=parse_bitcoind)


def discover_bitcoind(section):
    for network in section:
        yield Service(item=network["chain"].upper())


def check_bitcoind(item, section):
    data = next(filter(lambda net: net["chain"].upper() == item, section))

    yield Result(state=State.OK if data else State.CRIT, summary="Daemon Running")

    if data:
        for metric in [
            "blocks",
            "headers",
            "verificationprogress",
            "pruneheight",
            "size_on_disk",
        ]:
            yield Metric(metric, data[metric])


register.check_plugin(
    name="bitcoind",
    service_name="Bitcoind %s",
    discovery_function=discover_bitcoind,
    check_function=check_bitcoind,
)


# LND
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
