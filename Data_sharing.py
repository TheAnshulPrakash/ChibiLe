from queue import Queue

# Global shared queue for thread-safe operations
shared_data_queue = Queue(maxsize=1)
whisper_data=Queue(maxsize=1)
comm_port=Queue()

comm_port_send=Queue(maxsize=2)

BackGround=Queue(maxsize=1)
ForeGround=Queue(maxsize=1)
ForeGround.put("'#660000'")
BackGround.put("'#fcd7e1'")