"""
JalDrishti AI - Urban Flood & Underpass Submergence Sentinel Engine
Formulas: Rational Hydrological Runoff Q = (C * I * A) / 360 & Drain Choking Index
Author: Bhomesh Razdan (Lead Architect)
"""

from typing import List, Dict, Any, Optional
from ..core.models import UnderpassSensorNode, FloodSeverity

def classify_flood_severity(depth_cm: float) -> FloodSeverity:
    if depth_cm < 10.0:
        return FloodSeverity.NORMAL
    elif depth_cm < 25.0:
        return FloodSeverity.WATERLOGGED
    elif depth_cm < 50.0:
        return FloodSeverity.HAZARDOUS
    else:
        return FloodSeverity.SUBMERGED

def calculate_peak_runoff_m3_per_sec(rainfall_intensity_mm_h: float, area_hectares: float, runoff_coeff: float = 0.85) -> float:
    """Rational Method equation: Q = (C * I * A) / 360 (Peak urban stormwater runoff)."""
    if rainfall_intensity_mm_h <= 0 or area_hectares <= 0:
        return 0.0
    return round((runoff_coeff * rainfall_intensity_mm_h * area_hectares) / 360.0, 3)

class FloodSentinelEngine:
    """Real-time urban drainage and underpass monitoring engine."""

    def __init__(self):
        self._nodes: Dict[str, UnderpassSensorNode] = {}
        self._load_delhi_underpasses()

    def _load_delhi_underpasses(self):
        # Known chronic waterlogging hotspots in Delhi NCR
        nodes_data = [
            ("FL-DEL-01", "Minto Bridge Underpass", 28.6385, 77.2248, 62.0, 85.0, "Partially Choked", True),
            ("FL-DEL-02", "Pul Prahladpur Underpass", 28.4988, 77.2882, 78.5, 110.0, "Blocked", True),
            ("FL-DEL-03", "Zakhira Flyover Underpass", 28.6672, 77.1585, 34.0, 45.0, "Partially Choked", False),
            ("FL-DEL-04", "Azadpur Underpass (GT Karnal)", 28.7073, 77.1758, 22.0, 30.0, "Clear", False),
            ("FL-DEL-05", "Tilak Bridge Underpass", 28.6250, 77.2390, 15.0, 20.0, "Clear", False),
            ("FL-DEL-06", "Moolchand Underpass (Ring Road)", 28.5680, 77.2340, 8.0, 12.0, "Clear", False),
            ("FL-DEL-07", "Dwarka Sector 21 Underpass", 28.5520, 77.0580, 5.0, 8.0, "Clear", False),
        ]

        for sid, name, lat, lon, depth, flow, drain, pump in nodes_data:
            severity = classify_flood_severity(depth)
            node = UnderpassSensorNode(
                sensor_id=sid,
                location_name=name,
                latitude=lat,
                longitude=lon,
                water_depth_cm=depth,
                flow_rate_lps=flow,
                drain_status=drain,
                pump_active=pump,
                severity=severity
            )
            self._nodes[sid] = node

    def get_all_nodes(self) -> List[UnderpassSensorNode]:
        return list(self._nodes.values())

    def update_sensor_reading(self, sensor_id: str, new_depth_cm: float, new_flow_lps: float, drain_status: str, pump_active: bool) -> Optional[UnderpassSensorNode]:
        if sensor_id not in self._nodes:
            return None
        node = self._nodes[sensor_id]
        node.water_depth_cm = new_depth_cm
        node.flow_rate_lps = new_flow_lps
        node.drain_status = drain_status
        node.pump_active = pump_active
        node.severity = classify_flood_severity(new_depth_cm)
        return node

    def simulate_storm_runoff(self, rainfall_mm_h: float, duration_minutes: int) -> Dict[str, Any]:
        """Simulates city-wide drainage response to incoming cloudburst or heavy monsoon."""
        submerged_count = 0
        total_inflow_m3_s = 0.0
        alerts = []

        for node in self._nodes.values():
            catchment_ha = 12.5 # approx underpass catchment area
            inflow = calculate_peak_runoff_m3_per_sec(rainfall_mm_h, catchment_ha)
            total_inflow_m3_s += inflow

            # Depth increases if drain is choked
            drain_efficiency = 0.3 if node.drain_status == "Blocked" else 0.6 if node.drain_status == "Partially Choked" else 0.95
            projected_depth = node.water_depth_cm + (rainfall_mm_h * 0.4 * (1.0 - drain_efficiency))
            node.water_depth_cm = round(projected_depth, 1)
            node.severity = classify_flood_severity(projected_depth)

            if node.severity in [FloodSeverity.HAZARDOUS, FloodSeverity.SUBMERGED]:
                submerged_count += 1
                alerts.append({
                    "underpass": node.location_name,
                    "depth_cm": node.water_depth_cm,
                    "severity": node.severity.value,
                    "action_required": "Deploy high-capacity dewatering pump (4000 GPM) and divert arterial traffic."
                })

        return {
            "rainfall_event_mm_h": rainfall_mm_h,
            "duration_minutes": duration_minutes,
            "cumulative_stormwater_inflow_m3_s": round(total_inflow_m3_s, 2),
            "submerged_underpasses": submerged_count,
            "total_monitored": len(self._nodes),
            "emergency_alerts": alerts
        }
