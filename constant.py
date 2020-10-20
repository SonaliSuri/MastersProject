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
host = 'ec2-3-23-129-83.us-east-2.compute.amazonaws.com'
port = '8262'

# ====================
#  node host and port
# ====================
host_1 = 'ec2-3-138-202-205.us-east-2.compute.amazonaws.com'
port_1 = '8258'

# ====================
#  node host and port
# ====================
host_2 = 'ec2-3-12-102-120.us-east-2.compute.amazonaws.com'
port_2 = '8257'

# ====================
#  node host and port
# ====================
host_3 = 'ec2-18-219-28-245.us-east-2.compute.amazonaws.com'
port_3 = '8256'

# ====================
#  node host and port
# ====================
host_4 = 'ec2-3-14-28-219.us-east-2.compute.amazonaws.com'
port_4 = '8255'

# ====================
#  node host and port
# ====================
host_diagram = 'localhost'
port_diagram = '8273'

# ====================
#  node host and port
# ====================
host_node = 'localhost'
port_node = '8254'


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
MSG = "msg"

# ======
#
# =====
open_brac = "{"
close_brac = "}"

conf_nodes = [{'host': host_1, 'port': int(port_1)}]
