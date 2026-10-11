// JalDrishti AI - AWS Cedar Policies
// Author: Bhomesh Razdan (Lead Architect)

permit (
    principal in JalDrishti::Role::"Citizen",
    action in [
        JalDrishti::Action::"ViewFloodMap",
        JalDrishti::Action::"ReportWaterlogging",
        JalDrishti::Action::"RequestTanker",
        JalDrishti::Action::"CalculateRWH"
    ],
    resource
);

permit (
    principal in JalDrishti::Role::"WardEngineer",
    action in [
        JalDrishti::Action::"ActivatePump",
        JalDrishti::Action::"UpdateDrainStatus"
    ],
    resource is JalDrishti::Resource::"UnderpassDrain"
);

permit (
    principal in JalDrishti::Role::"MunicipalHydrologist",
    action in [
        JalDrishti::Action::"DispatchTankerFleet",
        JalDrishti::Action::"DeclareFloodEmergency"
    ],
    resource is JalDrishti::Resource::"EmergencyProtocol"
);

permit (
    principal in JalDrishti::Role::"Admin",
    action,
    resource
);
