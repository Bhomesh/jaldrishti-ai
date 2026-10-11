"""
JalDrishti AI - Configuration
Author: Bhomesh Razdan (Lead Architect)
"""

import os

class Settings:
    PROJECT_NAME: str = "JalDrishti AI"
    VERSION: str = "1.0.0"
    TRACK: str = "Track 02: Heat and Water"
    LEAD_ARCHITECT: str = "Bhomesh Razdan"
    AWS_REGION: str = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
    DYNAMODB_FLOOD_TABLE: str = os.getenv("DYNAMODB_FLOOD_TABLE", "JalDrishti-Underpass-Sensors")
    DYNAMODB_TANKER_TABLE: str = os.getenv("DYNAMODB_TANKER_TABLE", "JalDrishti-Tanker-Logistics")
    SNS_FLOOD_ALERT_ARN: str = os.getenv("SNS_FLOOD_ALERT_ARN", "arn:aws:sns:ap-south-1:123456789012:JalDrishti-Emergency")

settings = Settings()
