"""
Scenario 1:
Single switch Topology
Two traffic stream (Ping and iperf) sharing bottleneck is prevented using QoS """

from mininet.net import Mininet
from mininet.cli import CLI
import os
os.system("mn -c")
net = Mininet()
h1 = net.addHost('h1')
h2 = net.addHost('h2')
s1 = net.addSwitch('s1')
c0 = net.addController('c0')

q1 = net.addQSpec(queue=0, priority=1, minRate=0.1, maxRate=0.5)
q2 = net.addQSpec(queue=1, priority=2, minRate=0.1, maxRate=0.5)

params1 = {
    'bw': 200,
    'delay': '10ms'
}
params2 = {
    'bw': 200,
    'delay': '10ms'
}
net.addQlink( h1, s1, params1=params1, params2=params2, qspec2=[q1, q2])
net.addQlink( s1, h2, params1=params1, params2=params2, qspec1=[q1, q2])

net.start()

print('Adding flows on s1 interfaces')
s1.cmdPrint('ovs-ofctl -O OpenFlow13 add-flow s1 priority=200,icmp,in_port=1,actions=set_queue:0,output:2')
s1.cmdPrint('ovs-ofctl -O OpenFlow13 add-flow s1 priority=200,icmp,in_port=2,actions=set_queue:0,output:1')
s1.cmdPrint('ovs-ofctl -O OpenFlow13 add-flow s1 priority=100,tcp,in_port=1,actions=set_queue:1,output:2')
s1.cmdPrint('ovs-ofctl -O OpenFlow13 add-flow s1 priority=100,tcp,in_port=2,actions=set_queue:1,output:1')
#print(s1.cmdPrint('ovs-ofctl dump-flows s1'))
#net.pingAll()
#net.iperf()
print(s1.cmdPrint('ovs-appctl qos/show s1-eth2'))
CLI(net)
print("List QoS queues on switch interface: s1-eth1")
print(s1.cmdPrint('ovs-appctl qos/show s1-eth1'))
print("List QoS queues on switch interface: s1-eth2")
print(s1.cmdPrint('ovs-appctl qos/show s1-eth2'))
net.stop()
