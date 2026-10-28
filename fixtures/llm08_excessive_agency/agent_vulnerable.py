"""Vulnerable Agent: Unrestricted execution capabilities without privilege boundaries."""
import subprocess
from typing import Dict, Any

class VulnerableAdminAgent:
    def __init__(self, db_client=None):
        self.db = db_client or {}

    def execute_tool_call(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if tool_name == "execute_system_command":
            command = params.get("command", "")
            output = subprocess.check_output(command, shell=True, text=True)
            return {"status": "success", "output": output.strip()}
        elif tool_name == "delete_record":
            record_id = params.get("record_id")
            if record_id in self.db:
                del self.db[record_id]
                return {"status": "success", "message": f"Record {record_id} deleted"}
            return {"status": "not_found", "message": "Record missing"}
        raise ValueError(f"Unrecognized tool: {tool_name}")
