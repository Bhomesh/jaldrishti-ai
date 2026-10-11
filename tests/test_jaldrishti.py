"""
Unit Tests for JalDrishti AI - All Engines & Handlers
Author: Bhomesh Razdan (Lead Architect)
"""

import unittest
import json
from src.services.flood_engine import FloodSentinelEngine, calculate_peak_runoff_m3_per_sec, classify_flood_severity
from src.services.heat_engine import HeatStressEngine, calculate_wet_bulb_temperature, calculate_heat_index
from src.services.tanker_engine import TankerLogisticsEngine
from src.services.cedar_auth import CedarPolicyEngine
from src.lambda_handlers import (
    handler_get_underpasses,
    handler_simulate_storm,
    handler_assess_heatwave,
    handler_get_tanker_allocations,
    handler_calculate_rwh,
    handler_cedar_auth
)

class TestJalDrishti(unittest.TestCase):

    def test_flood_rational_runoff(self):
        # 50 mm/h rain on 10 hectares with C=0.85 -> Q = 0.85*50*10 / 360 = ~1.18 m3/s
        q = calculate_peak_runoff_m3_per_sec(50.0, 10.0, 0.85)
        self.assertAlmostEqual(q, 1.181, places=2)

    def test_underpass_simulation(self):
        eng = FloodSentinelEngine()
        sim = eng.simulate_storm_runoff(65.0, 90)
        self.assertIn("submerged_underpasses", sim)
        self.assertGreater(sim["submerged_underpasses"], 0)
        self.assertGreater(len(sim["emergency_alerts"]), 0)

    def test_stull_wet_bulb_calculation(self):
        # At 35°C and 70% RH, wet bulb is ~30.5°C
        wb = calculate_wet_bulb_temperature(35.0, 70.0)
        self.assertTrue(29.0 < wb < 32.0, f"Expected wet bulb around 30.5°C, got {wb}")

    def test_heat_stress_assessment(self):
        eng = HeatStressEngine()
        reading = eng.assess_zone("Delhi Ridge", 44.0, 60.0)
        self.assertIn("Lethal", reading.risk_level.value)
        self.assertLessEqual(reading.max_safe_outdoor_minutes, 15)

    def test_tanker_fair_share_dispatch(self):
        eng = TankerLogisticsEngine()
        dispatch = eng.optimize_dispatch(30)
        self.assertEqual(dispatch["allocated_tankers"], 30)
        self.assertGreater(len(dispatch["allocations"]), 3)

    def test_rwh_potential(self):
        eng = TankerLogisticsEngine()
        rwh = eng.calculate_rainwater_harvesting_potential(150.0)
        self.assertGreater(rwh["harvestable_volume_liters_year"], 50000)

    def test_cedar_authorization(self):
        eng = CedarPolicyEngine()
        allowed, _ = eng.is_authorized("Citizen", "Action::ViewFloodMap", "FloodSensor")
        self.assertTrue(allowed)
        denied, _ = eng.is_authorized("Citizen", "Action::ActivatePump", "UnderpassDrain")
        self.assertFalse(denied)

    def test_lambda_handlers(self):
        res = handler_get_underpasses({"httpMethod": "GET"})
        self.assertEqual(res["statusCode"], 200)

        res = handler_assess_heatwave({"httpMethod": "GET", "queryStringParameters": {"temp_c": "42", "rh_pct": "50"}})
        self.assertEqual(res["statusCode"], 200)

if __name__ == "__main__":
    unittest.main()
