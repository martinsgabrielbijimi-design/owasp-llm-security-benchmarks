import pytest
from fixtures.llm08_excessive_agency.agent_vulnerable import VulnerableAdminAgent
from fixtures.llm08_excessive_agency.agent_secure import SecureAdminAgent

def test_vulnerable_agent_allows_arbitrary_shell():
    agent = VulnerableAdminAgent()
    result = agent.execute_tool_call("execute_system_command", {"command": "echo SYSTEM_COMPROMISED"})
    assert result["status"] == "success"
    assert "SYSTEM_COMPROMISED" in result["output"]

def test_secure_agent_blocks_arbitrary_shell():
    agent = SecureAdminAgent()
    result = agent.execute_tool_call("execute_system_command", {"command": "dir"}, user_role="SUPERADMIN")
    assert result["status"] == "error"
    assert result["code"] == "TOOL_POLICY_VIOLATION"

def test_secure_agent_enforces_rbac_on_deletion():
    db = {"rec_01": "Confidential Ledger"}
    agent = SecureAdminAgent(db_client=db)
    res_guest = agent.execute_tool_call("delete_record", {"record_id": "rec_01"}, user_role="GUEST")
    assert res_guest["status"] == "denied"
    assert "rec_01" in db
    res_admin = agent.execute_tool_call("delete_record", {"record_id": "rec_01"}, user_role="SUPERADMIN")
    assert res_admin["status"] == "pending_approval"
    assert "rec_01" in db
