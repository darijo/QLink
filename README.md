# QLink
QLink extends Mininet API to enable emulating links with multiple queues to differentiate between different traffic streams. QLink extends Mininet API to enable emulating links with multiple queues to differentiate between different traffic streams. We extend Mininet API with an addqLink method that receives both link emulation and queuing parameters. Assigning traffic to queues is achieved through OpenFlow (OF) rules that can be installed through the application build on top of any SDN controller.

Authors: Meghana Salian, Ahmed H. Zahran <a.zahran@cs.ucc.ie>.

Contents:

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [Caveats](#caveats)
- [Acknowledgements](#acknowledgements)


## Requirements

- Python
- Mininet (tested on version 2.3.0)


## Installation

Clone the repository
	
	git clone https://github.com/darijo/QLink.git

	
Download Mininet version 2.3.0

	git clone https://github.com/mininet/mininet

	cd mininet
	
	git checkout -b mininet-2.3.0 2.3.0

	cd ..
	
Backup <net.py>, <node.py>, and <util.py> files in mininet/mininet folder
Copy <net.py>, <node.py>, and <util.py> from files folder to mininet/mininet folder or use provided patch file <qlink.patch> (patch -s -p1 < qlink.patch)

Install Mininet 

	mininet/util/install.sh -a

## Usage

Create simple one switch topology with two nodes and two traffic types

	python single_switch_scenario.py
	
Create two switch topology with two nodes and two traffic types

	python multi_switch_scenario.py

QLink extends Mininet with two key method, namely <addQSpec> and <addQLink>. addQspec is used to define individual child queue specifications, including:

 - queue: a non-negative integer queue identifier. This identifier can be used in to direct the traffic to this queue.
 - priority: an integer {0, .., 7}, where smaller values represent higher priorities. (default 7)
 - minRate: a fraction [0, 1] and represents the sustained ratio of the parent (root) bandwidth. (default 0.01)
 - maxRate: a fraction [0, 1] and represents the maximum allowable ratio of the parent bandwidth. (default 1)
 
Example of use:

	q1 = net.addQspec(queue=0, priority=1, minRate=0.1, maxRate =0.5)
	

 
addQlink is used to create a link between two Mininet nodes using the following parameters

- two mininet node names
- params1 (params2): a dictionary defining the link parameters with params1 (params2) representing the link parameters from the first (second) to the second (first) nodes.
- qspec1 (qspec2): a list of queues that are defined using addQspec. These queues are installed as children queues at the first (second) node.

Example of use:

	net.addQlink (s1, s2, params1 ={'bw ':200, 'delay': '10ms'}, params2={'bw':20, 'delay': '10ms'}, qspec1=[q1, q2], qspec2=[q1, q2 ])



