# Xiaomi MiMo Integration

## Overview

SentinelSky AI is powered by **Xiaomi MiMo AI models** for all intelligence and reasoning tasks. This document details our integration strategy, model usage, and safety measures.

## Why Xiaomi MiMo?

### Superior Capabilities
- **Long context window**: Essential for analyzing large smart contracts and threat data
- **Multilingual excellence**: Critical for global Web3 threat intelligence
- **Strong reasoning**: Required for complex risk assessment
- **Fast inference**: Enables real-time threat detection

### Perfect Fit for Web3 Security
- **Code understanding**: Analyzes Solidity, Vyper, Rust smart contracts
- **Pattern recognition**: Detects scam patterns across languages and platforms
- **Risk reasoning**: Evaluates multi-factor risks with nuanced judgment
- **Synthesis**: Combines findings from multiple agents into coherent reports

## Model Selection

### MiMo V2.5 (Standard Model)

**Strengths**:
- Fast inference speed
- Lower token cost
- Excellent for extraction and summarization
- Strong multilingual support

**Use Cases in SentinelSky AI**:
1. **Threat Scout Agent**: Extract threat indicators from feeds
2. **Social Trust Agent**: Analyze social media patterns
3. **Report Generator Agent**: Synthesize findings into reports
4. **Multilingual Threat Research**: Translate and localize threat intelligence

**Example Usage**:
```python
# Extract phishing indicators from raw data
response = await mimo_v25.extract(
    text=raw_threat_data,
    schema={
        "domain": "string",
        "type": "enum[phishing, scam, malware]",
        "severity": "enum[low, medium, high, critical]",
        "indicators": "array[string]"
    }
)
```

### MiMo V2.5 Pro (Advanced Model)

**Strengths**:
- Superior reasoning capability
- Deep context understanding
- Complex pattern detection
- Multi-factor risk assessment

**Use Cases in SentinelSky AI**:
1. **Phishing Detector Agent**: Deep risk reasoning for suspicious sites
2. **Contract Scanner Agent**: Vulnerability analysis and exploit detection
3. **Rugpull Risk Agent**: Multi-factor probability scoring
4. **Tokenomics Analyst Agent**: Economic modeling and projections

**Example Usage**:
```python
# Analyze smart contract for vulnerabilities
response = await mimo_v25_pro.reason(
    context={
        "contract_code": solidity_code,
        "bytecode": bytecode_analysis,
        "transaction_history": recent_txs,
        "similar_exploits": known_patterns
    },
    question="""
    Analyze this smart contract for security vulnerabilities.
    Focus on: reentrancy, access control, integer overflow,
    unchecked external calls, and hidden backdoors.
    
    For each vulnerability found:
    1. Describe the vulnerability
    2. Show the vulnerable code
    3. Explain the exploit scenario
    4. Assess the risk level
    5. Provide remediation steps
    """
)
```

## Integration Architecture

### API Client

```python
import httpx
from typing import Dict, List, Optional

class MiMoClient:
    """Xiaomi MiMo API client for SentinelSky AI"""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.xiaomi.com/mimo",
        model_v25: str = "mimo-v2.5",
        model_v25_pro: str = "mimo-v2.5-pro"
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.model_v25 = model_v25
        self.model_v25_pro = model_v25_pro
        self.client = httpx.AsyncClient(
            timeout=300.0,
            headers={"Authorization": f"Bearer {api_key}"}
        )
    
    async def extract(
        self,
        text: str,
        schema: Dict,
        model: str = None
    ) -> Dict:
        """Extract structured data using MiMo V2.5"""
        model = model or self.model_v25
        
        response = await self.client.post(
            f"{self.base_url}/extract",
            json={
                "model": model,
                "text": text,
                "schema": schema
            }
        )
        response.raise_for_status()
        return response.json()
    
    async def reason(
        self,
        context: Dict,
        question: str,
        model: str = None
    ) -> Dict:
        """Deep reasoning using MiMo V2.5 Pro"""
        model = model or self.model_v25_pro
        
        response = await self.client.post(
            f"{self.base_url}/reason",
            json={
                "model": model,
                "context": context,
                "question": question
            }
        )
        response.raise_for_status()
        return response.json()
    
    async def synthesize(
        self,
        inputs: List[Dict],
        instruction: str,
        model: str = None
    ) -> Dict:
        """Synthesize multiple agent results using MiMo V2.5 Pro"""
        model = model or self.model_v25_pro
        
        response = await self.client.post(
            f"{self.base_url}/synthesize",
            json={
                "model": model,
                "inputs": inputs,
                "instruction": instruction
            }
        )
        response.raise_for_status()
        return response.json()
    
    async def translate(
        self,
        text: str,
        source_lang: str,
        target_lang: str,
        model: str = None
    ) -> str:
        """Translate text using MiMo V2.5"""
        model = model or self.model_v25
        
        response = await self.client.post(
            f"{self.base_url}/translate",
            json={
                "model": model,
                "text": text,
                "source_lang": source_lang,
                "target_lang": target_lang
            }
        )
        response.raise_for_status()
        return response.json()["translated_text"]
```

### Error Handling

```python
class MiMoError(Exception):
    """Base exception for MiMo API errors"""
    pass

class MiMoQuotaExceeded(MiMoError):
    """Token quota exceeded"""
    pass

class MiMoRateLimited(MiMoError):
    """Rate limit exceeded"""
    pass

async def call_mimo_with_retry(
    func,
    max_retries: int = 3,
    backoff_factor: float = 2.0
):
    """Call MiMo API with exponential backoff retry"""
    for attempt in range(max_retries):
        try:
            return await func()
        except MiMoRateLimited:
            if attempt == max_retries - 1:
                raise
            wait_time = backoff_factor ** attempt
            await asyncio.sleep(wait_time)
        except MiMoQuotaExceeded:
            # Don't retry quota errors
            raise
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(1.0)
```

### Token Management

```python
class TokenBudgetManager:
    """Manage daily token budget"""
    
    def __init__(self, daily_budget: int = 38_000_000):
        self.daily_budget = daily_budget
        self.used_today = 0
        self.reset_time = self._get_next_midnight()
    
    async def request_tokens(
        self,
        agent: str,
        estimated_tokens: int,
        priority: int = 3
    ) -> bool:
        """Request token allocation for an agent"""
        # Reset counter at midnight
        if datetime.now() >= self.reset_time:
            self.used_today = 0
            self.reset_time = self._get_next_midnight()
        
        # Check if we have budget
        if self.used_today + estimated_tokens > self.daily_budget:
            if priority <= 2:  # Critical or high priority
                # Allow critical requests to exceed budget
                logger.warning(
                    f"Exceeding daily budget for critical request: {agent}"
                )
                self.used_today += estimated_tokens
                return True
            else:
                # Defer non-critical requests
                logger.info(
                    f"Deferring non-critical request: {agent}"
                )
                return False
        
        self.used_today += estimated_tokens
        return True
    
    def _get_next_midnight(self) -> datetime:
        """Get next midnight UTC"""
        now = datetime.now(timezone.utc)
        tomorrow = now + timedelta(days=1)
        return tomorrow.replace(hour=0, minute=0, second=0, microsecond=0)
```

## Agent Integration Examples

### Phishing Detector Agent

```python
class PhishingDetectorAgent:
    def __init__(self, mimo_client: MiMoClient):
        self.mimo = mimo_client
    
    async def analyze(self, url: str) -> PhishingReport:
        # Fetch page data
        page_data = await self.fetch_page(url)
        domain_info = await self.analyze_domain(url)
        
        # Use MiMo V2.5 Pro for deep reasoning
        analysis = await self.mimo.reason(
            context={
                "url": url,
                "page_content": page_data.content,
                "page_title": page_data.title,
                "domain_age": domain_info.age_days,
                "ssl_valid": domain_info.ssl_valid,
                "whois_data": domain_info.whois,
                "similar_domains": domain_info.similar
            },
            question="""
            Analyze this website for phishing indicators.
            
            Consider:
            1. Domain legitimacy (age, SSL, WHOIS)
            2. Visual similarity to known brands
            3. Suspicious content patterns
            4. Social engineering tactics
            5. Technical indicators (redirects, iframes, etc.)
            
            Provide:
            - Risk score (0-100)
            - Confidence level
            - Key indicators found
            - Recommendation (safe/suspicious/malicious)
            """
        )
        
        return PhishingReport(
            url=url,
            risk_score=analysis["risk_score"],
            confidence=analysis["confidence"],
            indicators=analysis["indicators"],
            recommendation=analysis["recommendation"],
            reasoning=analysis["reasoning"]
        )
```

### Contract Scanner Agent

```python
class ContractScannerAgent:
    def __init__(self, mimo_client: MiMoClient):
        self.mimo = mimo_client
    
    async def scan(self, address: str, chain: str) -> ContractReport:
        # Fetch contract data
        code = await self.fetch_contract_code(address, chain)
        bytecode = await self.fetch_bytecode(address, chain)
        txs = await self.fetch_recent_transactions(address, chain)
        
        # Use MiMo V2.5 Pro for vulnerability analysis
        analysis = await self.mimo.reason(
            context={
                "address": address,
                "chain": chain,
                "source_code": code,
                "bytecode_analysis": bytecode,
                "recent_transactions": txs,
                "known_vulnerabilities": VULNERABILITY_PATTERNS
            },
            question="""
            Perform a comprehensive security analysis of this smart contract.
            
            Check for:
            1. Reentrancy vulnerabilities
            2. Access control issues
            3. Integer overflow/underflow
            4. Unchecked external calls
            5. Denial of service vectors
            6. Front-running vulnerabilities
            7. Hidden backdoors or admin functions
            
            For each vulnerability:
            - Describe the issue
            - Show vulnerable code
            - Explain exploit scenario
            - Assess severity (low/medium/high/critical)
            - Provide fix recommendations
            
            Calculate overall risk score (0-100).
            """
        )
        
        return ContractReport(
            address=address,
            chain=chain,
            risk_score=analysis["risk_score"],
            vulnerabilities=analysis["vulnerabilities"],
            recommendations=analysis["recommendations"],
            detailed_analysis=analysis["detailed_analysis"]
        )
```

### Multi-Agent Synthesis

```python
class ReportGeneratorAgent:
    def __init__(self, mimo_client: MiMoClient):
        self.mimo = mimo_client
    
    async def generate_report(
        self,
        contract_analysis: Dict,
        tokenomics_analysis: Dict,
        social_analysis: Dict
    ) -> ComprehensiveReport:
        # Use MiMo V2.5 Pro to synthesize findings
        synthesis = await self.mimo.synthesize(
            inputs=[
                {
                    "agent": "Contract Scanner",
                    "findings": contract_analysis
                },
                {
                    "agent": "Tokenomics Analyst",
                    "findings": tokenomics_analysis
                },
                {
                    "agent": "Social Trust",
                    "findings": social_analysis
                }
            ],
            instruction="""
            Synthesize findings from multiple security agents into
            a comprehensive risk assessment report.
            
            Structure:
            1. Executive Summary
            2. Overall Risk Score (weighted average)
            3. Key Findings by Category
            4. Critical Issues (if any)
            5. Recommendations
            6. Conclusion
            
            Use clear, non-technical language for executive summary.
            Provide technical details in findings section.
            Prioritize actionable recommendations.
            """
        )
        
        return ComprehensiveReport(
            executive_summary=synthesis["executive_summary"],
            overall_risk_score=synthesis["overall_risk_score"],
            findings=synthesis["findings"],
            recommendations=synthesis["recommendations"]
        )
```

## Security and Privacy

### API Key Management

**Server-Side Only**:
```python
# ✅ CORRECT: API key on server
# Backend (FastAPI)
mimo_client = MiMoClient(
    api_key=os.environ["MIMO_API_KEY"]
)

# ❌ WRONG: Never expose API key in frontend
# Frontend (React) - DON'T DO THIS
const mimoKey = "sk-mimo-xxx"  // NEVER!
```

**Environment Variables**:
```bash
# .env (server-side only, never commit)
MIMO_API_KEY=sk-mimo-xxxxxxxxxxxxxxxxxx
MIMO_BASE_URL=https://api.xiaomi.com/mimo
MIMO_MODEL=mimo-v2.5
MIMO_PRO_MODEL=mimo-v2.5-pro
```

**Key Rotation**:
```python
# Rotate API keys every 90 days
async def rotate_api_key():
    new_key = await request_new_key()
    update_environment_variable("MIMO_API_KEY", new_key)
    restart_services()
```

### Public Demo Mode

**Mock Data Only**:
```python
class MiMoClientWrapper:
    def __init__(self, api_key: str, demo_mode: bool = False):
        self.demo_mode = demo_mode
        if not demo_mode:
            self.client = MiMoClient(api_key)
        else:
            self.client = MockMiMoClient()
    
    async def analyze(self, data):
        if self.demo_mode:
            # Return pre-generated mock results
            return MOCK_ANALYSIS_RESULTS[data.type]
        else:
            # Real MiMo API call
            return await self.client.analyze(data)
```

**Public Demo Configuration**:
```python
# Public demo uses mock data only
PUBLIC_DEMO_MODE = os.getenv("PUBLIC_DEMO_MODE", "true") == "true"

if PUBLIC_DEMO_MODE:
    # No real MiMo API calls
    # No real blockchain data
    # No real threat detection
    mimo_client = MockMiMoClient()
else:
    # Real MiMo integration (admin only)
    mimo_client = MiMoClient(api_key=os.environ["MIMO_API_KEY"])
```

### Data Privacy

**No Sensitive Data to MiMo**:
```python
# ✅ CORRECT: Only send public data
await mimo.analyze({
    "contract_address": "0x123...",  # Public
    "source_code": code,              # Public
    "chain": "ethereum"               # Public
})

# ❌ WRONG: Never send private data
await mimo.analyze({
    "private_key": "0xabc...",        # NEVER!
    "seed_phrase": "word1 word2...",  # NEVER!
    "user_email": "user@example.com"  # NEVER!
})
```

**Data Retention**:
- MiMo API calls: No persistent storage by default
- Request logs: Anonymized, 30-day retention
- Analysis results: Cached locally, no PII

## Monitoring and Optimization

### Token Usage Tracking

```python
class TokenUsageTracker:
    async def track_usage(
        self,
        agent: str,
        model: str,
        tokens_used: int,
        request_id: str
    ):
        await db.insert_token_usage({
            "timestamp": datetime.now(),
            "agent": agent,
            "model": model,
            "tokens_used": tokens_used,
            "request_id": request_id
        })
        
        # Update metrics
        metrics.increment(f"tokens.{agent}.{model}", tokens_used)
```

### Performance Monitoring

```python
# Track MiMo API latency
with metrics.timer("mimo.api.latency"):
    result = await mimo.analyze(data)

# Track success/failure rates
metrics.increment("mimo.api.success")
# or
metrics.increment("mimo.api.error")
```

### Cost Optimization

```python
# Cache frequently requested analyses
@cache(ttl=3600)  # 1 hour
async def analyze_contract(address: str):
    return await contract_scanner.scan(address)

# Batch similar requests
async def batch_analyze(addresses: List[str]):
    # Single MiMo call for multiple contracts
    return await mimo.batch_analyze(addresses)
```

## Future Enhancements

### Phase 2
- Fine-tuned MiMo models for Web3 security
- Custom prompt templates per agent
- Streaming responses for real-time updates

### Phase 3
- On-device MiMo deployment for privacy
- Federated learning for threat patterns
- Custom model training on proprietary data

### Phase 4
- MiMo model marketplace integration
- Community-contributed security models
- Decentralized AI inference network

## Conclusion

Xiaomi MiMo integration is the foundation of SentinelSky AI's intelligence capabilities:

- **MiMo V2.5**: Fast, efficient extraction and summarization
- **MiMo V2.5 Pro**: Deep reasoning for critical security decisions
- **38M tokens/day**: Comprehensive Web3 threat coverage
- **Server-side only**: Secure API key management
- **Public demo**: Mock data for transparency

SentinelSky AI demonstrates the power of Xiaomi MiMo for real-world Web3 security applications.

---

**For more information**:
- [Application Description](./application_description.md)
- [Architecture](./architecture.md)
- [Token Consumption](./token_consumption.md)
- [Safety Guidelines](./safety.md)
