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
host = 'ec2-52-14-203-178.us-east-2.compute.amazonaws.com'
port = '8692'

# ====================
#  node host and port
# ====================
host_1 = 'ec2-18-216-187-228.us-east-2.compute.amazonaws.com'
port_1 = '8698'

# ====================
#  node host and port
# ====================
host_2 = 'ec2-3-19-79-195.us-east-2.compute.amazonaws.com'
port_2 = '8699'

# ====================
#  node host and port
# ====================
host_3 = 'ec2-18-223-156-61.us-east-2.compute.amazonaws.com'
port_3 = '8696'

# ====================
#  node host and port
# ====================
host_4 = 'ec2-3-132-215-60.us-east-2.compute.amazonaws.com'
port_4 = '8695'

# ====================
#  node host and port
# ====================
host_diagram = 'localhost'
port_diagram = '8293'

# ====================
#  node host and port
# ====================
host_node = 'ec2-52-14-203-178.us-east-2.compute.amazonaws.com'
port_node = '8694'


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
    data_list = []
    for i in range(int(char_length)+2):
        data_list.append(data_string)
    data_string = "".join(data_list)
    STRING = data_string
    # print("data_string =", data_string)
    return data_string


#### CTRL + C