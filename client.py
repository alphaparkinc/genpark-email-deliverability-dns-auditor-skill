class EmailDeliverabilityDNSClient:
    def audit(self, domain: str) -> dict:
        return {"is_valid": True}