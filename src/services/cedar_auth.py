"""
JalDrishti AI - AWS Cedar Policy Authorization Engine
Controls roles: Citizen, WardEngineer, MunicipalHydrologist, DisasterAdmin
Author: Bhomesh Razdan (Lead Architect)
"""

from typing import Dict, Any, Tuple

class CedarPolicyEngine:
    def __init__(self):
        self.policies = [
            {
                "id": "policy::permit_citizen_read",
                "effect": "permit",
                "principal_roles": ["Citizen", "WardEngineer", "MunicipalHydrologist", "Admin"],
                "actions": ["Action::ViewFloodMap", "Action::ReportWaterlogging", "Action::RequestTanker", "Action::CalculateRWH"],
                "resource_types": ["FloodSensor", "TankerLogistics", "HeatReading"]
            },
            {
                "id": "policy::permit_ward_engineer",
                "effect": "permit",
                "principal_roles": ["WardEngineer", "Admin"],
                "actions": ["Action::ActivatePump", "Action::UpdateDrainStatus"],
                "resource_types": ["UnderpassDrain"]
            },
            {
                "id": "policy::permit_municipal_dispatch",
                "effect": "permit",
                "principal_roles": ["MunicipalHydrologist", "Admin"],
                "actions": ["Action::DispatchTankerFleet", "Action::DeclareFloodEmergency"],
                "resource_types": ["TankerFleet", "EmergencyProtocol"]
            }
        ]

    def is_authorized(self, principal_role: str, action: str, resource_type: str, context: Dict[str, Any] = None) -> Tuple[bool, str]:
        for policy in self.policies:
            if (policy["effect"] == "permit" and
                principal_role in policy["principal_roles"] and
                action in policy["actions"] and
                resource_type in policy["resource_types"]):
                return True, f"PERMIT by {policy['id']}"
                
        return False, f"DENY: Unauthorized action {action} by {principal_role} on {resource_type}"
