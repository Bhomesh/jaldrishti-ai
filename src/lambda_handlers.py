"""
JalDrishti AI - AWS Lambda Handlers
Author: Bhomesh Razdan (Lead Architect)
"""

import json
from typing import Dict, Any
from .services.flood_engine import FloodSentinelEngine
from .services.heat_engine import HeatStressEngine
from .services.tanker_engine import TankerLogisticsEngine
from .services.cedar_auth import CedarPolicyEngine

flood_engine = FloodSentinelEngine()
heat_engine = HeatStressEngine()
tanker_engine = TankerLogisticsEngine()
cedar_engine = CedarPolicyEngine()

def build_response(status_code: int, body: Any) -> Dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,Authorization"
        },
        "body": json.dumps(body)
    }

def handler_get_underpasses(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    nodes = [n.to_dict() for n in flood_engine.get_all_nodes()]
    return build_response(200, {
        "count": len(nodes),
        "source": "Delhi Municipal Stormwater Telemetry Network",
        "nodes": nodes
    })

def handler_simulate_storm(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    params = event.get("queryStringParameters") or {}
    try:
        rain = float(params.get("rain_mm_h", 45.0))
        duration = int(params.get("duration_mins", 60))
    except ValueError:
        return build_response(400, {"error": "Invalid simulation parameters"})

    sim = flood_engine.simulate_storm_runoff(rain, duration)
    return build_response(200, sim)

def handler_assess_heatwave(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    params = event.get("queryStringParameters") or {}
    try:
        temp = float(params.get("temp_c", 43.5))
        rh = float(params.get("rh_pct", 58.0))
        zone = params.get("zone", "Central Delhi (Connaught Place Heat Island)")
    except ValueError:
        return build_response(400, {"error": "Invalid temperature/humidity values"})

    reading = heat_engine.assess_zone(zone, temp, rh)
    return build_response(200, reading.to_dict())

def handler_get_tanker_allocations(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    params = event.get("queryStringParameters") or {}
    fleet = int(params.get("fleet_size", 30))
    result = tanker_engine.optimize_dispatch(fleet)
    return build_response(200, result)

def handler_calculate_rwh(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    params = event.get("queryStringParameters") or {}
    try:
        roof = float(params.get("roof_sqm", 120.0))
    except ValueError:
        return build_response(400, {"error": "Invalid roof area"})
    rwh = tanker_engine.calculate_rainwater_harvesting_potential(roof)
    return build_response(200, rwh)

def handler_cedar_auth(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    try:
        body = json.loads(event.get("body", "{}"))
        role = body.get("role", "Citizen")
        action = body.get("action", "Action::ViewFloodMap")
        res = body.get("resource", "FloodSensor")
    except Exception:
        return build_response(400, {"error": "Invalid JSON body"})

    allowed, reason = cedar_engine.is_authorized(role, action, res)
    return build_response(200, {
        "principal_role": role,
        "action": action,
        "resource": res,
        "decision": "ALLOW" if allowed else "DENY",
        "reason": reason
    })
