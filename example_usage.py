"""Example usage for Contract Net Protocol Skill."""
from client import ContractNetManager

def main():
    print("Executing Contract Net Protocol...")
    task = {"id": "COMPUTE_RENDER_JOB_01", "complexity": 500}
    bids = [
        {"agent_id": "worker_node_1", "cost": 42.5},
        {"agent_id": "worker_node_2", "cost": 29.0},
        {"agent_id": "worker_node_3", "cost": 34.0}
    ]
    award = ContractNetManager.evaluate_bids(task, bids)
    print("Contract Award:", award)
    assert award["winner"] == "worker_node_2"
    assert award["clearing_price"] == 29.0
    print("Contract Net Protocol verified successfully!")

if __name__ == "__main__":
    main()
