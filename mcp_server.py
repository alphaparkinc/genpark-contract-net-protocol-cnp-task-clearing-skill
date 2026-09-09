"""MCP Server for Contract Net Protocol Skill."""
import json
import sys
from client import ContractNetManager

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "clear_contract_net",
                            "description": "Clear Contract Net Protocol bids and award task",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "task": {"type": "object"},
                                    "bids": {
                                        "type": "array",
                                        "items": {
                                            "type": "object",
                                            "properties": {
                                                "agent_id": {"type": "string"},
                                                "cost": {"type": "number"}
                                            },
                                            "required": ["agent_id", "cost"]
                                        }
                                    }
                                },
                                "required": ["task", "bids"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                award = ContractNetManager.evaluate_bids(args["task"], args["bids"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(award)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
