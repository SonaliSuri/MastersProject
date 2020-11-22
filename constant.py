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
host = 'ec2-54-226-110-230.compute-1.amazonaws.com'
port = '8292'

# ====================
#  node host and port
# ====================
host_1 = 'ec2-54-164-88-108.compute-1.amazonaws.com'
port_1 = '8298'

# ====================
#  node host and port
# ====================
host_2 = 'ec2-184-72-127-166.compute-1.amazonaws.com'
port_2 = '8299'

# ====================
#  node host and port
# ====================
host_3 = 'ec2-54-242-182-233.compute-1.amazonaws.com'
port_3 = '8296'

# ====================
#  node host and port
# ====================
host_4 = 'ec2-3-95-31-142.compute-1.amazonaws.com'
port_4 = '8295'

# ====================
#  node host and port
# ====================
host_diagram = 'localhost'
port_diagram = '8293'

# ====================
#  node host and port
# ====================
host_node = 'ec2-54-226-110-230.compute-1.amazonaws.com'
port_node = '8294'


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