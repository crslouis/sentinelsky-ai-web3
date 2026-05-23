#!/usr/bin/env python3
"""
SentinelSky AI Agent Demo

This demo showcases the intelligence layer using MOCK DATA ONLY.
No real credentials, wallets, or transactions are involved.
"""

import json
import time
from datetime import datetime
from typing import Dict, List

# Mock data for demonstration
MOCK_OPPORTUNITIES = [
    {
        "id": "opp_001",
        "type": "airdrop",
        "project": "LayerZero Testnet",
        "chain": "Ethereum Sepolia",
        "status": "active",
        "deadline": "2026-06-30",
        "requirements": ["Connect wallet", "Bridge tokens", "Complete tasks"],
        "estimated_value": "TBD"
    },
    {
        "id": "opp_002",
        "type": "testnet",
        "project": "Arbitrum Orbit",
        "chain": "Arbitrum Sepolia",
        "status": "active",
        "deadline": "2026-07-15",
        "requirements": ["Deploy contract", "Interact with protocol"],
        "estimated_value": "TBD"
    },
    {
        "id": "opp_003",
        "type": "airdrop",
        "project": "zkSync Era Campaign",
        "chain": "zkSync Sepolia",
        "status": "upcoming",
        "deadline": "2026-08-01",
        "requirements": ["Waitlist registration", "Social tasks"],
        "estimated_value": "TBD"
    }
]

MOCK_WALLET = {
    "address": "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
    "chain": "Ethereum Sepolia",
    "balance": "1.5 ETH (testnet)",
    "note": "This is a MOCK wallet address for demo purposes only"
}


class SentinelSkyAgent:
    """Demo agent with mock data"""
    
    def __init__(self):
        self.opportunities = MOCK_OPPORTUNITIES
        self.wallet = MOCK_WALLET
        
    def scan_opportunities(self) -> List[Dict]:
        """Simulate scanning for opportunities"""
        print("🔍 Scanning Web3 opportunities...")
        time.sleep(1)
        print(f"✅ Found {len(self.opportunities)} opportunities\n")
        return self.opportunities
    
    def analyze_opportunity(self, opp_id: str) -> Dict:
        """Simulate analyzing a specific opportunity"""
        opp = next((o for o in self.opportunities if o["id"] == opp_id), None)
        if not opp:
            return {"error": "Opportunity not found"}
        
        print(f"📊 Analyzing {opp['project']}...")
        time.sleep(1)
        
        analysis = {
            "opportunity": opp,
            "risk_level": "low",
            "time_required": "15-30 minutes",
            "recommended_action": "Review requirements and proceed with caution",
            "safety_checks": [
                "✅ Official project verified",
                "✅ No private key required",
                "✅ Testnet environment",
                "⚠️  Human approval required for all transactions"
            ]
        }
        
        return analysis
    
    def get_wallet_status(self) -> Dict:
        """Return mock wallet status"""
        return self.wallet
    
    def simulate_workflow(self, opp_id: str) -> Dict:
        """Simulate a complete workflow (NO REAL EXECUTION)"""
        print(f"\n🤖 Simulating workflow for opportunity: {opp_id}")
        print("=" * 60)
        
        # Step 1: Analyze
        analysis = self.analyze_opportunity(opp_id)
        if "error" in analysis:
            return analysis
        
        print("\n📋 Analysis Complete:")
        print(json.dumps(analysis, indent=2))
        
        # Step 2: Prepare actions
        print("\n🔧 Preparing actions...")
        time.sleep(1)
        actions = [
            {"step": 1, "action": "Navigate to project website", "status": "simulated"},
            {"step": 2, "action": "Connect wallet (approval required)", "status": "pending_approval"},
            {"step": 3, "action": "Complete required tasks", "status": "pending"},
            {"step": 4, "action": "Submit verification", "status": "pending"}
        ]
        
        print("✅ Action plan created")
        for action in actions:
            print(f"  {action['step']}. {action['action']} - {action['status']}")
        
        # Step 3: Safety reminder
        print("\n⚠️  SAFETY REMINDER:")
        print("  • This is a SIMULATION using mock data")
        print("  • Real execution requires explicit user approval")
        print("  • Never share private keys or seed phrases")
        print("  • Always verify transactions independently")
        
        return {
            "status": "simulation_complete",
            "opportunity": opp_id,
            "analysis": analysis,
            "actions": actions,
            "timestamp": datetime.now().isoformat()
        }


def main():
    """Main demo function"""
    print("=" * 60)
    print("🛡️  SentinelSky AI - Agent Demo")
    print("=" * 60)
    print("⚠️  DEMO MODE: Using mock data only")
    print("=" * 60)
    print()
    
    agent = SentinelSkyAgent()
    
    # Demo 1: Scan opportunities
    opportunities = agent.scan_opportunities()
    for opp in opportunities:
        print(f"📌 {opp['project']} ({opp['type']})")
        print(f"   Chain: {opp['chain']}")
        print(f"   Status: {opp['status']}")
        print(f"   Deadline: {opp['deadline']}")
        print()
    
    # Demo 2: Wallet status
    print("💼 Wallet Status:")
    wallet = agent.get_wallet_status()
    print(json.dumps(wallet, indent=2))
    print()
    
    # Demo 3: Simulate workflow
    result = agent.simulate_workflow("opp_001")
    
    print("\n" + "=" * 60)
    print("✅ Demo Complete")
    print("=" * 60)
    print("\n📝 Summary:")
    print(f"  • Scanned {len(opportunities)} opportunities")
    print(f"  • Analyzed 1 opportunity in detail")
    print(f"  • Simulated workflow with safety checks")
    print(f"  • All data is MOCK - no real execution")
    print()


if __name__ == "__main__":
    main()
