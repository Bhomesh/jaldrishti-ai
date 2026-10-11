"""
JalDrishti AI - Core Data Models and Hydrological Entities
Author: Bhomesh Razdan (Lead Architect)
Event: Bharat Builds Tour - Environmental Hacks (Track 02: Heat and Water)
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from enum import Enum
import time

class FloodSeverity(str, Enum):
    NORMAL = "Normal"               # < 10 cm water
    WATERLOGGED = "Waterlogged"     # 10 - 25 cm (traffic slowed)
    HAZARDOUS = "Hazardous"         # 25 - 50 cm (sedans stranded)
    SUBMERGED = "Submerged"         # > 50 cm (critical emergency / closed)

class HeatRiskLevel(str, Enum):
    SAFE = "Safe"                   # Wet-bulb < 26°C
    CAUTION = "Caution"             # Wet-bulb 26 - 29°C
    EXTREME_CAUTION = "Extreme"     # Wet-bulb 29 - 32°C
    LETHAL = "Lethal Heat Stress"   # Wet-bulb > 32°C

@dataclass
class UnderpassSensorNode:
    sensor_id: str
    location_name: str
    latitude: float
    longitude: float
    water_depth_cm: float
    flow_rate_lps: float            # Liters per second
    drain_status: str               # "Clear", "Partially Choked", "Blocked"
    pump_active: bool
    severity: FloodSeverity
    updated_at: float = field(default_factory=time.time)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d['severity'] = self.severity.value
        return d

@dataclass
class HeatStressReading:
    zone_name: str
    ambient_temp_c: float
    relative_humidity_pct: float
    heat_index_c: float
    wet_bulb_temp_c: float
    risk_level: HeatRiskLevel
    max_safe_outdoor_minutes: int
    advisory: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d['risk_level'] = self.risk_level.value
        return d

@dataclass
class WaterTankerDispatchNode:
    colony_id: str
    colony_name: str
    zone: str
    population: int
    groundwater_table_depth_m: float
    daily_shortage_liters: float
    assigned_tankers: int
    fair_share_priority_score: float # 0 - 100

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
