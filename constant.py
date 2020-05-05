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
host = 'localhost'
port = '8262'

# ====================
#  node host and port
# ====================
host_1 = 'localhost'
port_1 = '8258'

# ====================
#  node host and port
# ====================
host_2 = 'localhost'
port_2 = '8257'

# ====================
#  node host and port
# ====================
host_3 = 'localhost'
port_3 = '8256'

# ====================
#  node host and port
# ====================
host_4 = 'localhost'
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
