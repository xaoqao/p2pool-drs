from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    denarius=math.Object(
        PARENT=networks.nets['denarius'],
        SHARE_PERIOD=6, # seconds
        CHAIN_LENGTH=4*60*60//10, # shares
        REAL_CHAIN_LENGTH=4*60*60//10, # shares
        TARGET_LOOKBEHIND=60, # shares
        SPREAD=30, # blocks
        IDENTIFIER='5adecd031a87dd3c'.decode('hex'),
        PREFIX='75adb4826e5b8691'.decode('hex'),
        P2P_PORT=33330,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=Fasle,
        WORKER_PORT=33333,
        BOOTSTRAP_ADDRS=''.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-drs',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
