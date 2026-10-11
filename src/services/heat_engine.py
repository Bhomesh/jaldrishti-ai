"""
JalDrishti AI - Extreme Heatwave & Stull Wet-Bulb Temperature Engine
Calculates Physiological Heat Index and Wet-Bulb Thresholds (Stull Formula, 2011)
Author: Bhomesh Razdan (Lead Architect)
"""

import math
from typing import Dict, Any
from ..core.models import HeatStressReading, HeatRiskLevel

def calculate_wet_bulb_temperature(t_c: float, rh_pct: float) -> float:
    """
    Stull's empirical equation (2011) for Wet-Bulb Temperature (valid for RH 5% - 99% and T -20°C to 50°C).
    Accurate to within 1°C of psychrometric tables.
    """
    term1 = t_c * math.atan(0.151977 * math.sqrt(rh_pct + 8.313659))
    term2 = math.atan(t_c + rh_pct)
    term3 = -math.atan(rh_pct - 1.676331)
    term4 = 0.00391838 * (rh_pct ** 1.5) * math.atan(0.023101 * rh_pct)
    term5 = -4.686035
    tw = term1 + term2 + term3 + term4 + term5
    return round(tw, 1)

def calculate_heat_index(t_c: float, rh_pct: float) -> float:
    """NOAA Heat Index Rothfusz polynomial approximation in Celsius."""
    # Convert Celsius to Fahrenheit
    t_f = (t_c * 9.0 / 5.0) + 32.0
    
    # Rothfusz Regression
    hi_f = (-42.379 +
            2.04901523 * t_f +
            10.14333127 * rh_pct -
            0.22475541 * t_f * rh_pct -
            0.00683783 * (t_f ** 2) -
            0.05481717 * (rh_pct ** 2) +
            0.00122874 * (t_f ** 2) * rh_pct +
            0.00085282 * t_f * (rh_pct ** 2) -
            0.00000199 * (t_f ** 2) * (rh_pct ** 2))
            
    # Convert back to Celsius
    hi_c = (hi_f - 32.0) * 5.0 / 9.0
    return round(hi_c, 1)

class HeatStressEngine:
    """Engine assessing heatwaves and wet-bulb physiological risk."""

    def assess_zone(self, zone_name: str, ambient_temp_c: float, relative_humidity_pct: float) -> HeatStressReading:
        hi_c = calculate_heat_index(ambient_temp_c, relative_humidity_pct)
        wb_c = calculate_wet_bulb_temperature(ambient_temp_c, relative_humidity_pct)

        if wb_c < 26.0:
            risk = HeatRiskLevel.SAFE
            safe_minutes = 240
            adv = "Comfortable outdoor thermal condition. Maintain normal hydration."
        elif wb_c < 29.0:
            risk = HeatRiskLevel.CAUTION
            safe_minutes = 90
            adv = "Heat stress possible during prolonged exertion. Drink ORS/electrolytes and rest in shade."
        elif wb_c < 32.0:
            risk = HeatRiskLevel.EXTREME
            safe_minutes = 30
            adv = "Severe danger of heat cramps, exhaustion, and sunstroke. Limit outdoor physical labor to 30 mins."
        else:
            risk = HeatRiskLevel.LETHAL
            safe_minutes = 10
            adv = "CRITICAL EMERGENCY: Human thermoregulation impaired (sweat cannot evaporate). Mandatory work stoppage, activate misting stations and cool roofs."

        return HeatStressReading(
            zone_name=zone_name,
            ambient_temp_c=ambient_temp_c,
            relative_humidity_pct=relative_humidity_pct,
            heat_index_c=hi_c,
            wet_bulb_temp_c=wb_c,
            risk_level=risk,
            max_safe_outdoor_minutes=safe_minutes,
            advisory=adv
        )
