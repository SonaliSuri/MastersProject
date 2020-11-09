# ================
#  MESSAGE TYPES
# ================
COMMIT = "Commit"
COMMITACK = "CommitACK"
PREPARE = "Prepare"
PRE_PREPARE = "Pre-Prepare"
REQUEST = "Request"
REPLY = "Reply"


# ====================
#  node host and port
# ====================
host = 'ec2-54-153-59-159.us-west-1.compute.amazonaws.com'
port = '8362'

# ====================
#  node host and port
# ====================
host_1 = 'ec2-54-241-144-146.us-west-1.compute.amazonaws.com'
port_1 = '8358'

# ====================
#  node host and port
# ====================
host_2 = 'ec2-54-193-67-29.us-west-1.compute.amazonaws.com'
port_2 = '8357'

# ====================
#  node host and port
# ====================
host_3 = 'ec2-13-52-99-86.us-west-1.compute.amazonaws.com'
port_3 = '8356'

# ====================
#  node host and port
# ====================
host_4 = 'ec2-3-101-39-128.us-west-1.compute.amazonaws.com'
port_4 = '8355'

# ====================
#  node host and port
# ====================
host_diagram = 'localhost'
port_diagram = '8373'

# ====================
#  node host and port
# ====================
host_node = 'localhost'
port_node = '8354'


# ====================
#  number of faulty nodes, number of prepared messages, number of commit messages, number of reply messages
# ====================
faulty = 1
prep = 'prep'
commit = 'commit'
reply = 0

# ======================================
# HEADER KEY Constants
# ======================================
MSG_SEQ = "msg_seq"
VIEW = "view"
TYPE = "type"
DATA = "data"
MSG = "msg"
STRING = ""

# ======
#
# =====
open_brac = "{"
close_brac = "}"

conf_nodes = [{'host': host_1, 'port': int(port_1)}]


def get_string(char_length):
    data_string = "a"
    for i in range(char_length+2):
        data_string += data_string
    STRING = data_string
    return data_string


